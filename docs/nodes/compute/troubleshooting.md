# Troubleshooting Guide

Setting up a [Compute Resource Node](index.md) can be a daunting task. This page is here to help you troubleshoot the most common issues.

- Ensure to backup configuration files before making changes.
- Monitor the node after each troubleshooting step to check for resolution.
- Document each step taken for future reference or for support if needed.
- If you are unable to resolve the issue, then please check out the latest issues on the [Discourse Forum](https://community.aleph.im/c/node-operators/7) for support.

## 1) 404: Invalid message reference

### Issue Summary

After setting up a CRN, users may encounter a `404: Invalid message reference` error when attempting to connect to the node's diagnostic page.

### Probable Cause

- SSL configuration may be incomplete or incorrect, despite successful SSL activation.
- The hostname might not be correctly configured in the aleph-vm settings.

### Troubleshooting Steps

1. **Recheck SSL Configuration:**

   - Confirm that SSL certificates are correctly installed and configured.
   - Review the SSL configuration in the web server (e.g., Caddy, Nginx) to ensure it's correctly pointing to the intended ports with the right certificate paths.

2. **Configure Hostname Correctly:**

    - Ensure the hostname is properly configured as per the [CRN installation guide](./installation/debian-12.md#2-installation).
    - Make sure the domain name in the supervisor.env file matches the domain used in your SSL configuration.

3. **Restart Services:**

   - After updating the hostname, restart the relevant services to apply the changes.
   - This may include restarting the Docker container and the web server service.

4. **Review Log Files:**

   - If the problem still persists, check the log files of both the Docker container and the web server for any specific error messages related to SSL or hostname configurations.

## 2) SQUASHFS Errors in Diagnostic VM

### Issue Summary

Users may encounter SQUASHFS errors indicating a failure to decompress data, suggesting possible corruption of the runtime diagnostic VM.

#### Symptoms

Repeated SQUASHFS errors in the logs such as

- `Failed to read block`
- `Unable to read data cache entry`
- `zlib decompression failed, data probably corrupt`

related to a specific block.

### Probable Cause

The runtime of the new diagnostic VM appears to be improperly downloaded or corrupted.

### Troubleshooting Steps

1. **Stop the Supervisor**: It is important to stop the VMs first when doing the operations below.

2. **Clear Cache**: Remove the cache of the problematic file using the diagnostic VM hash. This can be done by deleting the file located at `/var/cache/aleph/runtime/$RUNTIME_HASH`.

   - Navigate to the cache directory: `cd /var/cache/aleph/vm/runtime/`.
   - Locate the file with the corresponding `$RUNTIME_HASH`.
   - Remove the file:

   ```shell
   sudo rm -f $RUNTIME_HASH
   ```

3. **Restart Supervisor**: After deleting the problematic file, restart the supervisor system. This should trigger the re-download of the runtime file.

   - Restart the supervisor: `sudo systemctl restart supervisor` (or `aleph-vm-supervisor.service` when installing from source).

4. **Re-download**: Upon restart, the system will automatically attempt to re-download the runtime, replacing the corrupted file.

   - If the problem persists, further investigation into network stability or hardware integrity may be necessary.

## 3) Missing Diagnostic VM Metrics

### Issue Summary

The `diagnostic_vm_latency` metrics data is missing for your CRN, even though virtualization is reportedly operational.
Users can check the raw network metrics data for their node on the [Message Explorer](https://explorer.aleph.im/messages?showAdvancedFilters=1&channels=aleph-scoring&type=POST&page=1).
For more info on the data found there, see [Metrics](../reliability/metrics.md).

Two urls are used to check this marker:

- `/vm/67705389842a0a1b95eaa408b009741027964edc805997475e95c505d642edd8` (legacy runtime)
- `/vm/3fc0aa9569da840c43e7bd2033c3c580abb46b007527d6d20f2d4e98e867f7af` (current runtime)

Check that both work on your node, on an URL similar to

`https://my-compute-node.example/vm/3fc0aa9569da840c43e7bd2033c3c580abb46b007527d6d20f2d4e98e867f7af`

#### Symptoms

- No `diagnostic_vm_latency` entry in the node's diagnostic data.
- Node appears functional, and virtualization is reportedly operational.
- Previous cache clearing solution was ineffective.

### Troubleshooting Steps

1. **Upgrade Node Software:**

   - Ensure the node is running the latest CRN version.

2. **Disable IPv6 Forwarding:**

   - If upgrading does not resolve the issue, try disabling IPv6 forwarding:
     - Set `ALEPH_VM_IPV6_FORWARDING_ENABLED=False` in `/etc/aleph-vm/supervisor.env`.
     - Manually check if IPv6 forwarding is still active:
       ```shell
       cat /proc/sys/net/ipv6/conf/all/forwarding
       ```
       If the output is 1, disable it with:
       ```shell
       echo 0 > /proc/sys/net/ipv6/conf/all/forwarding
       ```

3. **Clear Cache:**

   - See [SQUASHFS Errors in running diagnostic VM](#2-squashfs-errors-in-diagnostic-vm).

4. **Contact Cloud Provider:**

   - If the issue persists, ask your Cloud Provider:
     "I tried to enable IPv6 forwarding on my server. This makes my machine unreachable over IPv6. Why is that?"

## 4) IPv6 Unreachable

### Issue Summary

When using IPv6 on a node, the network is unreachable.

#### Symptoms

- `ping6` command fails to connect to an IPv6 address.
- The system returns the error "Network is unreachable."

### Common Causes

- Incorrect IPv6 configuration.
- Network interface not configured for IPv6.
- IPv6 connectivity issues with the network.

### Troubleshooting Steps

1. **Check IPv6 Configuration:**

   - Ensure that IPv6 is enabled on the network interface.
   - Verify that the IPv6 address is correctly assigned to the interface.
   - Confirm that the gateway for IPv6 is set up correctly.

2. **Review Netplan Configuration (for Ubuntu systems):**

   - Open the Netplan configuration file located typically at /etc/netplan/\*.yaml.
   - Check for proper syntax and settings for IPv6, including address, gateway, and nameservers.
   - Example of a Netplan configuration for IPv6:

   ```yaml
   network:
     version: 2
     ethernets:
       eth0:
         dhcp4: no
         dhcp6: no
         addresses:
           - "2602:2940:0:1f::2/64"
         gateway6: "2602:2940:0:1f::1"
         nameservers:
           addresses: ["2001:4860:4860::8888", "2001:4860:4860::8844"]
   ```

   After making changes, apply them with `sudo netplan apply`.

3. **Check Network Interface:**

   - Use `ip -6 addr show` to check if the IPv6 address is assigned to the network interface.
   - Use `ip -6 route show` to verify the default route for IPv6.

4. **Test Network Connectivity:**

   - Use `ping6` to ping the local IPv6 gateway or known IPv6 addresses like Google's DNS `2001:4860:4860::8888` to test connectivity.

## 5) Persistent Storage Corruption

### Issue Summary

A Compute Resource Node exhibits issues with the `persistent_storage` feature.

#### Symptoms

- Errors in the `persistent_storage` field from the diagnostic on the index page of a CRN or on the `/status/check/fastapi` API endpoint.
- The endpoint `/state/increment` on the diagnostic VM returns an error 500.
- The field `diagnostic_vm_latency` is missing from the metrics.

### Probable Cause

The diagnostic VM tests the capability of the VM to persist data on the host. This is done by incrementing a counter in a JSON file, itself stored in a persistent volume.

When a diagnostic virtual machine happens to be stopped while writing data to this file, it is possible to end up with a corrupt file that, for example, only contains part of the expected JSON data and cannot be parsed.

### Troubleshooting Steps

1. **Identify Corrupted Volumes:**

   - Identify the identifier of the two diagnostic VMs from the variables `CHECK_FASTAPI_VM_ID` and `LEGACY_CHECK_FASTAPI_VM_ID` in the [configuration of aleph-vm](https://github.com/aleph-im/aleph-vm/blob/main/src/aleph/vm/conf.py#L292-L293).

2. **Stop the service:**

   - Stop the service to avoid any further corruption:
     ```shell
     sudo systemctl stop aleph-vm-supervisor.service
     ```

3. **Remove Corrupted Volumes:**

   - Remove the corrupted files. Here are the commands to remove the identified corrupted volumes:
     ```shell
     sudo rm /var/lib/aleph/vm/volumes/persistent/63faf8b5db1cf8d965e6a464a0cb8062af8e7df131729e48738342d956f29ace/increment-storage.ext4
     sudo rm /var/lib/aleph/vm/volumes/persistent/67705389842a0a1b95eaa408b009741027964edc805997475e95c505d642edd8/increment-storage.ext4
     ```

4. **Restart Services:**

   - After removing the corrupted volume files, restart the affected services to trigger the recreation of the necessary storage files:
     ```shell
     sudo systemctl restart aleph-vm-supervisor.service
     ```

5. **Verify System Stability:**

   - Check the dashboard of the index page of the CRN or open the storage test endpoint on both VMs opening:
     ```
     https://$YOUR_CRN_HOSTNAME/vm/$CHECK_FASTAPI_VM_ID/state/increment
     ```

## Found an issue?

If the documentation didn't help, you can [report an issue](https://github.com/aleph-im/support/issues).
