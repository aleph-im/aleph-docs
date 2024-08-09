# Encrypted disk image

You must create a virtual machine disk image,  encrypted with a password of your choice.

Theses samples scripts create an encrypted VM image suitable be used for confidential computing.

They will create an encrypted partition, a boot partition and the necessary initramfs to decrypt the partition. The created image is designed to work in tandem with the custom OVMF found in `runtimes/ovmf` which can receive the decryption key in a secure channel via QMP and pass it to grub to decrypt the disk.  

You can customise your VM by modifying the `setup_debian_rootfs.sh` script and  adding your instructions at the end. This script is run "inside" the VM chroot. For examples: add your user, ssh key or install additional software. 

## 0. Requirements

Ensure you have the [requirements](./requirements.md) setup. 

## 1. Fetch a base image you can trust

In this example, we use Debian 12.

Your image need to have cloud-init installed in it for the network setup. It is recommended to start from the genericcloud image. Experiment with using the nocloud image then installing cloud-init have failed to work.

```shell
wget https://cloud.debian.org/images/cloud/bookworm/latest/debian-12-genericcloud-amd64.qcow2
```

## 2. Extract the root filesystem

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

Then, you can simply copy the root file system to any directory, take caution to preserve the proper permission like the setuid bit with the --archive option.

```shell
export ROOT_DIR=./extracted
mkdir ${ROOT_DIR}
sudo cp --archive /mnt/debian/* ${ROOT_DIR}
```

Clean up the mount
```shell
sudo guestunmount /mnt/debian
sudo rm -r /mnt/debian
```

## 3. Create the encrypted disk

Run the build_debian_image.sh that will create the image with the encrypted disk 
> This script will require sudo for certain commands

The password option is the *secret* password key, with which the disk will be encrypted, you will need to pass it to launch the VM.  

```shell
bash ./build_debian_image.sh  --rootfs-dir  $ROOT_DIR -o ~/destination-image.img --password your-password
```

> Tip: To debug the image creation, pass the `-x` option to bash in front of the script name

## 4. Test and customise your image

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

> Once you have entered your password you might have to wait a minute or so for the disk to decrypt and boot.

To exit qemu : press Ctrl a, x and then [Enter]

Make it your own:  add your user, ssh key, other program that you might need.
Don't forget your encryption password! The aleph team can't help you if you lose it

## 5. Upload the disk image on IPFS

2. Upload the disk file you just created to ipfs

```shell
curl -L -X POST -F file=@destination-image.img "http://ipfs-2.aleph.im/api/v0/add"
```

## 6. Register the disk image on aleph.im

3. Pin the ipfs file in aleph via
```
aleph file pin <ipfs hash>
```

4. Check that it is present 

... and get it's ItemHash that is to be passed at the rootfs item hash:
```shell
aleph file list
```
