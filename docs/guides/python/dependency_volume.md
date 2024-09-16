# Add Python dependencies to a program

Many Python programs require additional packages beyond those present on the system by default.
While you could of course create your own runtime, there is a faster and easier solution.
The official aleph.im Python runtimes automatically includes `/opt/packages` in the Python search path (`PYTHONPATH`). Mounting a volume on this path will make any Python module or package present in that volume importable from your program.

Using a dedicated volume for your dependencies has several advantages:

- No need to create a custom runtime
- Update your dependencies without updating all your program
- Use the same dependencies for multiple programs.s

This tutorial will teach you how to create a volume for your Python dependencies
and add it to your program.

## Why use a dedicated volume?

Dependencies can be updated independently of your program.
For example, you may want to update the version of a dependency without modifying the rest of your application.
You could also reuse the same dependencies for multiple programs.

## Set up your environment (Debian/Ubuntu Linux)

> ℹ If you use macOS, see the section at the end of this tutorial to set up your environment.

```shell
sudo apt install python-pip python-venv squashfs-tools
```

```shell
pip install aleph-client
```

## Create the volume

Install the packages in a directory. `pip` has an option to specify an alternative installation directory.

```shell
pip install -t my-packages -r requirements.txt
```

Create a `squashfs` volume:

```shell
mksquashfs ./my-packages packages.squashfs
```

## Upload the dependency volume

To use this volume inside a program, we need the aleph.im message hash storing
this volume, meaning that we need to upload the volume to aleph.im first.

### Without IPFS (small size)

```shell
aleph file upload packages.squashfs
```

### With IPFS
```shell
/opt/go-ipfs/ipfs daemon
```

```shell
ipfs add packages.squashfs
```
| added QmWWX6BaaRkRSr2iNdwH5e29ACPg2nCHHXTRTfuBmVm3Ga venv.squashfs

```shell
aleph file pin QmWWX6BaaRkRSr2iNdwH5e29ACPg2nCHHXTRTfuBmVm3Ga
```

## Create your program

```shell
aleph program upload ./my-program main:app
```

Press Enter at the following prompt to use the default runtime:
```
Ref of runtime ? [bd79839bf96e595a06da5ac0b6ba51dea6f7e2591bb913deccded04d831d29f4]
```

Press `Y` to add extra volumes to your program:
``` 
Add volume ? [y/N] Y
Description: Python Packages
Mount: /opt/packages
Ref: 61f43ab261060ff94838dc94313a70cdb939a5fc6c99924b96d55dcc2c108d03
Use latest version ? [Y/n] Y
```

Finally, press Enter to skip adding more volumes.
```shell
Add volume ? [y/N]
```

Your program should be uploaded on aleph.im.

## [macOS] Set up your environment with Vagrant

Setting up the environment to create your virtualenv volume is a little more complex on macOS.
This section will guide you through the installation of VirtualBox and Vagrant to create a Linux
development environment on your Mac.

### Install VirtualBox
You will need VirtualBox, a free and open-source hosted hypervisor (or virtual machine manager) for the next step.

You can download and install it <a href="https://www.virtualbox.org/wiki/Downloads">here </a>.

### Install Vagrant
Vagrant is an open-source software product for building and maintaining portable virtual software development 
environments based on VirtualBox.
Run the following command to install it (make sure [homebrew](https://brew.sh) is installed on your Mac).

```shell
brew install vagrant
```

Once Vagrant is installed, go to your working repository and initialize Vagrant:

```shell
vagrant init boxomatic/debian-11
```

A `Vagrantfile` (in Ruby) will be created, you can consult it if you wish.
Instantiate a new virtual machine with the following command:

```shell
vagrant up
```

If this does not work, check out you System Preferences > Security and Privacy and allow 
the "System software from developer" in the bottom of the window.
Once the command finishes, your virtual machine will be booted and ready!

### Set Vagrantfile configuration

Open the vagrantfile and add following `config.vm.box`

```shell
config.vm.network "forwarded_port", guest:8000, host:8000
```
