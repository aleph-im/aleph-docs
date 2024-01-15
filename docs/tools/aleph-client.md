# Command line

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
```

## Test using Docker

Use the aleph.im client from within Docker or Podman with:

```shell
docker run --rm -ti -v $(pwd)/data:/data ghcr.io/aleph-im/aleph-client/aleph-client:master --help
```

> ⚠️ This will use an ephemeral key that will be discarded when stopping the container.
