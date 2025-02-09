# Copyright 2021 Red Hat
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import pytest

from sretoolbox.binaries import Mtcli, Oc, OperatorSDK, Opm


@pytest.mark.parametrize(
    "params",
    [
        {
            "instance": Mtcli,
            "version": "0.0.0",
        },
        {
            "instance": Oc,
            "version": "4.6.1",
        },
        {
            "instance": Opm,
            "version": "1.15.1",
        },
        {
            "instance": OperatorSDK,
            "version": "1.4.2",
        },
    ],
)
def test_download_binaries(params):
    _ = params["instance"](version=params["version"], download_path="/tmp")
