import subprocess


def on_config(config):
    try:
        output = subprocess.check_output("git describe --always --dirty", shell=True)
        version = output.decode("utf8").strip()
    except subprocess.CalledProcessError:
        version = 'local-dev'

    config.setdefault("extra", {})["version"] = version
    return config
