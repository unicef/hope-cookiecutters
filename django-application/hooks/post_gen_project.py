import os
import subprocess
import sys
from glob import glob

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "


def run(*cmd: str):
    try:
        result = subprocess.run(cmd,
                                env={"PATH": f"{os.getcwd()}/.venv/bin/:{os.environ['PATH']}",
                                     "PYTHONPATH": f"{os.getcwd()}/src/:",
                                     "DJANGO_SETTINGS_MODULE": f"{{ cookiecutter.package_name}}.config.settings",
                                     },
#                                capture_output=True,
#                                check=True,
                                text=True,
                                )
        if result.returncode != 0:
            print(f"❌ Command failed with exit code {result.returncode}", file=sys.stderr)
            print(f"Command failed with exit code {result.returncode}")
            sys.exit(result.returncode)
    except subprocess.CalledProcessError as e:
        print(str(e))


def run_venv(*cmd: str):
    return run(*cmd)


def main():
    print(f"{SUCCESS}Project structure created in {os.getcwd()}.{TERMINATOR}")
    print(f"{SUCCESS}Start setup project.{TERMINATOR}")
    print(f"{INFO}.. Initializing git. Creating main/develop branches.{TERMINATOR}")
    run("git", "init", "--initial-branch", "main")
    run("git", "checkout", "-b", "develop")

    print(f"{INFO}.. Generating uv.lock file.{TERMINATOR}")
    run("uv", "lock", "-q")

    print(f"{INFO}.. Setup .gitignore and .envrc files.{TERMINATOR}")
    run("mv", "_.gitignore", ".gitignore")
    run("mv", "_.envrc", ".envrc")

    print(f"{INFO}.. Creating virtualenv.{TERMINATOR}")
    run("uv", "venv", "-q")
    run("uv", "sync", "-q")

    print(f"{INFO}.. Installing pre-commit hooks.{TERMINATOR}")
    run_venv(f"{os.getcwd()}/.venv/bin/pre-commit", "install")

    print(f"{INFO}.. Add files to git.{TERMINATOR}")
    run("git", "add", ".")

    print(f"{SUCCESS}Project setup completed.{TERMINATOR}")



if __name__ == "__main__":
    main()
