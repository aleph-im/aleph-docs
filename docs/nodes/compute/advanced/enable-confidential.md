# Enable Confidential computing

This guide outlines how to enable [Confidential Computing](../../../computing/confidential/index.md) on a CRN.

## Hardware requirement
To enable Confidential Computing, your system must be equipped with 4th Generation AMD EPYC™ Processors that support Secure Encrypted Virtualization (SEV).

The supported processors include the [9004 Series Processors and 8004 Series Processors](https://www.amd.com/en/products/processors/server/epyc/4th-generation-9004-and-8004-series.html#tabs-4380fde236-item-2130f0d757-tab).

Note that the [4004 Series Processors do not provide SEV](https://www.amd.com/en/products/processors/server/epyc/infinity-guard.html) and are therefore not supported.

> ℹ️ The 4th Generation requirement stems from security vulnerabilities discovered in SEV on Zen3 and earlier architectures.

## Additional Software Requirements
In addition to the standard software requirements, the following must be configured:

* **BIOS Configuration**: SEV support must be [enabled in the BIOS](https://www.amd.com/content/dam/amd/en/documents/epyc-technical-docs/tuning-guides/58207-using-sev-with-amd-epyc-processors.pdf) (refer to Section 2.1 of the document). (see Section 2.1).
* **Kernel and Platform Support**: The operating system kernel must support SEV. For example, Ubuntu 24.04 includes this support by default.
* **sevctl**: The [sevctl](https://github.com/virtee/sevctl) tool must be installed. This utility is included in the aleph-vm Debian package and is installed at `/opt/sevctl`.
* **QEMU**: QEMU must be installed on the system. `apt install cloud-image-utils qemu-utils qemu-system-x86`

To verify that your system supports AMD SEV, run the following command:  `/opt/sevctl ok`

A successful output should include:

```[ PASS ]   - Secure Encrypted Virtualization (SEV)```
For more details on enabling SEV and troubleshooting, refer to the official [AMD SEV documentation](https://www.amd.com/fr/developer/sev.html).


## Enabling the confidential computing feature

To enable SEV in the `aleph-vm` configuration, modify the supervisor.env file, by default located at `/etc/aleph-vm/supervisor.env`. Add or update the following lines:
```
ALEPH_VM_ENABLE_QEMU_SUPPORT=1
ALEPH_VM_ENABLE_CONFIDENTIAL_COMPUTING=1

```

After starting the server, verify that Confidential Computing is enabled by checking the configuration endpoint at:
`http://localhost:4020/status/config` 

The endpoint should return:
```json
ENABLE_CONFIDENTIAL_COMPUTING: true
```
