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

## Cannot SSH inside the VM

1. **Validate IPv6 Connectivity**  
   Ensure that IPv6 is functioning correctly on your local network. You can test this by
   visiting [https://test-ipv6.com/](https://test-ipv6.com/).

2. **Retrieve the VM's IP Address**  
   Use the following command to retrieve the VM's IP address:
   ```bash
   aleph instance list
   ```

3. **Try Different User Logins**  
   Depending on your distribution, the default user login may differ:
   - For Debian-based distributions, the default user is `root`.
   - For Ubuntu, the default user is `ubuntu`.

4. **Check VM Logs**  
   To investigate further, check the logs with:
   ```bash
   aleph instance logs <vm_hash>
   ```


## What to Do If You Entered the Wrong Decryption Password

If you mistakenly entered the wrong decryption secret while starting the VM, you will need to reboot it.

To reboot, run the following command:

```bash
aleph instance restart <vm_hash>
```

Then continue the process again from `aleph instance confidential-start`.


## Error: "Bad Measurement"

If the VM fails to start and the logs display the following error:

```shell
qemu-system-x86_64: sev_launch_start: LAUNCH_START ret=1 fw_error=11 'Bad measurement'
qemu-system-x86_64: sev_kvm_init: failed to create encryption context
qemu-system-x86_64: failed to initialize kvm: Operation not permitted
```

### Probable Causes

1. **Policy Mismatch**  
   The policy requested by the client does not match the start packet sent by the client. This is unlikely if the VM was
   started using the Aleph client unless the default policy was explicitly modified.

2. **Platform Certificate Issues**  
   The CRN's platform certificate may not match the start packet sent by the client due to one of the following reasons:
   - A session generated for one CRN was reused for another CRN.
   - The CRN platform certificate was rotated after the client generated the session certificate.
   - The CRN platform certificate was rotated, but the old one is still being returned by the CRN API endpoint. (If
     other confidential VMs can start, this is likely not the issue.)

### Resolution Steps

1. **On the Client Side:**  
   Regenerate the session certificate by running:
   ```bash
   aleph instance confidential-init-session
   ```  
   When prompted to remove existing certificates, answer "yes." Afterward, continue the normal start process using:
   ```bash
   aleph instance confidential-start
   ```

2. **If the Error Persists:**
   - **On the CRN Node Side:**  
     Verify if the cached platform certificate at `<CONFIDENTIAL_DIRECTORY>/certs_export.cert` matches the output of:
     ```bash
     /opt/sevctl export
     ```  
     If they do not match, delete the cached certificate file and instruct the client to restart the session process
     from scratch.

