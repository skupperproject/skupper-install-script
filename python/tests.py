#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

from plano import *

ENV["TEST_INSTALL_PREFIX"] = make_temp_dir(prefix="skupper-install-script-")

@test
def install():
    run(f"sh install.sh")

@test
def uninstall():
    run(f"sh install.sh")
    run(f"sh uninstall.sh")

@test
def option_help():
    run(f"sh install.sh -h")
    run(f"sh install.sh --help")
    run(f"sh uninstall.sh -h")
    run(f"sh uninstall.sh --help")

    with expect_error():
        run(f"sh install.sh --nope")

    with expect_error():
        run(f"sh uninstall.sh --not-at-all")

    with expect_error():
        run(f"sh install.sh nope")

    with expect_error():
        run(f"sh uninstall.sh not-at-all")

@test
def option_interactive():
    run(f"echo yes | sh install.sh --interactive", shell=True)
    run(f"echo no | sh install.sh --interactive", shell=True)
    run(f"echo yes | sh uninstall.sh --interactive", shell=True)
    run(f"echo no | sh uninstall.sh --interactive", shell=True)

@test
def option_verbose():
    run(f"sh install.sh --verbose")
    run(f"sh uninstall.sh --verbose")

def test_shell(shell):
    if not which(shell):
        skip_test(f"Shell '{shell}' is not available")

    run(f"{shell} install.sh") # No existing installation and no existing backup
    run(f"{shell} install.sh") # Creates a backup
    run(f"{shell} install.sh") # Backs up the backup
    run(f"{shell} uninstall.sh")

def test_version(version):
    run(f"sh install.sh --version {version}")

def test_scheme(scheme):
    run(f"sh install.sh --scheme {scheme}")
    run(f"sh uninstall.sh --scheme {scheme}")

for shell in "ash", "bash", "dash", "ksh", "mksh", "yash", "zsh":
    add_test(f"shell-{shell}", test_shell, shell)

for version in "latest", "main", "1.5.3":
    add_test(f"version-{version}", test_version, version)

for scheme in "home", "opt":
    add_test(f"scheme-{scheme}", test_scheme, scheme)
