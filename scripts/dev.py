import os
import subprocess

IS_WINDOWS = os.name == "nt"


def install():
    cmd = ["poetry", "install", "&&", "pre-commit", "install"]
    subprocess.run(cmd, shell=IS_WINDOWS)


def test():
    cmd = ["poetry", "run", "pytest"]
    subprocess.run(cmd, shell=IS_WINDOWS)


def pre_commit():
    cmd = ["pre-commit", "run", "--all-files"]
    subprocess.run(cmd, shell=IS_WINDOWS)


def lint():
    cmd = [
        "poetry",
        "run",
        "isort",
        "." "poetry",
        "run",
        "black",
        ".",
        "&&",
        "poetry",
        "run",
        "pylint",
        "--load-plugins",
        "pylint_django",
        "--django-settings-module=blackslope.settings",
        "apiapp",
    ]
    subprocess.run(cmd, shell=IS_WINDOWS)
