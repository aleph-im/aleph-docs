# Aleph CLI

**Usage**:

```console
$ aleph aleph [OPTIONS] COMMAND [ARGS]...
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

## `about`

Display the informations of Aleph CLI

**Usage**:

```console
$ aleph about [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `version`

### `about version`

**Usage**:

```console
$ aleph about version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `account`

Manage account

**Usage**:

```console
$ aleph account [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `address`: Display your public address.
* `balance`
* `create`: Create or import a private key.
* `export-private-key`: Display your private key.
* `path`
* `sign-bytes`: Sign a message using your private key.

### `account address`

Display your public address.

**Usage**:

```console
$ aleph account address [OPTIONS]
```

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--help`: Show this message and exit.

### `account balance`

**Usage**:

```console
$ aleph account balance [OPTIONS]
```

**Options**:

* `--address TEXT`: Address
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--help`: Show this message and exit.

### `account create`

Create or import a private key.

**Usage**:

```console
$ aleph account create [OPTIONS]
```

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file
* `--replace / --no-replace`: [default: no-replace]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `account export-private-key`

Display your private key.

**Usage**:

```console
$ aleph account export-private-key [OPTIONS]
```

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--help`: Show this message and exit.

### `account path`

**Usage**:

```console
$ aleph account path [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

### `account sign-bytes`

Sign a message using your private key.

**Usage**:

```console
$ aleph account sign-bytes [OPTIONS]
```

**Options**:

* `--message TEXT`: Message to sign
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

## `aggregate`

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

### `aggregate forget`

Forget all the messages composing an aggregate.

**Usage**:

```console
$ aleph aggregate forget [OPTIONS] KEY
```

**Arguments**:

* `KEY`: Aggregate item hash to be removed.  [required]

**Options**:

* `--reason TEXT`: A description of why the messages are being forgotten
* `--channel TEXT`: Aleph.im network channel where the message is located
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aggregate get`

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
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `aggregate post`

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
* `--channel TEXT`: Aleph.im network channel where the message is located
* `--inline / --no-inline`: inline  [default: no-inline]
* `--sync / --no-sync`: Sync response  [default: no-sync]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

## `domain`

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

### `domain add`

Add and link a Custom Domain.

**Usage**:

```console
$ aleph domain add [OPTIONS] FQDN
```

**Arguments**:

* `FQDN`: Domain name. ex: aleph.im  [required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--target [ipfs|program|instance]`: IPFS|PROGRAM|INSTANCE
* `--item-hash TEXT`: Item hash
* `--owner TEXT`: Owner address, default current account
* `--ask / --no-ask`: Prompt user for confirmation  [default: ask]
* `--help`: Show this message and exit.

### `domain attach`

Attach resource to a Custom Domain.

**Usage**:

```console
$ aleph domain attach [OPTIONS] FQDN
```

**Arguments**:

* `FQDN`: Domain name. ex: aleph.im  [required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--item-hash TEXT`: Item hash
* `--ask / --no-ask`: Prompt user for confirmation  [default: ask]
* `--help`: Show this message and exit.

### `domain detach`

Unlink Custom Domain.

**Usage**:

```console
$ aleph domain detach [OPTIONS] FQDN
```

**Arguments**:

* `FQDN`: Domain name. ex: aleph.im  [required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--ask / --no-ask`: Prompt user for confirmation  [default: ask]
* `--help`: Show this message and exit.

### `domain info`

Show Custom Domain Details.

**Usage**:

```console
$ aleph domain info [OPTIONS] FQDN
```

**Arguments**:

* `FQDN`: Domain name. ex: aleph.im  [required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--help`: Show this message and exit.

## `file`

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

### `file download`

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

### `file forget`

forget a file and his message on aleph.im.

**Usage**:

```console
$ aleph file forget [OPTIONS] ITEM_HASH REASON
```

**Arguments**:

* `ITEM_HASH`: Hash to forget  [required]
* `REASON`: reason to forget  [required]

**Options**:

* `--channel TEXT`: channel
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `file list`

List all files for a given address

**Usage**:

```console
$ aleph file list [OPTIONS]
```

**Options**:

* `--address TEXT`: Address
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--pagination INTEGER`: Maximum number of files to return.  [default: 100]
* `--page INTEGER`: Offset in pages.  [default: 1]
* `--sort-order INTEGER`: Order in which files should be listed: -1 means most recent messages first, 1 means older messages first.  [default: -1]
* `--json / --no-json`: Print as json instead of rich table  [default: no-json]
* `--help`: Show this message and exit.

### `file pin`

Persist a file from IPFS on aleph.im.

**Usage**:

```console
$ aleph file pin [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: IPFS hash to pin on aleph.im  [required]

**Options**:

* `--channel TEXT`: Aleph.im network channel where the message is located
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--ref TEXT`: Checkout https://aleph-im.gitbook.io/aleph-js/api-resources-reference/posts
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `file upload`

Upload and store a file on aleph.im.

**Usage**:

```console
$ aleph file upload [OPTIONS] PATH
```

**Arguments**:

* `PATH`: Path of the file to upload  [required]

**Options**:

* `--channel TEXT`: Aleph.im network channel where the message is located
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--ref TEXT`: Checkout https://aleph-im.gitbook.io/aleph-js/api-resources-reference/posts
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

## `instance`

Manage instances (VMs) on aleph.im network

**Usage**:

```console
$ aleph instance [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `create`: Register a new instance on aleph.im
* `delete`: Delete an instance, unallocating all...
* `list`: List all instances associated with your...

### `instance create`

Register a new instance on aleph.im

**Usage**:

```console
$ aleph instance create [OPTIONS]
```

**Options**:

* `--channel TEXT`: Aleph.im network channel where the message is located
* `--memory INTEGER`: Maximum memory allocation on vm in MiB  [default: 256]
* `--vcpus INTEGER`: Number of virtual cpus to allocate.  [default: 1]
* `--timeout-seconds FLOAT`: If vm is not called after [timeout_seconds] it will shutdown  [default: 30.0]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--ssh-pubkey-file PATH`: Path to a public ssh key to be added to the instance.  [default: /home/mhh/.ssh/id_rsa.pub]
* `--print-messages / --no-print-messages`: [default: no-print-messages]
* `--rootfs TEXT`: Hash of the rootfs to use for your instance. Defaults to Ubuntu 22. You can also create your own rootfs and pin it  [default: Ubuntu 22]
* `--rootfs-name TEXT`: Name of the rootfs to use for your instance. If not set, content.metadata.name of the --rootfs store message will be used.  [default: main-rootfs]
* `--rootfs-size INTEGER`: Size of the rootfs to use for your instance. If not set, content.size of the --rootfs store message will be used.  [default: 2000]
* `--debug / --no-debug`: [default: no-debug]
* `--persistent-volume TEXT`: Persistent volumes are allocated on the host machine and are not deleted when the VM is stopped.

Requires at least a "mount" and "size_mib". For more info, see the docs: https://docs.aleph.im/computing/volumes/persistent/

Example: --persistent_volume persistence=host,size_mib=100,mount=/opt/data
* `--ephemeral-volume TEXT`: Ephemeral volumes are allocated on the host machine when the VM is started and deleted when the VM is stopped.

Example: --ephemeral-volume size_mib=100,mount=/tmp/data
* `--immutable-volume TEXT`: Immutable volumes are pinned on the network and can be used by multiple VMs at the same time. They are read-only and useful for setting up libraries or other dependencies.

Requires at least a "ref" (message hash) and "mount" path. "use_latest" is True by default, to use the latest version of the volume, if it has been amended. See the docs for more info: https://docs.aleph.im/computing/volumes/immutable/

Example: --immutable-volume ref=25a393222692c2f73489dc6710ae87605a96742ceef7b91de4d7ec34bb688d94,mount=/lib/python3.8/site-packages
* `--help`: Show this message and exit.

### `instance delete`

Delete an instance, unallocating all resources associated with it. Immutable volumes will not be deleted.

**Usage**:

```console
$ aleph instance delete [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: [required]

**Options**:

* `--reason TEXT`: Reason for deleting the instance  [default: User deletion]
* `--private-key TEXT`
* `--private-key-file PATH`: [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: [default: no-print-message]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `instance list`

List all instances associated with your private key

**Usage**:

```console
$ aleph instance list [OPTIONS]
```

**Options**:

* `--address TEXT`: Owner address of the instance
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--json / --no-json`: Print as json instead of rich table  [default: no-json]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

## `message`

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

### `message amend`

Amend an existing aleph.im message.

**Usage**:

```console
$ aleph message amend [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Hash reference of the message to amend  [required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `message find`

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

### `message forget`

Forget an existing aleph.im message.

**Usage**:

```console
$ aleph message forget [OPTIONS] HASHES
```

**Arguments**:

* `HASHES`: Comma separated list of hash references of messages to forget  [required]

**Options**:

* `--reason TEXT`: A description of why the messages are being forgotten.
* `--channel TEXT`: Aleph.im network channel where the message is located
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `message get`

**Usage**:

```console
$ aleph message get [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: [required]

**Options**:

* `--help`: Show this message and exit.

### `message post`

Post a message on aleph.im.

**Usage**:

```console
$ aleph message post [OPTIONS]
```

**Options**:

* `--path PATH`: Path to the content you want to post. If omitted, you can input your content directly
* `--type TEXT`: Text representing the message object type  [default: test]
* `--ref TEXT`: Checkout https://aleph-im.gitbook.io/aleph-js/api-resources-reference/posts
* `--channel TEXT`: Aleph.im network channel where the message is located
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `message sign`

Sign an aleph message with a private key. If no --message is provided, the message will be read from stdin.

**Usage**:

```console
$ aleph message sign [OPTIONS]
```

**Options**:

* `--message TEXT`: Message to sign
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `message watch`

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

## `node`

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

### `node compute`

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

### `node core`

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

## `program`

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

### `program unpersist`

Stop a persistent virtual machine by making it non-persistent

**Usage**:

```console
$ aleph program unpersist [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: [required]

**Options**:

* `--private-key TEXT`
* `--private-key-file PATH`: [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `program update`

Update the code of an existing program

**Usage**:

```console
$ aleph program update [OPTIONS] ITEM_HASH PATH
```

**Arguments**:

* `ITEM_HASH`: [required]
* `PATH`: [required]

**Options**:

* `--private-key TEXT`
* `--private-key-file PATH`: [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: [default: print-message]
* `--debug / --no-debug`: [default: no-debug]
* `--help`: Show this message and exit.

### `program upload`

Register a program to run on aleph.im. For more information, see https://docs.aleph.im/computing/

**Usage**:

```console
$ aleph program upload [OPTIONS] PATH ENTRYPOINT
```

**Arguments**:

* `PATH`: Path to your source code  [required]
* `ENTRYPOINT`: Your program entrypoint  [required]

**Options**:

* `--channel TEXT`: Aleph.im network channel where the message is located
* `--memory INTEGER`: Maximum memory allocation on vm in MiB  [default: 256]
* `--vcpus INTEGER`: Number of virtual cpus to allocate.  [default: 1]
* `--timeout-seconds FLOAT`: If vm is not called after [timeout_seconds] it will shutdown  [default: 30.0]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  [default: /home/mhh/.aleph-im/private-keys/ethereum.key]
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

