from .. import env

STREAMING = {
    "BROKER_URL": env("STREAMING_BROKER_URL"),
    "QUEUES": {
        "{{cookiecutter.package_name}}": {
            "routing": ["hope.*.*"],
        },
    },
}
