# Copyright (c) QuantCo 2023-2024
# SPDX-License-Identifier: LicenseRef-QuantCo

import re
import subprocess

import pytest


def test_generation(generate_project):
    path = generate_project()

    assert (path / ".pre-commit-hooks.yaml").exists()


def test_generation_incorrect_params(generate_project):
    with pytest.raises(subprocess.CalledProcessError):
        generate_project({"url": "www.google.com"})


def test_version_in_environment_yml(generate_project):
    path = generate_project()

    assert (path / "environment.yml").exists()
    with open(path / "environment.yml") as f:
        environment = f.read()
        print(environment)
    assert re.search(r"ansible-lint=\d+\.\d+\.\d+", environment)
