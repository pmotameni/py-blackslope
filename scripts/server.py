import os
import subprocess

IS_WINDOWS = os.name == "nt"


def main():
    cmd = ["python", "manage.py", "runserver", "0.0.0.0:8000"]
    subprocess.run(cmd, shell=IS_WINDOWS)
