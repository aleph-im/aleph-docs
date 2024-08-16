# Aleph.im Command-Line Interface

All the features of aleph.im can be accessed from a terminal using the 
[aleph-client](https://github.com/aleph-im/aleph-client/) command-line interface.

## Requirements

On Linux:

```shell
apt-get install -y python3-pip libsecp256k1-dev
```

On macOS:

```shell
brew tap cuber/homebrew-libsecp256k1
brew install libsecp256k1
```

## Installation

We recommend using [pipx](https://github.com/pypa/pipx) to install Python based command-line tools on Linux and macOS
systems.

`pipx` installs tools in isolated environments, ensuring that it does not mess up with your system.
Install `pipx` from [the `pipx` documentation](https://github.com/pypa/pipx?tab=readme-ov-file#on-linux)
using `apt` or `brew`.

Once `pipx` setup, [aleph-client from PyPI](https://pypi.org/project/aleph-client/) can be installed using:

```shell
pipx install aleph-client
```

Advanced users may instead create a [Python virtual environment](https://docs.python.org/3/library/venv.html)
and install `aleph-client` in it:

```shell
python3 -m venv my-virtual-environment
source ./my-virtual-environment/activate
pip install aleph-client
```

In both cases, the command `aleph` should now be available to use.

## Using Docker

The tools is also available as a [OCI Image Format](https://specs.opencontainers.org/image-spec/)
to use with [Docker](https://www.docker.com/) or [Podman](https://podman.io/).

```shell
docker run --rm -ti \
    -v $(pwd)/data:/data \
    ghcr.io/aleph-im/aleph-client/aleph-client:master \
    --help
```


> ⚠️ This will use an ephemeral key that will be discarded when stopping the container.

## Usage

All available commands can be found from the help menu:
```shell
aleph --help
                                                                                                
 Usage: aleph [OPTIONS] COMMAND [ARGS]...                                                                  
                                                                                                           
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|pwsh]  Install completion for the specified       │
│                                                              shell.                                     │
│                                                              [default: None]                            │
│ --show-completion           [bash|zsh|fish|powershell|pwsh]  Show completion for the specified shell,   │
│                                                              to copy it or customize the installation.  │
│                                                              [default: None]                            │
│ --help                                                       Show this message and exit.                │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────────────────╮
│ about             Display the information of Aleph CLI                                                 │
│ account           Manage account                                                                        │
│ aggregate         Manage aggregate messages on aleph.im                                                 │
│ domain            Manage custom Domain (dns) on aleph.im                                                │
│ file              File uploading and pinning on IPFS and aleph.im                                       │
│ instance          Manage instances (VMs) on aleph.im network                                            │
│ message           Post, amend, watch and forget messages on aleph.im                                    │
│ node              Get node info on aleph.im network                                                     │
│ program           Upload and update programs on aleph.im VM                                             │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

And are documented on the [usage page](usage.md).
