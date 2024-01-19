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

from burly import *
from plano import *

@command
def build():
    burly_in = read("burly.sh").strip()

    boilerplate = extract_boilerplate(burly_in)
    functions = extract_functions(burly_in)

    core_function_names = [
        "assert",
        "random_number",
        "print", "print_result", "print_section",
        "run", "log", "fail",
        "green", "yellow", "red", "bold",
        "init_logging", "handle_exit",
        "enable_debug_mode",
        "enable_strict_mode",
    ]

    install_function_names = core_function_names + [
        "program_is_available",
        "check_required_programs",
        "check_required_network_resources",
        "check_writable_directories",
        "ask_to_proceed",
        "extract_archive",
    ]

    uninstall_function_names = core_function_names + [
        "check_writable_directories",
        "ask_to_proceed",
    ]

    burly_out = [boilerplate]

    for name in install_function_names:
        burly_out.append(functions[name])

    install_sh_in = read("install.sh.in")
    install_sh = replace(install_sh_in, "@burly@", "\n".join(burly_out))

    burly_out = [boilerplate]

    for name in uninstall_function_names:
        burly_out.append(functions[name])

    uninstall_sh_in = read("uninstall.sh.in")
    uninstall_sh = replace(uninstall_sh_in, "@burly@", "\n".join(burly_out))

    write("install.sh", install_sh)
    write("uninstall.sh", uninstall_sh)

@command(passthrough=True)
def test(verbose=False, passthrough_args=[]):
    build()

    if verbose:
        passthrough_args.append("--verbose")

    import tests

    PlanoTestCommand(tests).main(passthrough_args)

@command
def clean():
    remove(find(".", "__pycache__"))

@command
def lint():
    """
    Use shellcheck to scan for problems
    """
    check_program("shellcheck")

    build()

    run("shellcheck --shell sh --enable all --exclude SC3043,SC2310,SC2312 install.sh uninstall.sh")

@command
def update_burly():
    """
    Update the embedded Burly repo
    """
    make_dir("external")
    remove("external/burly-main")
    run("curl -sfL https://github.com/ssorj/burly/archive/main.tar.gz | tar -C external -xz", shell=True)
