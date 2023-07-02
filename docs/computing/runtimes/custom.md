# Custom Runtimes

Custom runtimes can be created by customizing the filesystem of Linux distributions or 
[entirely from scratch](https://linuxfromscratch.org/lfs/).

## Base filesystem

Refer to the installation guide of your distribution for the procedure to obtain a base root filesystem.

> ⚠️ Only 64-bit Intel/AMD processors (x86_64) are supported on the network at the moment . Make sure you build runtimes on that architecture.

### Debian Bullseye

```shell
mkdir ./rootfs
debootstrap --arch=amd64 --variant=minbase bullseye ./rootfs http://deb.debian.org/debian/
```

### Ubuntu 22.04

```shell
mkdir ./rootfs
debootstrap --arch=amd64 jammy ./rootfs http://archive.ubuntu.com/ubuntu/
```

[//]: # (#### NixOS - TODO)


Following the next steps, you will be able to create and customize your own Debian based runtime:

## 1. Install required dependencies

First you need to install the required tools to be able to generate you own runtime.

Using Debian and Ubuntu systems:

```shell
sudo apt-get install debootstrap squashfs-toolssquashfs-tools
```

Using Nix:
```shell
nix-shell -p debootstrap squashfsTools
```

## 2. Obtain the build scripts

Download the files `create_disk_image.sh`, `init0.sh` and `init1.py` from the 
[official runtime](existing.md#official-runtime-with-debian-11-python-39-and-nodejs-14):

[https://github.com/aleph-im/aleph-vm/tree/main/runtimes/aleph-debian-11-python](https://github.com/aleph-im/aleph-vm/tree/main/runtimes/aleph-debian-11-python)

Customize these files to suit your needs.

## 3. Build a new runtime

Running the script `create_disk_image.sh` as root will create a file named `rootfs.squashfs`:

```shell
sudo ./create_disk_image.sh
```

## 4. Publish the runtime on aleph.im

```shell
aleph file pin ./rootfs.squashfs
```

This command will provide you with the `item_hash` of the custom runtime, 
that you can then use when creating the program.
