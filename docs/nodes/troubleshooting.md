# Troubleshooting Guide
Setting up a [Core Channel Node](./core/index.md) or a [Compute Resource Node](./compute.md) can be a daunting task. This page is here to help you troubleshoot the most common issues.

## Core Resource Nodes

- Ensure to backup configuration files before making changes.
- Monitor the node after each troubleshooting step to check for resolution.
- Document each step taken for future reference or for support if needed.
- If you are unable to resolve the issue, please reach out to the Aleph.im team on [Telegram](https://t.me/alephim) for support.

### SQUASHFS Errors in Diagnostic VM
#### Issue Summary:
Users may encounter SQUASHFS errors indicating a failure to decompress data, suggesting possible corruption of the runtime diagnostic VM.

#### Symptoms:
Repeated SQUASHFS errors such as

- `Failed to read block`
- `Unable to read data cache entry`
- `zlib decompression failed, data probably corrupt`

related to a specific block.

#### Probable Cause:
The runtime of the new diagnostic VM appears to be improperly downloaded or corrupted.

#### Recommended Solution:

1. **Clear Cache**: Remove the cache of the problematic file using the diagnostic VM hash. This can be done by deleting the file located at /var/cache/aleph/runtime/RUNTIME_HASH.
2. **Restart Supervisor**: After deleting the problematic file, restart the supervisor system. This should trigger the re-download of the runtime file.
3. **Re-download**: Upon restart, the system should attempt to re-download the runtime, replacing the corrupted file.

#### Steps to Perform:

1. Navigate to the cache directory: cd /var/cache/aleph/runtime/.
2. Locate the file with the corresponding RUNTIME_HASH.
3. Remove the file: sudo rm -f <RUNTIME_HASH>.
4. Restart the supervisor: sudo systemctl restart supervisor (or the equivalent command for your system).

5. By following these steps, the error should be resolved as the system acquires a fresh, uncorrupted version of the runtime. If the problem persists, further investigation into network stability or hardware integrity may be necessary.

### Missing Diagnostic VM Data
#### Issue Summary:
The `diagnostic_vm_latency` data is missing for your CRN, even though virtualization is reportedly operational.

#### Symptoms:

- No `diagnostic_vm_latency` entry in the node's diagnostic data.
- Node appears functional, and virtualization is reportedly operational.
- Previous cache clearing solution was ineffective.

#### Troubleshooting Steps:

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
    See [SQUASHFS Errors in running diagnostic VM](#squashfs-errors-in-running-diagnostic-vm). 
4. **Contact Cloud Provider:**
    - If the issue persists, ask your Cloud Provider:
      - "I tried to enable IPv6 forwarding on my server. This makes my machine unreachable over IPv6. Why is that?"


### IPv6 Unreachable
#### Issue Summary:
When using IPv6 on a node, the network is unreachable.

#### Symptoms:

- `ping6` command fails to connect to an IPv6 address.
- The system returns the error "Network is unreachable."

#### Common Causes:

- Incorrect IPv6 configuration.
- Network interface not configured for IPv6.
- IPv6 connectivity issues with the network.

#### Troubleshooting Steps:
1. **Check IPv6 Configuration:**
    - Ensure that IPv6 is enabled on the network interface.
    - Verify that the IPv6 address is correctly assigned to the interface.
    - Confirm that the gateway for IPv6 is set up correctly.
2. **Review Netplan Configuration (for Ubuntu systems):**

    - Open the Netplan configuration file located typically at /etc/netplan/*.yaml.
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