import sys
import cookiecutter.prompt
'''
This pre_gen is to avoid to input tests variables if you don't want to create it
'''

if "{{ cookiecutter.use_transifex }}" == "y":
    cookiecutter.prompt.read_user_variable("transifex_organization","unicef-hope")
    cookiecutter.prompt.read_user_variable("transifex_project","{{ cookiecutter.github_repo }}")

else:
    """{{ cookiecutter.update(
        {
            "transifex_organization": "",
            "transifex_project": "",
        }
    )}}"""
