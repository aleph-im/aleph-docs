# Confidential Computing Requirements

## System

Creating a confidential virtual machine currently requires the creation of an encrypted disk on a machine you trust. This machine must run Linux on x86_64 (64 bit CPU, most recent PCs but not Mac).

The documentation below assumes a Linux system based on [Debian](https://www.debian.org/) or [Ubuntu](https://ubuntu.com/), but the procedure can be adjusted to other distributions. 

This requirement will be lifted in the future with confidential virtual machines that encrypt the filesystem themself.

## Software required

 * The [aleph-client](https://github.com/aleph-im/aleph-client/) command-line tool
 * The [sevctl](https://github.com/virtee/sevctl) tool from AMD
 * A [OpenSSH](https://www.openssh.com/) keypair
 * An [IPFS Server](https://github.com/ipfs/kubo)
 * Optional: [Qemu](https://www.qemu.org/) to test your VM locally

### aleph-client

Install [pipx](https://github.com/pypa/pipx?tab=readme-ov-file#on-linux):
```shell
sudo apt update
sudo apt install pipx
pipx ensurepath
```

Then install `aleph-client`: 
```shell
pipx install aleph-client
```

### sevctl

Install [Rust and Cargo](https://doc.rust-lang.org/cargo/getting-started/installation.html):
```shell
curl https://sh.rustup.rs -sSf | sh
```
 
Then install [sevctl](https://github.com/virtee/sevctl) using `cargo`:
```shell
cargo install sevctl
set --export PATH ~.cargo/bin:$PATH
```

### guestmount

This tool is used to create the encrypted disk.

On systems based on Debian/Ubuntu:

```shell
apt install guestmount
```

Note: Up to 119 dependencies and 178 MB of additional disk space will be used.

## IPFS Server

The encrypted filesystem you will create is close to 4 GB.

In order to copy in on the aleph.im decentralized network, you will first
need to make it available on IPFS.
