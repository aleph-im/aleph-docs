# Immutable Volumes

An immutable volume is a file containing
a [Squashfs filesystem](https://www.kernel.org/doc/html/latest/filesystems/squashfs.html) that can be mounted read-only
inside the virtual machine running programs in [on-demand](../index.md#on-demand-execution) or [persistent](../index.md#persistent-execution) execution
modes. This type of volume is typically used to provide additional libraries or data to the program.

Immutable volumes have the following properties:

- `comment`: A custom comment from the user about the volume.
- `mount`: The path on the filesystem of the virtual machine to mount the volume.
- `ref`: The `item_hash` of the STORE message that references the uploaded filesystem.
- `use_latest`: A flag indicating that the program should be restarted to use the last version of the volume.

> ℹ️ Squashfs is a standard Linux format and can be mounted on any Linux system to test.

## Providing Additional Data

Additional data can be provided to a program by bundling it in an immutable volume.

### 1. Create a Squashfs volume from the data

```shell
mksquashfs ./custom-data data.squashfs
```

### 2. Publish the file on aleph.im

```shell
aleph file upload ./data.squashfs
```

This command will provide you with the `item_hash` of the immutable volume, which you can then use to create the
program.

## Providing Additional Python Libraries

Additional Python libraries can be provided to a program by bundling them in an immutable volume mounted
on `/opt/packages`.

### 1. Create a directory that contains the dependencies

```shell
mkdir ./packages
pip3 install -t ./packages -r ./requirements.txt
```

### 2. Create a Squashfs volume from the directory

```shell
mksquashfs ./packages packages.squashfs
```

### 3. Publish the file on aleph.im

```shell
aleph file upload ./packages.squashfs
```

This command will provide you with the `item_hash` of the immutable volume, which you can then use to create the
program.