import os
import shutil
import subprocess
import sys
from glob import glob

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

def run(*cmd: str):
    try:
        subprocess.run(cmd,
                       env={"PATH": f"{os.getcwd()}/.venv/bin/:{os.environ['PATH']}",
                            "PYTHONPATH": f"{os.getcwd()}/src/:",
                            "DJANGO_SETTINGS_MODULE": f"{{ cookiecutter.package_name}}.config.settings",
                            "ADMIN_EMAIL": "",
                            "ADMIN_PASSWORD": "",
                            "ALLOWED_HOSTS": ""
                            },
                       capture_output=True,
                       check=True,
                       text=True,
                       )
    except subprocess.CalledProcessError as e:
        print(f"❌ Error executing {e.cmd} ", file=sys.stderr)
        print(f"Exit code {e.returncode}", file=sys.stderr)
        print(f"{e.stderr}")
        sys.exit(e.returncode)


def run_venv(*cmd: str):
    return run(*cmd)


def run_manage(*args):
    return run("python", "manage.py", *args)


def main():
    print(f"{SUCCESS}Project structure created in {os.getcwd()}.{TERMINATOR}")
    print(f"{SUCCESS}Start setup project.{TERMINATOR}")
    if "{{cookiecutter.use_transifex}}" != "y":
        remove(".tx")

    print(f"{INFO}.. Setup .gitignore and .envrc files.{TERMINATOR}")
    run("mv", "_.gitignore", ".gitignore")
    run("mv", "_.envrc", ".envrc")

    print(f"{INFO}.. Initializing git. Creating main/develop branches.{TERMINATOR}")
    run("git", "init", "--initial-branch", "main")
    run("git", "checkout", "-b", "develop")

    print(f"{INFO}.. Creating virtualenv.{TERMINATOR}")
    run("uv", "venv", "-q")
    run("uv", "sync", "-q")

    print(f"{INFO}.. Generating uv.lock file.{TERMINATOR}")
    run("uv", "lock", "-q")

    print(f"{INFO}.. Setup tailwind.{TERMINATOR}")
    run_manage("tailwind", "-v0", "install")
    print(f"{INFO}.. Installing pre-commit hooks.{TERMINATOR}")
    run_venv(f"{os.getcwd()}/.venv/bin/pre-commit", "install")
    subprocess.call(["touch", *glob("src/{{ cookiecutter.package_name}}/ui/theme/static/js/*.min.js")])

    print(f"{INFO}.. Add files to git.{TERMINATOR}")
    run("git", "add", ".")


    print(f"{INFO}.. Update translations.{TERMINATOR}")
    run_manage("compilemessages")

    print(f"{INFO}.. Run final check.{TERMINATOR}")
    run_manage("check")

    print(f"{SUCCESS}Project setup completed.{TERMINATOR}")



if __name__ == "__main__":
    main()
