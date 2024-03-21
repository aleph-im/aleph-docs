# Installation

Access all the features of aleph.im from your terminal using the 
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

Install [aleph-client from PyPI](https://pypi.org/project/aleph-client/) using `pip`:

```shell
pip install aleph-client
```

## Usage

Explore the available commands from the help menu:
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
│ about             Display the informations of Aleph CLI                                                 │
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

Or check out the [documentation page](usage.md).

## Test using Docker

Use the aleph.im client from within Docker or Podman with:

```shell
docker run --rm -ti -v $(pwd)/data:/data ghcr.io/aleph-im/aleph-client/aleph-client:master --help
```

> ⚠️ This will use an ephemeral key that will be discarded when stopping the container.
