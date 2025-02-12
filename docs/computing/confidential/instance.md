# Confidential Instance Creation

This section outlines the process of starting a confidential instance on the Aleph Network.

If issues arise following these steps, consult the [Confidential VM troubleshooting](./troubleshooting.md) guide.

The **CLI Documentation** is also a precious source of information, see [CLI Reference](../../tools/aleph-client/usage.md), or use
`--help` for a quick overview of a specific command.

## Prerequisites

Before proceeding, ensure the following:

1. **aleph-client and sevctl**: The aleph-client and sev-ctl must be installed. Refer
   to [Requirements](./requirements.md)
   for instructions
2. **Upload your VM image**: Your encrypted VM image must be uploaded to the Aleph Network. Refer to
   the [Encrypted Virtual Machine Image](./encrypted-disk.md) guide for instructions.

## Step-by-Step Guide

### Method 1: Automatic Instance Creation

The CLI provides a streamlined command to automate the entire creation process:

```shell
aleph instance confidential
```

This command handles instance creation, secure channel setup, and VM initialization.

### Method 2: Manual Instance Creation

For more control, follow these steps:

#### 1. Create the Instance

Launch the instance configuration process:

```shell
aleph instance create --confidential
```

- **Payment**: Select a payment chain and payment method (hold, superfluid, nft).
- **Resources**: Specify CPU, RAM, disk size and rootfs (your VM image hash).
- **Deployment**: Choose a CRN (Compute Resource Node) for deployment.

**Important**: Record the CRN URL and VM hash for subsequent steps. Use `aleph instance list` if needed.

#### 2. Establish a Secure Communication Channel

Initialize a secure session with your VM:

```shell
aleph instance confidential-init-session <vm-hash>
```

- **Troubleshooting**: If this step fails, reboot the instance using:

  ```shell
  aleph instance reboot <vm-hash> <node-url>
  ```

  Then, retry establishing the session.

#### 3. Validate and Start the VM

Verify the VM's integrity and start it:

```shell
aleph instance confidential-start <vm-hash>
```

- **Troubleshooting**: On failure, reboot using the command above, then retry.

## Post-Creation Steps

Your VM is now ready to use.

### Retrieve VM Logs

Monitor your VM's activity:

```shell
aleph instance logs <vm-hash>
```

### Access Your VM via SSH

#### 1. **Find the Instance Details**

- **Via CLI**:

```shell
aleph instance list
```

- **Via API**: Access the compute node's API at `https://<node-url>/about/executions/list`.

#### 2. **Connect via SSH**:

Use the retrieved IP address to SSH into your VM:

```shell
ssh <user>@<ip> [-i <path-to-ssh-key>]
```

- **Default Users**:
    - Debian: `root`
    - Ubuntu: `ubuntu`