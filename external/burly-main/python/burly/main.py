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

import re

from plano import *

__all__ = "extract_boilerplate", "extract_functions"

def extract_boilerplate(code):
    boilerplate = re.search(r"# BEGIN BOILERPLATE\n(.*?)\n# END BOILERPLATE", code, re.DOTALL)

    if boilerplate:
        return boilerplate.group(1).strip()

def extract_functions(code):
    functions = dict()
    matches = re.finditer(r"\n(\w+)\s*\(\)\s+{\n.*?\n}", code, re.DOTALL)

    for match in matches:
        functions[match.group(1)] = match.group(0)

    return functions
