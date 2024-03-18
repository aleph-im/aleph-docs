# Running Instances on the Local Environment

Aleph.im supports two popular and high-performance hypervisors for virtualization: Firecracker and Qemu. This guide outlines the steps to run instances on your local machine for development and testing purposes.

## Prerequisites

- **SSH Keys:** Ensure you have a valid SSH key pair set up. You'll need the public key to enable SSH access to the instances.

## Steps

1. **Configure Allocation Token and SSH Keys:**

    - Edit the `/etc/aleph/supervisor.env` file and add the following lines:

      ```bash
      # Encrypted allocation token hash in sha1 format
      ALEPH_VM_ALLOCATION_TOKEN_HASH=YOUR_ALLOCATION_TOKEN_HASH
 
      # List of authorized SSH public keys (replace "YOUR_SSH_PUBLIC_KEY" with your actual key)
      ALEPH_VM_DEVELOPER_SSH_KEYS=["YOUR_SSH_PUBLIC_KEY"]
      ```

        - **Important:** Replace `YOUR_ALLOCATION_TOKEN_HASH` with your actual encrypted allocation token and `YOUR_SSH_PUBLIC_KEY` with your public SSH key.


2. **Enable Developer SSH Keys (Optional):**

   By default, SSH access to instances is only enabled to the user that creates the VM for security reasons. To enable it for development, you have two options:

   **a) Modifying the Systemd Service File:**

    1. Locate the Aleph VM orchestrator service file, typically found at `/etc/systemd/system/aleph-vm-orchestrator.service`.
    2. Edit the file and add the `--developer-ssh-keys` argument to the `ExecStart` line. It should look something like this:

       ```
       ExecStart=python3 -m aleph.vm.orchestrator --print-settings --very-verbose --developer-ssh-keys
       ```

    3. Reload the systemd configuration and restart the service:

       ```bash
       sudo systemctl daemon-reload
       sudo systemctl restart aleph-vm-supervisor
       ```

   **b) Running the Orchestrator Manually:**

   You can simply append the `--developer-ssh-keys` argument when running the orchestrator manually:

     ```bash
     python3 -m aleph.vm.orchestrator --print-settings --very-verbose --developer-ssh-keys
     ```

3. **Launch an Instance:**

   Use the following `curl` command to launch an instance locally:

     ```bash
     curl --retry 5 --max-time 10 --fail -X POST -H "Content-Type: application/json" \
     -H "X-Auth-Signature: test" \
     -d '{"persistent_vms": [], "instances": ["INSTANCE_ID"]}' \
     "[http://ovh.staging.aleph.sh/control/allocations](http://ovh.staging.aleph.sh/control/allocations)"
     ```

    - Replace `INSTANCE_ID` with the actual ID of the instances you want to launch.

## Running a Qemu Instance

To run an instance using the Qemu hypervisor, follow these additional steps:

1. **Enable Qemu Support:**

   Edit the `/etc/aleph/supervisor.env` file and add the following line:

     ```bash
     ALEPH_VM_ENABLE_QEMU_SUPPORT=True
     ```

2. **Set Default Hypervisor (Optional):**

   If you primarily use Qemu, you can set it as the default hypervisor:

     ```bash
     ALEPH_VM_INSTANCE_DEFAULT_HYPERVISOR=qemu
     ```

3. **Launch a Qemu Instance:**

   The `curl` command remains almost the same, but ensure the instance you're launching has a Qemu runtime. Replace `QEMU_INSTANCE_ID` with the actual ID of the Qemu instance:

     ```bash
     curl --retry 5 --max-time 10 --fail -X POST -H "Content-Type: application/json" \
     -H "X-Auth-Signature: test" \
     -d '{"persistent_vms": [], "instances": ["QEMU_INSTANCE_ID"]}' \
     "[invalid URL removed]
