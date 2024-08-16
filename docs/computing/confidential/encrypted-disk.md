# Encrypted Virtual Machine image

A virtual machine disk image encrypted with a password only known by the user must be created to ensure confidentiality. 
This way, even the compute resource node running the instance will not be able to access, read, or modify its content.
## Creating an Encrypted Virtual Machine Disk Image using the sample scripts

Scripts are provided, they are specifically designed to create an encrypted VM image for confidential computing purposes.

The provided scripts will:

* Create an encrypted partition.
* Set up a boot partition.
* Generate the required initramfs for decrypting the encrypted partition during boot.

The resulting disk image is designed to work seamlessly with the custom OVMF (Open Virtual Machine Firmware) located in [runtimes/ovmf](https://github.com/aleph-im/aleph-vm/tree/main/runtimes/ovmf). This OVMF version is capable of receiving the decryption key securely via QMP (QEMU Machine Protocol) and passing it to GRUB for disk decryption.

### 0. Requirements

Ensure you have the [requirements](./requirements.md) set up. 

### 1. Retrieving the Scripts
Download the necessary sample scripts from the following repository:<br>
[Aleph VM Examples - Confidential Image](https://github.com/aleph-im/aleph-vm/tree/main/examples/example_confidential_image)

```shell
wget https://raw.githubusercontent.com/aleph-im/aleph-vm/main/examples/example_confidential_image/build_debian_image.sh
wget https://raw.githubusercontent.com/aleph-im/aleph-vm/main/examples/example_confidential_image/setup_debian_rootfs.sh
```

These scripts are specifically designed to create an encrypted VM image for confidential computing purposes.

### 2. Customizing the VM
It is advised to at least add a user with both a password and an SSH key in the sudo group.

You can customize your VM by modifying the `setup_debian_rootfs.sh` script. This script is executed within the VM’s chroot environment, allowing you to tailor the system according to your needs. This allows you to:

* Add a user.
* Install an SSH key.
* Install additional software.
* Modify the default configuration.

Simply add your custom instructions at the end of the `setup_debian_rootfs.sh` script.

### 3. Fetch a base image you can trust

In this example, we use Debian 12.

It is recommended to start from the genericcloud image, as it contain cloud-init, which is used to setup the network when launching the VM.

```shell
wget https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-genericcloud-amd64.qcow2
```

Note: Experiment with using the nocloud image then installing cloud-init have failed to work.
The CRN rely on the feature of cloud-init being enabled (it is per default), other cloud-init feature can be disabled.

### 4. Extract the root filesystem

To do so, we simply need to mount the raw image with `guestmount`.

> Make sure that you stop the VM before exporting the root filesystem.

```shell
sudo mkdir -p /mnt/debian
sudo guestmount \
  --format=qcow2 \
  -a ./debian-12-genericcloud-amd64.qcow2 \
  -o allow_other \
  -i /mnt/debian
```

Then, you can simply copy the root file system to any directory, take caution to preserve the proper permission like the setuid bit with the `--archive` option.

```shell
export ROOT_DIR=./extracted
mkdir ${ROOT_DIR}
sudo cp --archive /mnt/debian/* ${ROOT_DIR}
```

Clean up the mount:

```shell
sudo guestunmount /mnt/debian
sudo rm -r /mnt/debian
```

### 5. Create the encrypted disk

Run the build_debian_image.sh that will create the image with the encrypted disk 
> This script will require sudo for certain commands.

The password option is the *secret* password key, with which the disk will be encrypted, you will need to pass it to launch the VM.  

```shell
bash ./build_debian_image.sh --rootfs-dir  $ROOT_DIR -o ~/destination-image.img --password your-password
```

> Tip: To debug the image creation, pass the `-x` option to bash in front of the script name.

### Optional: Test and further customise your image

The confidential VM can be started locally in QEMU using the following command. From there you can modify it as you wish.

```shell
sudo qemu-system-x86_64 \
  -drive format=raw,file=</path/to/your/image.img> \
  -enable-kvm \
  -m 2048 \
  -nic user,model=virtio \
  -nographic \
  -serial mon:stdio \
  -drive if=pflash,format=raw,unit=0,file=/usr/share/ovmf/OVMF.fd,readonly=on
```

> Note: Once you have entered your password you might have to wait a minute or so for the disk to decrypt and boot.

To exit qemu : press `Ctrl + a`, then `x` and then `[Enter]`

Make it your own:  add your user, ssh key, other program that you might need. Don't forget your encryption password! The aleph team can't help you if you lose it.

### 6. Uploading the disk image on IPFS

Upload the disk file you just created to ipfs. Either using an ipfs interface or via `curl`:

```shell
curl -L -X POST -F file=@destination-image.img "http://ipfs-2.aleph.im/api/v0/add"
```

### 7. Register the disk image on Aleph.im

Pin the ipfs file on aleph.im via:

```
aleph file pin <ipfs hash>
```

### 8. Check that it is present 

Finally, get its ItemHash that is to be passed at the rootfs item hash:

```shell
aleph file list
```

---

Next: [Creating the confidential instance](./instance.md)