# Troubleshooting a confidential VM 

What to do in case your confidential VM is not working

## Fetch the logs
If the VM is supposed to be started but cannot be reached, try fetching the logs of your VM, use the commands:

```shell
aleph instance logs <vm_id>
```

If you don't know the id of your VM use `aleph instance list`

You should see in the logs, the disk unlocking , the boot logs and the system invite.

The last lines  should be something similar to this
```
cloud-init[502]: Cloud-init v. 24.1.3-0ubuntu1~22.04.5 finished at Thu, 05 Sep 2024 19:36:07 +0000. Datasource DataSourceNoCloud [seed=/dev/sr0][dsmode=net].  Up 23.63 seconds
[  OK  ] Finished Execute cloud user/final scripts.
[  OK  ] Reached target Cloud-init target.

Ubuntu 22.04.4 LTS dbnszzoulvoea7crseir75egj4xbm5zzzaaut2nbpknjadidp3ua ttyS0
```

## Attempt launching the VM locally

If the VM fail to start, try launching your VM disk image locally in QEMU, this will allow to check if the disk image has been
properly built.

```shell
sudo qemu-system-x86_64 \
  -enable-kvm \
  -m 2048 \
  -nic user,model=virtio \
  -nographic \
  -serial mon:stdio \
  -drive if=pflash,format=raw,unit=0,file=/usr/share/ovmf/OVMF.fd,readonly=on
  -drive format=raw,file=</path/to/your/image.img> \
```

> Note: Once you have entered your password you might have to wait a minute or so for the disk to decrypt and boot.

To exit qemu: press `Ctrl + a`, then `x` and then `[Enter]`
