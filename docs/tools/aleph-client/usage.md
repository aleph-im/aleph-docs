# Aleph CLI Documentation

**Usage**:

```console
$ aleph [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `about`: Display the informations of Aleph CLI
* `account`: Manage account
* `aggregate`: Manage aggregate messages on aleph.im
* `domain`: Manage custom Domain (dns) on aleph.im
* `file`: File uploading and pinning on IPFS and...
* `instance`: Manage instances (VMs) on aleph.im network
* `message`: Post, amend, watch and forget messages on...
* `node`: Get node info on aleph.im network
* `program`: Upload and update programs on aleph.im VM

## `aleph about`

Display the informations of Aleph CLI

**Usage**:

```console
$ aleph about [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `version`

### `aleph about version`

**Usage**:

```console
$ aleph about version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `aleph account`

Manage account

**Usage**:

```console
$ aleph account [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `address`: Display your public address(es).
* `balance`: Display your ALEPH balance.
* `chain`: Display the currently active chain.
* `config`: Configure current private key file and...
* `create`: Create or import a private key.
* `export-private-key`: Display your private key.
* `list`: Display available private keys, along with...
* `path`: Display the directory path where your...
* `show`: Display current configuration.
* `sign-bytes`: Sign a message using your private key.

### `aleph account address`

Display your public address(es).

**Usage**:

```console
$ aleph account address [OPTIONS]
```

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--help`: Show this message and exit.

### `aleph account balance`

Display your ALEPH balance.

**Usage**:

```console
$ aleph account balance [OPTIONS]
```

**Options**:

* `--address TEXT`: Address
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain for the address
* `--help`: Show this message and exit.

### `aleph account chain`

Display the currently active chain.

**Usage**:

```console
$ aleph account chain [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `aleph account config`

Configure current private key file and active chain (default selection)

**Usage**:

```console
$ aleph account config [OPTIONS]
```

**Options**:

* `--private-key-file PATH`: New path to the private key file
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: New active chain
* `--help`: Show this message and exit.

### `aleph account create`

Create or import a private key.

**Usage**:

```console
$ aleph account create [OPTIONS]
```

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain of origin of your private key (ensuring correct parsing)
* `--replace / --no-replace`: Overwrites private key file if it already exists  [default: no-replace]
* `--active / --no-active`: Loads the new private key after creation  [default: active]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph account export-private-key`

Display your private key.

**Usage**:

```console
$ aleph account export-private-key [OPTIONS]
```

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file
* `--help`: Show this message and exit.

### `aleph account list`

Display available private keys, along with currenlty active chain and account (from config file).

**Usage**:

```console
$ aleph account list [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `aleph account path`

Display the directory path where your private keys, config file, and other settings are stored.

**Usage**:

```console
$ aleph account path [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `aleph account show`

Display current configuration.

**Usage**:

```console
$ aleph account show [OPTIONS]
```

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--help`: Show this message and exit.

### `aleph account sign-bytes`

Sign a message using your private key.

**Usage**:

```console
$ aleph account sign-bytes [OPTIONS]
```

**Options**:

* `--message TEXT`: Message to sign
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain for the address
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

## `aleph aggregate`

Manage aggregate messages on aleph.im

**Usage**:

```console
$ aleph aggregate [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `forget`: Forget all the messages composing an...
* `get`: Fetch an aggregate by key and content.
* `post`: Create or Update aggregate

### `aleph aggregate forget`

Forget all the messages composing an aggregate.

**Usage**:

```console
$ aleph aggregate forget [OPTIONS] KEY
```

**Arguments**:

* `KEY`: Aggregate item hash to be removed.  [required]

**Options**:

* `--reason TEXT`: A description of why the messages are being forgotten
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  [default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph aggregate get`

Fetch an aggregate by key and content.

**Usage**:

```console
$ aleph aggregate get [OPTIONS] KEY
```

**Arguments**:

* `KEY`: Aggregate key to be fetched.  [required]

**Options**:

* `--address TEXT`: Address
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph aggregate post`

Create or Update aggregate

**Usage**:

```console
$ aleph aggregate post [OPTIONS] KEY CONTENT
```

**Arguments**:

* `KEY`: Aggregate key to be created.  [required]
* `CONTENT`: Aggregate content (ex : {'c': 3, 'd': 4})  [required]

**Options**:

* `--address TEXT`: address
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  [default: ALEPH-CLOUDSOLUTIONS]
* `--inline / --no-inline`: inline  [default: no-inline]
* `--sync / --no-sync`: Sync response  [default: no-sync]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

## `aleph domain`

Manage custom Domain (dns) on aleph.im

**Usage**:

```console
$ aleph domain [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `add`: Add and link a Custom Domain.
* `attach`: Attach resource to a Custom Domain.
* `detach`: Unlink Custom Domain.
* `info`: Show Custom Domain Details.

### `aleph domain add`

Add and link a Custom Domain.

**Usage**:

```console
$ aleph domain add [OPTIONS] FQDN
```

**Arguments**:

* `FQDN`: Domain name. ex: aleph.im  [required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--target [ipfs|program|instance]`: IPFS|PROGRAM|INSTANCE
* `--item-hash TEXT`: Item hash
* `--owner TEXT`: Owner address, default current account
* `--ask / --no-ask`: Prompt user for confirmation  [default: ask]
* `--help`: Show this message and exit.

### `aleph domain attach`

Attach resource to a Custom Domain.

**Usage**:

```console
$ aleph domain attach [OPTIONS] FQDN
```

**Arguments**:

* `FQDN`: Domain name. ex: aleph.im  [required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--item-hash TEXT`: Item hash
* `--catch-all-path TEXT`: Choose a relative path to catch all unmatched route or a 404 error
* `--ask / --no-ask`: Prompt user for confirmation  [default: ask]
* `--help`: Show this message and exit.

### `aleph domain detach`

Unlink Custom Domain.

**Usage**:

```console
$ aleph domain detach [OPTIONS] FQDN
```

**Arguments**:

* `FQDN`: Domain name. ex: aleph.im  [required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--ask / --no-ask`: Prompt user for confirmation  [default: ask]
* `--help`: Show this message and exit.

### `aleph domain info`

Show Custom Domain Details.

**Usage**:

```console
$ aleph domain info [OPTIONS] FQDN
```

**Arguments**:

* `FQDN`: Domain name. ex: aleph.im  [required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--help`: Show this message and exit.

## `aleph file`

File uploading and pinning on IPFS and aleph.im

**Usage**:

```console
$ aleph file [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `download`: Download a file on aleph.im.
* `forget`: forget a file and his message on aleph.im.
* `list`: List all files for a given address
* `pin`: Persist a file from IPFS on aleph.im.
* `upload`: Upload and store a file on aleph.im.

### `aleph file download`

Download a file on aleph.im.

**Usage**:

```console
$ aleph file download [OPTIONS] HASH
```

**Arguments**:

* `HASH`: hash to download from aleph.  [required]

**Options**:

* `--use-ipfs / --no-use-ipfs`: Download using IPFS instead of storage  [default: no-use-ipfs]
* `--output-path PATH`: Output directory path  [default: .]
* `--file-name TEXT`: Output file name (without extension)
* `--file-extension TEXT`: Output file extension
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph file forget`

forget a file and his message on aleph.im.

**Usage**:

```console
$ aleph file forget [OPTIONS] ITEM_HASH [REASON]
```

**Arguments**:

* `ITEM_HASH`: Hash to forget  [required]
* `[REASON]`: reason to forget  [default: User deletion]

**Options**:

* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  [default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph file list`

List all files for a given address

**Usage**:

```console
$ aleph file list [OPTIONS]
```

**Options**:

* `--address TEXT`: Address
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--pagination INTEGER`: Maximum number of files to return.  [default: 100]
* `--page INTEGER`: Offset in pages.  [default: 1]
* `--sort-order INTEGER`: Order in which files should be listed: -1 means most recent messages first, 1 means older messages first.  [default: -1]
* `--json / --no-json`: Print as json instead of rich table  [default: no-json]
* `--help`: Show this message and exit.

### `aleph file pin`

Persist a file from IPFS on aleph.im.

**Usage**:

```console
$ aleph file pin [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: IPFS hash to pin on aleph.im  [required]

**Options**:

* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  [default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--ref TEXT`: Checkout https://aleph-im.gitbook.io/aleph-js/api-resources-reference/posts
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph file upload`

Upload and store a file on aleph.im.

**Usage**:

```console
$ aleph file upload [OPTIONS] PATH
```

**Arguments**:

* `PATH`: Path of the file to upload  [required]

**Options**:

* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  [default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--ref TEXT`: Checkout https://aleph-im.gitbook.io/aleph-js/api-resources-reference/posts
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

## `aleph instance`

Manage instances (VMs) on aleph.im network

**Usage**:

```console
$ aleph instance [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `allocate`: Notify a CRN to start an instance (for...
* `confidential`: Create (optional), start and unlock a...
* `confidential-init-session`: Initialize a confidential communication...
* `confidential-start`: Validate the authenticity of the VM and...
* `create`: Create and register a new instance on...
* `delete`: Delete an instance, unallocating all...
* `erase`: Erase an instance stored or running on a CRN
* `expire`: Expire an instance
* `list`: List all instances associated to an account
* `logs`: Retrieve the logs of an instance
* `reboot`: Reboot an instance
* `stop`: Stop an instance

### `aleph instance allocate`

Notify a CRN to start an instance (for Pay-As-You-Go and confidential instances only)

**Usage**:

```console
$ aleph instance allocate [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to allocate  [required]

**Options**:

* `--domain TEXT`: CRN domain on which the VM will be allocated
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain you are using to pay for your instance
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance confidential`

Create (optional), start and unlock a confidential VM (all-in-one command)

This command combines the following commands:

    - create (unless vm_id is passed)

    - allocate

    - confidential-init-session

    - confidential-start

**Usage**:

```console
$ aleph instance confidential [OPTIONS] [VM_ID]
```

**Arguments**:

* `[VM_ID]`: Item hash of your VM. If provided, skip the instance creation, else create a new one

**Options**:

* `--crn-url TEXT`: URL of the CRN to deploy to (only applicable for confidential and/or Pay-As-You-Go instances)
* `--crn-hash TEXT`: Hash of the CRN to deploy to (only applicable for confidential and/or Pay-As-You-Go instances)
* `--policy INTEGER`: [default: 1]
* `--confidential-firmware TEXT`: Hash to UEFI Firmware to launch confidential instance  [default: ba5bb13f3abca960b101a759be162b229e2b7e93ecad9d1307e54de887f177ff]
* `--firmware-hash TEXT`: Hash of the UEFI Firmware content, to validate measure (ignored if path is provided)  [default: 89b76b0e64fe9015084fbffdf8ac98185bafc688bfe7a0b398585c392d03c7ee]
* `--firmware-file TEXT`: Your private key. Cannot be used with --private-key-file
* `--keep-session / --no-keep-session`: Keeping the already initiated session
* `--vm-secret TEXT`: Secret password to start the VM
* `--payment-type [hold|superfluid|nft]`: Payment method, either holding tokens, NFTs, or Pay-As-You-Go via token streaming
* `--payment-chain [ETH|AVAX|BASE|SOL]`: Chain you want to use to pay for your instance
* `--name TEXT`: Name of your new instance
* `--rootfs TEXT`: Hash of the rootfs to use for your instance. Defaults to Ubuntu 22. You can also create your own rootfs and pin it
* `--rootfs-size INTEGER`: Size of the rootfs to use for your instance. If not set, content.size of the --rootfs store message will be used
* `--vcpus INTEGER`: Number of virtual CPUs to allocate
* `--memory INTEGER`: Maximum memory (RAM) allocation on VM in MiB
* `--timeout-seconds FLOAT`: If vm is not called after [timeout_seconds] it will shutdown  [default: 30.0]
* `--ssh-pubkey-file PATH`: Path to a public ssh key to be added to the instance  [default: /home/olivier/.ssh/id_rsa.pub]
* `--skip-volume / --no-skip-volume`: Skip prompt to attach more volumes  [default: no-skip-volume]
* `--persistent-volume TEXT`: Persistent volumes are allocated on the host machine and are not deleted when the VM is stopped.

Requires at least a "mount" and "size_mib". For more info, see the docs: https://docs.aleph.im/computing/volumes/persistent/

Example: --persistent_volume persistence=host,size_mib=100,mount=/opt/data
* `--ephemeral-volume TEXT`: Ephemeral volumes are allocated on the host machine when the VM is started and deleted when the VM is stopped.

Example: --ephemeral-volume size_mib=100,mount=/tmp/data
* `--immutable-volume TEXT`: Immutable volumes are pinned on the network and can be used by multiple VMs at the same time. They are read-only and useful for setting up libraries or other dependencies.

Requires at least a "ref" (message hash) and "mount" path. "use_latest" is True by default, to use the latest version of the volume, if it has been amended. See the docs for more info: https://docs.aleph.im/computing/volumes/immutable/

Example: --immutable-volume ref=25a393222692c2f73489dc6710ae87605a96742ceef7b91de4d7ec34bb688d94,mount=/lib/python3.8/site-packages
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  [default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance confidential-init-session`

Initialize a confidential communication session with the VM

**Usage**:

```console
$ aleph instance confidential-init-session [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to initialize the session for  [required]

**Options**:

* `--domain TEXT`: CRN domain on which the session will be initialized
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain you are using to pay for your instance
* `--policy INTEGER`: [default: 1]
* `--keep-session / --no-keep-session`: Keeping the already initiated session
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance confidential-start`

Validate the authenticity of the VM and start it

**Usage**:

```console
$ aleph instance confidential-start [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to start  [required]

**Options**:

* `--domain TEXT`: CRN domain on which the VM will be started
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain you are using to pay for your instance
* `--firmware-hash TEXT`: Hash of the UEFI Firmware content, to validate measure (ignored if path is provided)  [default: 89b76b0e64fe9015084fbffdf8ac98185bafc688bfe7a0b398585c392d03c7ee]
* `--firmware-file TEXT`: Your private key. Cannot be used with --private-key-file
* `--vm-secret TEXT`: Secret password to start the VM
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance create`

Create and register a new instance on aleph.im

**Usage**:

```console
$ aleph instance create [OPTIONS]
```

**Options**:

* `--payment-type [hold|superfluid|nft]`: Payment method, either holding tokens, NFTs, or Pay-As-You-Go via token streaming
* `--payment-chain [ETH|AVAX|BASE|SOL]`: Chain you want to use to pay for your instance
* `--hypervisor [qemu|firecracker]`: Hypervisor to use to launch your instance. Defaults to QEMU
* `--name TEXT`: Name of your new instance
* `--rootfs TEXT`: Hash of the rootfs to use for your instance. Defaults to Ubuntu 22. You can also create your own rootfs and pin it
* `--rootfs-size INTEGER`: Size of the rootfs to use for your instance. If not set, content.size of the --rootfs store message will be used
* `--vcpus INTEGER`: Number of virtual CPUs to allocate
* `--memory INTEGER`: Maximum memory (RAM) allocation on VM in MiB
* `--timeout-seconds FLOAT`: If vm is not called after [timeout_seconds] it will shutdown  [default: 30.0]
* `--ssh-pubkey-file PATH`: Path to a public ssh key to be added to the instance  [default: /home/olivier/.ssh/id_rsa.pub]
* `--crn-hash TEXT`: Hash of the CRN to deploy to (only applicable for confidential and/or Pay-As-You-Go instances)
* `--crn-url TEXT`: URL of the CRN to deploy to (only applicable for confidential and/or Pay-As-You-Go instances)
* `--confidential / --no-confidential`: Launch a confidential instance (requires creating an encrypted volume)  [default: no-confidential]
* `--confidential-firmware TEXT`: Hash to UEFI Firmware to launch confidential instance  [default: ba5bb13f3abca960b101a759be162b229e2b7e93ecad9d1307e54de887f177ff]
* `--skip-volume / --no-skip-volume`: Skip prompt to attach more volumes  [default: no-skip-volume]
* `--persistent-volume TEXT`: Persistent volumes are allocated on the host machine and are not deleted when the VM is stopped.

Requires at least a "mount" and "size_mib". For more info, see the docs: https://docs.aleph.im/computing/volumes/persistent/

Example: --persistent_volume persistence=host,size_mib=100,mount=/opt/data
* `--ephemeral-volume TEXT`: Ephemeral volumes are allocated on the host machine when the VM is started and deleted when the VM is stopped.

Example: --ephemeral-volume size_mib=100,mount=/tmp/data
* `--immutable-volume TEXT`: Immutable volumes are pinned on the network and can be used by multiple VMs at the same time. They are read-only and useful for setting up libraries or other dependencies.

Requires at least a "ref" (message hash) and "mount" path. "use_latest" is True by default, to use the latest version of the volume, if it has been amended. See the docs for more info: https://docs.aleph.im/computing/volumes/immutable/

Example: --immutable-volume ref=25a393222692c2f73489dc6710ae87605a96742ceef7b91de4d7ec34bb688d94,mount=/lib/python3.8/site-packages
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  [default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--print-messages / --no-print-messages`: [default: no-print-messages]
* `--verbose / --no-verbose`: [default: verbose]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance delete`

Delete an instance, unallocating all resources associated with it. Associated VM will be stopped and erased. Immutable volumes will not be deleted.

**Usage**:

```console
$ aleph instance delete [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Instance item hash to forget  [required]

**Options**:

* `--reason TEXT`: Reason for deleting the instance  [default: User deletion]
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain for the address
* `--crn-url TEXT`: Domain of the CRN where an associated VM is running. It ensures your VM will be stopped and erased on the CRN before the instance message is actually deleted
* `--private-key TEXT`
* `--private-key-file PATH`: [default: ~/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: [default: no-print-message]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance erase`

Erase an instance stored or running on a CRN

**Usage**:

```console
$ aleph instance erase [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to erase  [required]

**Options**:

* `--domain TEXT`: CRN domain on which the VM is stored or running
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain you are using to pay for your instance
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--silent / --no-silent`: [default: no-silent]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance expire`

Expire an instance

**Usage**:

```console
$ aleph instance expire [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to expire  [required]

**Options**:

* `--domain TEXT`: CRN domain on which the VM is running
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain you are using to pay for your instance
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance list`

List all instances associated to an account

**Usage**:

```console
$ aleph instance list [OPTIONS]
```

**Options**:

* `--address TEXT`: Owner address of the instance
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain for the address
* `--json / --no-json`: Print as json instead of rich table  [default: no-json]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance logs`

Retrieve the logs of an instance

**Usage**:

```console
$ aleph instance logs [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to retrieve the logs from  [required]

**Options**:

* `--domain TEXT`: CRN domain on which the VM is running
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain you are using to pay for your instance
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance reboot`

Reboot an instance

**Usage**:

```console
$ aleph instance reboot [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to reboot  [required]

**Options**:

* `--domain TEXT`: CRN domain on which the VM is running
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain you are using to pay for your instance
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance stop`

Stop an instance

**Usage**:

```console
$ aleph instance stop [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to stop  [required]

**Options**:

* `--domain TEXT`: CRN domain on which the VM is running
* `--chain [AVAX|BASE|BSC|CSDK|DOT|ETH|NEO|NULS|NULS2|SOL|TEZOS]`: Chain you are using to pay for your instance
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

## `aleph message`

Post, amend, watch and forget messages on aleph.im

**Usage**:

```console
$ aleph message [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `amend`: Amend an existing aleph.im message.
* `find`
* `forget`: Forget an existing aleph.im message.
* `get`
* `post`: Post a message on aleph.im.
* `sign`: Sign an aleph message with a private key.
* `watch`: Watch a hash for amends and print amend...

### `aleph message amend`

Amend an existing aleph.im message.

**Usage**:

```console
$ aleph message amend [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Hash reference of the message to amend  [required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph message find`

**Usage**:

```console
$ aleph message find [OPTIONS]
```

**Options**:

* `--pagination INTEGER`: [default: 200]
* `--page INTEGER`: [default: 1]
* `--message-types TEXT`
* `--content-types TEXT`
* `--content-keys TEXT`
* `--refs TEXT`
* `--addresses TEXT`
* `--tags TEXT`
* `--hashes TEXT`
* `--channels TEXT`
* `--chains TEXT`
* `--start-date TEXT`
* `--end-date TEXT`
* `--ignore-invalid-messages / --no-ignore-invalid-messages`: [default: ignore-invalid-messages]
* `--help`: Show this message and exit.

### `aleph message forget`

Forget an existing aleph.im message.

**Usage**:

```console
$ aleph message forget [OPTIONS] HASHES
```

**Arguments**:

* `HASHES`: Comma separated list of hash references of messages to forget  [required]

**Options**:

* `--reason TEXT`: A description of why the messages are being forgotten.
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  [default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph message get`

**Usage**:

```console
$ aleph message get [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Item hash of the message  [required]

**Options**:

* `--help`: Show this message and exit.

### `aleph message post`

Post a message on aleph.im.

**Usage**:

```console
$ aleph message post [OPTIONS]
```

**Options**:

* `--path PATH`: Path to the content you want to post. If omitted, you can input your content directly
* `--type TEXT`: Text representing the message object type  [default: test]
* `--ref TEXT`: Checkout https://aleph-im.gitbook.io/aleph-js/api-resources-reference/posts
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  [default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph message sign`

Sign an aleph message with a private key. If no --message is provided, the message will be read from stdin.

**Usage**:

```console
$ aleph message sign [OPTIONS]
```

**Options**:

* `--message TEXT`: Message to sign
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph message watch`

Watch a hash for amends and print amend hashes

**Usage**:

```console
$ aleph message watch [OPTIONS] REF
```

**Arguments**:

* `REF`: Hash reference of the message to watch  [required]

**Options**:

* `--indent INTEGER`: Number of indents to use
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

## `aleph node`

Get node info on aleph.im network

**Usage**:

```console
$ aleph node [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `compute`: Get all compute node on aleph network
* `core`: Get all core node on aleph

### `aleph node compute`

Get all compute node on aleph network

**Usage**:

```console
$ aleph node compute [OPTIONS]
```

**Options**:

* `--json / --no-json`: Print as json instead of rich table  [default: no-json]
* `--active / --no-active`: Only show active nodes  [default: no-active]
* `--address TEXT`: Owner address to filter by
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph node core`

Get all core node on aleph

**Usage**:

```console
$ aleph node core [OPTIONS]
```

**Options**:

* `--json / --no-json`: Print as json instead of rich table  [default: no-json]
* `--active / --no-active`: Only show active nodes  [default: no-active]
* `--address TEXT`: Owner address to filter by
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

## `aleph program`

Upload and update programs on aleph.im VM

**Usage**:

```console
$ aleph program [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `unpersist`: Stop a persistent virtual machine by...
* `update`: Update the code of an existing program
* `upload`: Register a program to run on aleph.im.

### `aleph program unpersist`

Stop a persistent virtual machine by making it non-persistent

**Usage**:

```console
$ aleph program unpersist [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Item hash to unpersist  [required]

**Options**:

* `--private-key TEXT`
* `--private-key-file PATH`: [default: ~/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph program update`

Update the code of an existing program

**Usage**:

```console
$ aleph program update [OPTIONS] ITEM_HASH PATH
```

**Arguments**:

* `ITEM_HASH`: Item hash to update  [required]
* `PATH`: Source path to upload  [required]

**Options**:

* `--private-key TEXT`
* `--private-key-file PATH`: [default: ~/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: [default: print-message]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aleph program upload`

Register a program to run on aleph.im. For more information, see https://docs.aleph.im/computing/

**Usage**:

```console
$ aleph program upload [OPTIONS] PATH ENTRYPOINT
```

**Arguments**:

* `PATH`: Path to your source code  [required]
* `ENTRYPOINT`: Your program entrypoint  [required]

**Options**:

* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  [default: ALEPH-CLOUDSOLUTIONS]
* `--memory INTEGER`: Maximum memory allocation on vm in MiB  [default: 256]
* `--vcpus INTEGER`: Number of virtual cpus to allocate.  [default: 1]
* `--timeout-seconds FLOAT`: If vm is not called after [timeout_seconds] it will shutdown  [default: 30.0]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: ~/.aleph-im/private-keys/ethereum.key]
* `--print-messages / --no-print-messages`: [default: no-print-messages]
* `--print-code-message / --no-print-code-message`: [default: no-print-code-message]
* `--print-program-message / --no-print-program-message`: [default: no-print-program-message]
* `--runtime TEXT`: Hash of the runtime to use for your program. Defaults to aleph debian with Python3.8 and node. You can also create your own runtime and pin it
* `--beta / --no-beta`: If true, you will be prompted to add message subscriptions to your program  [default: no-beta]
* `--debug / --no-debug`: [default: no-debug]
* `--persistent / --no-persistent`: [default: no-persistent]
* `--persistent-volume TEXT`: Persistent volumes are allocated on the host machine and are not deleted when the VM is stopped.

Requires at least a "mount" and "size_mib". For more info, see the docs: https://docs.aleph.im/computing/volumes/persistent/

Example: --persistent_volume persistence=host,size_mib=100,mount=/opt/data
* `--ephemeral-volume TEXT`: Ephemeral volumes are allocated on the host machine when the VM is started and deleted when the VM is stopped.

Example: --ephemeral-volume size_mib=100,mount=/tmp/data
* `--immutable-volume TEXT`: Immutable volumes are pinned on the network and can be used by multiple VMs at the same time. They are read-only and useful for setting up libraries or other dependencies.

Requires at least a "ref" (message hash) and "mount" path. "use_latest" is True by default, to use the latest version of the volume, if it has been amended. See the docs for more info: https://docs.aleph.im/computing/volumes/immutable/

Example: --immutable-volume ref=25a393222692c2f73489dc6710ae87605a96742ceef7b91de4d7ec34bb688d94,mount=/lib/python3.8/site-packages
* `--help`: Show this message and exit.
