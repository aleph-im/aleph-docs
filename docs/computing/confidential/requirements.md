# Confidential Computing Requirements

## System

Creating a confidential virtual machine currently requires the creation of an encrypted disk on a machine you trust.
This machine must run Linux on x86_64 (64 bit CPU, most recent PCs but not Mac) and have IPv6 connectivity.

The documentation below assumes a Linux system based on [Debian](https://www.debian.org/) or [Ubuntu](https://ubuntu.com/), but the procedure can be adjusted to other distributions.

This requirement will be lifted in the future with confidential virtual machines that encrypt the filesystem themself.

## Software required

- The [aleph-client](https://github.com/aleph-im/aleph-client/) command-line tool
- The [sevctl](https://github.com/virtee/sevctl) tool from AMD
- A [OpenSSH](https://www.openssh.com/) keypair
- An [IPFS Server](https://github.com/ipfs/kubo)
- Optional: [Qemu](https://www.qemu.org/) to test your VM locally

### aleph-client

The `aleph-client` command line tool can be installed
following [the documentation here](../../tools/aleph-client/index.md).

### sevctl

Installing [Rust and Cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html):

```shell
curl https://sh.rustup.rs -sSf | sh
```

Some packages may need to be installed on some systems (ex: Ubuntu) in order to build sevctl:

```shell
apt install -y pkg-config libssl-dev asciidoctor
```

The [sevctl](https://github.com/virtee/sevctl) tool can then be installed using `cargo`:

```shell
cargo install sevctl
set --export PATH ~.cargo/bin:$PATH
```

> ℹ️ On Windows, we recommend using [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) following the same previous steps.

### guestmount

This tool is used to create the encrypted disk.

On systems based on Debian/Ubuntu, it can be installed using:

```shell
apt install guestmount
```

Note: Up to 119 dependencies and 178 MB of additional disk space will be used.

## IPFS Server

The encrypted filesystem you will create is close to 4 GB.

In order to copy in on the aleph.im decentralized network, it is required to first
make it available on [IPFS](https://ipfs.tech/).

---

Next: [Creating an encrypted filesystem](./encrypted-disk.md)
