# Immutable volumes

An immutable volume is a file that contains a [Squashfs filesystem](https://www.kernel.org/doc/html/latest/filesystems/squashfs.html) and can be mounted read-only inside the virtual machine that runs programs in [on-demand](../on_demand.md) or [persistent](../persistent.md) execution modes.

Such volume is typically used to provide additional libraries or data to the program. 

Such volume can be published and updated independently of the program. This allows different processes or entities
to manage the lifecycle of different components of the programs.

> ℹ️ Squashfs is a standard Linux format. You can always mount it on a Linux system to test things out.

## Providing additional data

You can provide additional data to your program by bundling them in an immutable volume.

### 1. Create a Squashfs volume from the additional data

```shell
mksquashfs ./custom-data data.squashfs
```

### 2. Publish the file on Aleph

```shell
aleph file pin ./data.squashfs
```

This command will provide you with the `item_hash` of the immutable volume, 
that you can then use when creating the program.

## Providing additional Python libraries

You can provide additional Python libraries to your program by bundling them in an immutable volume mounted on `/opt/packages`.

### 1. Create a directory containing the dependencies

```shell
mkdir ./packages
pip3 install -t ./packages -r ./requirements.txt
```

### 2. Create a Squashfs volume from the directory

```shell
mksquashfs ./packages packages.squashfs
```

### 3. Publish the file on Aleph

```shell
aleph file pin ./packages.squashfs
```

This command will provide you with the `item_hash` of the immutable volume, 
that you can then use when creating the program.

[//]: # (## Providing additional Node libraries)

