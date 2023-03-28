# Choosing runtime

## Introduction

The Aleph.im network machines needs to run a runtime filesystem as a base operating system with all the libraries
and all de dependencies that you need to run your VMs code.

## Types of runtimes

We have different types of runtimes. Each runtime have an OS as a base, and can have some libraries or binaries
already installed.

### Official runtime with Debian 11, Python 3.9 and NodeJS 14

It is the latest stable version of Debian (11), with Python version already added to Debian (3.9) and NodeJs 14. 

### Official min. runtime for binaries (Rust, Go, ...)

It is an Alpine OS runtime with the basic packages already installed, just to run some Linux binaries. Note that
this runtime is **so fast to launch** because don´t have to load any dependencies.

### Another runtime

If you already have a runtime, or you want to create your custom own, you can use this option to specify the Item hash
of the runtime.

## Creating you custom runtime

> ⚠️ Runtime files should be created using a system architecture of x86 64bit.

Following the next steps, you will be able to create and customize your own Debian based runtime:

### Install required dependencies

First you need to install the required tools to be able to generate you own runtime.

For Debian and Ubuntu systems:

```bash
sudo apt-get install debootstrap chroot mksquashfs
```

### Generate the runtime

You can download and use as an example one of the runtimes that we have here:
https://github.com/aleph-im/aleph-vm/tree/main/runtimes

Only executing the `create_disk_image.sh` script as root will generate the root filesystem.

```bash
sudo sh create_disk_image.sh
```

### Publish the runtime

You can follow [this guide](https://ipfs-2.aleph.im/ipfs/QmdyF1cD5WtockpAzLYhgXYJUDY4iXeAKtQuUn1kjsQ3k1/execution/volumes/immutable/) to publish your runtime.

## Conclusion

In this tutorial, you learned how to select or create your runtime to be able to use a function
or an instance inside Aleph.IM network.