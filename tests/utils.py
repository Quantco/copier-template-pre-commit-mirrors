# Copyright (c) QuantCo 2023-2024
# SPDX-License-Identifier: LicenseRef-QuantCo

import contextlib
import os
import subprocess


@contextlib.contextmanager
def change_directory(dir):
    prev_dir = os.getcwd()
    os.chdir(dir)
    yield
    os.chdir(prev_dir)


@contextlib.contextmanager
def git_user(name="ForrestQuant", email="forrest.quant@quantco.com"):
    variables = {
        "GIT_AUTHOR_NAME": name,
        "GIT_COMMITTER_NAME": name,
        "GIT_AUTHOR_EMAIL": email,
        "GIT_COMMITTER_EMAIL": email,
    }
    old_variables = {}

    for key, value in variables.items():
        old_variables[key] = os.environ.get(key)
        os.environ[key] = value

    yield

    for key, value in old_variables.items():
        if value is not None:
            os.environ[key] = value
        else:
            del os.environ[key]


def git_init_add(to_add="."):
    result = subprocess.run(["git", "init"])
    result.check_returncode()
    result = subprocess.run(["git", "add", to_add])
    result.check_returncode()
