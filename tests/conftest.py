# Copyright (c) QuantCo 2023-2024
# SPDX-License-Identifier: LicenseRef-QuantCo

import subprocess
from itertools import chain
from pathlib import Path

import pytest

from .utils import git_user


@pytest.fixture
def generate_project(tmp_path):
    def _generate(extra_data=None):
        if extra_data is None:
            extra_data = {}

        data = {
            "tool": "ansible-lint",
            "url": "https://github.com/ansible/ansible-lint",
            "entry": "ansible-lint",
        }
        data.update(extra_data)

        directory = Path(__file__).parent
        with git_user():
            data = chain.from_iterable(
                [("--data", f"{key}={value}") for key, value in data.items()]
            )
            subprocess.check_call(
                [
                    "copier",
                    "copy",
                    "--defaults",
                    "--vcs-ref=HEAD",
                    "--trust",
                    *data,
                    directory.parent,
                    tmp_path,
                ]
            )

        return tmp_path

    return _generate


@pytest.fixture
def generated_project(generate_project):
    return generate_project()
