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

* [`pricing`](#aleph-pricing): Display pricing for services available on aleph.im & twentysix.cloud
* [`account`](#aleph-account): Manage accounts
* [`message`](#aleph-message): Manage messages (post, amend, watch and forget) on aleph.im & twentysix.cloud
* [`aggregate`](#aleph-aggregate): Manage aggregate messages and permissions on aleph.im & twentysix.cloud
* [`file`](#aleph-file): Manage files (upload and pin on IPFS) on aleph.im & twentysix.cloud
* [`program`](#aleph-program): Manage programs (micro-VMs) on aleph.im & twentysix.cloud
* [`instance`](#aleph-instance): Manage instances (VMs) on aleph.im & twentysix.cloud
* [`domain`](#aleph-domain): Manage custom domain (DNS) on aleph.im & twentysix.cloud
* [`node`](#aleph-node): Get node info on aleph.im & twentysix.cloud
* [`about`](#aleph-about): Display the informations of Aleph CLI

## `aleph pricing`

Display pricing for services available on aleph.im & twentysix.cloud

**Usage**:

```console
$ aleph pricing [OPTIONS] SERVICE:{storage|website|program|instance|confidential|gpu|all}
```

**Arguments**:

* `SERVICE:{storage|website|program|instance|confidential|gpu|all}`: Service to display pricing for  \[required]

**Options**:

* `--compute-units INTEGER`: Compute units to display pricing for  \[default: 0]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

## `aleph account`

Manage accounts

**Usage**:

```console
$ aleph account [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* [`create`](#aleph-account-create): Create or import a private key.
* [`address`](#aleph-account-address): Display your public address(es).
* [`chain`](#aleph-account-chain): Display the currently active chain.
* [`path`](#aleph-account-path): Display the directory path where your private keys, config file, and other settings are stored.
* [`show`](#aleph-account-show): Display current configuration.
* [`export-private-key`](#aleph-account-export-private-key): Display your private key.
* [`sign-bytes`](#aleph-account-sign-bytes): Sign a message using your private key.
* [`balance`](#aleph-account-balance): Display your ALEPH balance.
* [`list`](#aleph-account-list): Display available private keys, along with currenlty active chain and account (from config file).
* [`config`](#aleph-account-config): Configure current private key file and active chain (default selection)

### `aleph account create`

Create or import a private key.

**Usage**:

```console
$ aleph account create [OPTIONS]
```

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file
* `--chain [ARB|AVAX|BASE|BLAST|BOB|BSC|CSDK|CYBER|DOT|ETH|FRAX|INK|LINEA|LISK|METIS|MODE|NEO|NULS|NULS2|OP|POL|SOL|TEZOS|WLD|ZORA]`: Chain of origin of your private key (ensuring correct parsing)
* `--replace / --no-replace`: Overwrites private key file if it already exists  \[default: no-replace]
* `--active / --no-active`: Loads the new private key after creation  \[default: active]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph account address`

Display your public address(es).

**Usage**:

```console
$ aleph account address [OPTIONS]
```

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--help`: Show this message and exit.

### `aleph account chain`

Display the currently active chain.

**Usage**:

```console
$ aleph account chain [OPTIONS]
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
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
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

### `aleph account sign-bytes`

Sign a message using your private key.

**Usage**:

```console
$ aleph account sign-bytes [OPTIONS]
```

**Options**:

* `--message TEXT`: Message to sign
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--chain [ARB|AVAX|BASE|BLAST|BOB|BSC|CSDK|CYBER|DOT|ETH|FRAX|INK|LINEA|LISK|METIS|MODE|NEO|NULS|NULS2|OP|POL|SOL|TEZOS|WLD|ZORA]`: Chain for the address
* `--debug / --no-debug`: \[default: no-debug]
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
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--chain [ARB|AVAX|BASE|BLAST|BOB|BSC|CSDK|CYBER|DOT|ETH|FRAX|INK|LINEA|LISK|METIS|MODE|NEO|NULS|NULS2|OP|POL|SOL|TEZOS|WLD|ZORA]`: Chain for the address
* `--help`: Show this message and exit.

### `aleph account list`

Display available private keys, along with currenlty active chain and account (from config file).

**Usage**:

```console
$ aleph account list [OPTIONS]
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
* `--chain [ARB|AVAX|BASE|BLAST|BOB|BSC|CSDK|CYBER|DOT|ETH|FRAX|INK|LINEA|LISK|METIS|MODE|NEO|NULS|NULS2|OP|POL|SOL|TEZOS|WLD|ZORA]`: New active chain
* `--help`: Show this message and exit.

## `aleph message`

Manage messages (post, amend, watch and forget) on aleph.im & twentysix.cloud

**Usage**:

```console
$ aleph message [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* [`get`](#aleph-message-get)
* [`find`](#aleph-message-find)
* [`post`](#aleph-message-post): Post a message on aleph.im.
* [`amend`](#aleph-message-amend): Amend an existing aleph.im message.
* [`forget`](#aleph-message-forget): Forget an existing aleph.im message.
* [`watch`](#aleph-message-watch): Watch a hash for amends and print amend hashes
* [`sign`](#aleph-message-sign): Sign an aleph message with a private key.

### `aleph message get`

**Usage**:

```console
$ aleph message get [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Item hash of the message  \[required]

**Options**:

* `--help`: Show this message and exit.

### `aleph message find`

**Usage**:

```console
$ aleph message find [OPTIONS]
```

**Options**:

* `--pagination INTEGER`: \[default: 200]
* `--page INTEGER`: \[default: 1]
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
* `--ignore-invalid-messages / --no-ignore-invalid-messages`: \[default: ignore-invalid-messages]
* `--help`: Show this message and exit.

### `aleph message post`

Post a message on aleph.im.

**Usage**:

```console
$ aleph message post [OPTIONS]
```

**Options**:

* `--path PATH`: Path to the content you want to post. If omitted, you can input your content directly
* `--type TEXT`: Text representing the message object type  \[default: test]
* `--ref TEXT`: Item hash of the message to update
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  \[default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph message amend`

Amend an existing aleph.im message.

**Usage**:

```console
$ aleph message amend [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Hash reference of the message to amend  \[required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph message forget`

Forget an existing aleph.im message.

**Usage**:

```console
$ aleph message forget [OPTIONS] HASHES
```

**Arguments**:

* `HASHES`: Comma separated list of hash references of messages to forget  \[required]

**Options**:

* `--reason TEXT`: A description of why the messages are being forgotten.
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  \[default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph message watch`

Watch a hash for amends and print amend hashes

**Usage**:

```console
$ aleph message watch [OPTIONS] REF
```

**Arguments**:

* `REF`: Hash reference of the message to watch  \[required]

**Options**:

* `--indent INTEGER`: Number of indents to use
* `--debug / --no-debug`: \[default: no-debug]
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
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

## `aleph aggregate`

Manage aggregate messages and permissions on aleph.im & twentysix.cloud

**Usage**:

```console
$ aleph aggregate [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* [`forget`](#aleph-aggregate-forget): Delete an aggregate by key or subkeys
* [`post`](#aleph-aggregate-post): Create or update an aggregate by key or subkey
* [`get`](#aleph-aggregate-get): Fetch an aggregate by key or subkeys
* [`list`](#aleph-aggregate-list): Display all aggregates associated to an account
* [`authorize`](#aleph-aggregate-authorize): Grant specific publishing permissions to an address to act on behalf of this account
* [`revoke`](#aleph-aggregate-revoke): Revoke all publishing permissions from an address acting on behalf of this account
* [`permissions`](#aleph-aggregate-permissions): Display all permissions emitted by an account

### `aleph aggregate forget`

Delete an aggregate by key or subkeys

**Usage**:

```console
$ aleph aggregate forget [OPTIONS] KEY
```

**Arguments**:

* `KEY`: Aggregate key to remove  \[required]

**Options**:

* `--subkeys TEXT`: Remove specified subkey(s) only. Must be a comma separated list. E.g. `key1` or `key1,key2`
* `--address TEXT`: Target address. Defaults to current account address
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  \[default: ALEPH-CLOUDSOLUTIONS]
* `--inline / --no-inline`: inline  \[default: no-inline]
* `--sync / --no-sync`: Sync response  \[default: no-sync]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: \[default: no-print-message]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph aggregate post`

Create or update an aggregate by key or subkey

**Usage**:

```console
$ aleph aggregate post [OPTIONS] KEY CONTENT
```

**Arguments**:

* `KEY`: Aggregate key to create/update  \[required]
* `CONTENT`: Aggregate content, in json format and between single quotes. E.g. '{"a": 1, "b": 2}'. If a subkey is provided, also allow to pass a string content between quotes  \[required]

**Options**:

* `--subkey TEXT`: Specified subkey where the content will be replaced
* `--address TEXT`: Target address. Defaults to current account address
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  \[default: ALEPH-CLOUDSOLUTIONS]
* `--inline / --no-inline`: inline  \[default: no-inline]
* `--sync / --no-sync`: Sync response  \[default: no-sync]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: \[default: no-print-message]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph aggregate get`

Fetch an aggregate by key or subkeys

**Usage**:

```console
$ aleph aggregate get [OPTIONS] KEY
```

**Arguments**:

* `KEY`: Aggregate key to fetch  \[required]

**Options**:

* `--subkeys TEXT`: Fetch specified subkey(s) only. Must be a comma separated list. E.g. `key1` or `key1,key2`
* `--address TEXT`: Target address. Defaults to current account address
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph aggregate list`

Display all aggregates associated to an account

**Usage**:

```console
$ aleph aggregate list [OPTIONS]
```

**Options**:

* `--address TEXT`: Target address. Defaults to current account address
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--json / --no-json`: Print as json instead of rich table  \[default: no-json]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph aggregate authorize`

Grant specific publishing permissions to an address to act on behalf of this account

**Usage**:

```console
$ aleph aggregate authorize [OPTIONS] ADDRESS
```

**Arguments**:

* `ADDRESS`: Target address. Defaults to current account address  \[required]

**Options**:

* `--chain [ARB|AVAX|BASE|BLAST|BOB|BSC|CSDK|CYBER|DOT|ETH|FRAX|INK|LINEA|LISK|METIS|MODE|NEO|NULS|NULS2|OP|POL|SOL|TEZOS|WLD|ZORA]`: Only on specified chain
* `--types TEXT`: Only for specified message types (comma separated list)
* `--channels TEXT`: Only on specified channels (comma separated list)
* `--post-types TEXT`: Only for specified post types (comma separated list)
* `--aggregate-keys TEXT`: Only for specified aggregate keys (comma separated list)
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: \[default: no-print-message]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph aggregate revoke`

Revoke all publishing permissions from an address acting on behalf of this account

**Usage**:

```console
$ aleph aggregate revoke [OPTIONS] ADDRESS
```

**Arguments**:

* `ADDRESS`: Target address. Defaults to current account address  \[required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: \[default: no-print-message]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph aggregate permissions`

Display all permissions emitted by an account

**Usage**:

```console
$ aleph aggregate permissions [OPTIONS]
```

**Options**:

* `--address TEXT`: Target address. Defaults to current account address
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--json / --no-json`: Print as json instead of rich table  \[default: no-json]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

## `aleph file`

Manage files (upload and pin on IPFS) on aleph.im & twentysix.cloud

**Usage**:

```console
$ aleph file [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* [`pin`](#aleph-file-pin): Persist a file from IPFS on aleph.im.
* [`upload`](#aleph-file-upload): Upload and store a file on aleph.im.
* [`download`](#aleph-file-download): Download a file from aleph.im or display related infos.
* [`forget`](#aleph-file-forget): forget a file and his message on aleph.im.
* [`list`](#aleph-file-list): List all files for a given address

### `aleph file pin`

Persist a file from IPFS on aleph.im.

**Usage**:

```console
$ aleph file pin [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: IPFS hash to pin on aleph.im  \[required]

**Options**:

* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  \[default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--ref TEXT`: Item hash of the message to update
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph file upload`

Upload and store a file on aleph.im.

**Usage**:

```console
$ aleph file upload [OPTIONS] PATH
```

**Arguments**:

* `PATH`: Path of the file to upload  \[required]

**Options**:

* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  \[default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--ref TEXT`: Item hash of the message to update
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph file download`

Download a file from aleph.im or display related infos.

**Usage**:

```console
$ aleph file download [OPTIONS] HASH
```

**Arguments**:

* `HASH`: hash to download from aleph.  \[required]

**Options**:

* `--use-ipfs / --no-use-ipfs`: Download using IPFS instead of storage  \[default: no-use-ipfs]
* `--output-path PATH`: Output directory path  \[default: .]
* `--file-name TEXT`: Output file name (without extension)
* `--file-extension TEXT`: Output file extension
* `--only-info / --no-only-info`: \[default: no-only-info]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph file forget`

forget a file and his message on aleph.im.

**Usage**:

```console
$ aleph file forget [OPTIONS] ITEM_HASH [REASON]
```

**Arguments**:

* `ITEM_HASH`: Hash(es) to forget. Must be a comma separated list. Example: `123...abc` or `123...abc,456...xyz`  \[required]
* `[REASON]`: reason to forget  \[default: User deletion]

**Options**:

* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  \[default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: \[default: no-debug]
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
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--pagination INTEGER`: Maximum number of files to return.  \[default: 100]
* `--page INTEGER`: Offset in pages.  \[default: 1]
* `--sort-order INTEGER`: Order in which files should be listed: -1 means most recent messages first, 1 means older messages first.  \[default: -1]
* `--json / --no-json`: Print as json instead of rich table  \[default: no-json]
* `--help`: Show this message and exit.

## `aleph program`

Manage programs (micro-VMs) on aleph.im & twentysix.cloud

**Usage**:

```console
$ aleph program [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* [`create`](#aleph-program-create): Register a program to run on aleph.im (create/upload are aliases)
* [`upload`](#aleph-program-upload): Register a program to run on aleph.im (create/upload are aliases)
* [`update`](#aleph-program-update): Update the code of an existing program (item hash will not change)
* [`delete`](#aleph-program-delete): Delete a program
* [`list`](#aleph-program-list): List all programs associated to an account
* [`persist`](#aleph-program-persist): Recreate a non-persistent program as persistent (item hash will change).
* [`unpersist`](#aleph-program-unpersist): Recreate a persistent program as non-persistent (item hash will change).
* [`logs`](#aleph-program-logs): Display the logs of a program
* [`runtime-checker`](#aleph-program-runtime-checker): Check versions used by a runtime (distribution, python, nodejs, etc)

### `aleph program create`

Register a program to run on aleph.im (create/upload are aliases)

For more information, see https://docs.aleph.im/computing

**Usage**:

```console
$ aleph program create [OPTIONS] PATH ENTRYPOINT
```

**Arguments**:

* `PATH`: Path to your source code. Can be a directory, a .squashfs file or a .zip archive  \[required]
* `ENTRYPOINT`: Your program entrypoint. Example: `main:app` for Python programs, else `run.sh` for a script containing your launch command  \[required]

**Options**:

* `--name TEXT`: Name for your program
* `--runtime TEXT`: Hash of the runtime to use for your program. You can also create your own runtime and pin it. Currently defaults to `63f07193e6ee9d207b7d1fcf8286f9aee34e6f12f101d2ec77c1229f92964696` (Use `aleph program runtime-checker` to inspect it)
* `--compute-units INTEGER`: Number of compute units to allocate. Compute units correspond to a tier that includes vcpus, memory, disk and gpu presets. For reference, run: `aleph pricing --help`
* `--vcpus INTEGER`: Number of virtual CPUs to allocate
* `--memory INTEGER`: Maximum memory (RAM) in MiB to allocate
* `--timeout-seconds FLOAT`: If vm is not called after [timeout_seconds] it will shutdown  \[default: 30.0]
* `--internet / --no-internet`: Enable internet access for your program. By default, internet access is disabled  \[default: no-internet]
* `--updatable / --no-updatable`: Allow program updates. By default, only the source code can be modified without requiring redeployement (same item hash). When enabled (set to True), this option allows to update any other field. However, such modifications will require a program redeployment (new item hash)  \[default: no-updatable]
* `--beta / --no-beta`: If true, you will be prompted to add message subscriptions to your program  \[default: no-beta]
* `--persistent / --no-persistent`: Create your program as persistent. By default, programs are ephemeral (serverless): they only start when called and then shutdown after the defined timeout delay.  \[default: no-persistent]
* `--skip-volume / --no-skip-volume`: Skip prompt to attach more volumes  \[default: no-skip-volume]
* `--persistent-volume TEXT`: Persistent volumes are allocated on the host machine and are not deleted when the VM is stopped.
Requires at least `name`, `persistence`, `mount` and `size_mib`. For more info, see the docs: https://docs.aleph.im/computing/volumes/persistent/
Example: --persistent_volume name=data,persistence=host,size_mib=100,mount=/opt/data
* `--ephemeral-volume TEXT`: Ephemeral volumes are allocated on the host machine when the VM is started and deleted when the VM is stopped.
Requires at least `name`, `mount` and `size_mib`.
Example: --ephemeral-volume name=temp,size_mib=100,mount=/tmp/data
* `--immutable-volume TEXT`: Immutable volumes are pinned on the network and can be used by multiple VMs at the same time. They are read-only and useful for setting up libraries or other dependencies.
Requires at least `name`, `ref` (message hash) and `mount` path. `use_latest` is True by default, to use the latest version of the volume, if it has been amended. See the docs for more info: https://docs.aleph.im/computing/volumes/immutable/
Example: --immutable-volume name=libs,ref=25a3...8d94,mount=/lib/python3.11/site-packages
* `--skip-env-var / --no-skip-env-var`: Skip prompt to set environment variables  \[default: no-skip-env-var]
* `--env-vars TEXT`: Environment variables to pass. They will be public and visible in the message, so don't include secrets. Must be a comma separated list. Example: `KEY=value` or `KEY=value,KEY=value`
* `--address TEXT`: Address of the payer. In order to delegate the payment, your account must be authorized beforehand to publish on the behalf of this address. See the docs for more info: https://docs.aleph.im/protocol/permissions/
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  \[default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-messages / --no-print-messages`: \[default: no-print-messages]
* `--print-code-message / --no-print-code-message`: \[default: no-print-code-message]
* `--print-program-message / --no-print-program-message`: \[default: no-print-program-message]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph program upload`

Register a program to run on aleph.im (create/upload are aliases)

For more information, see https://docs.aleph.im/computing

**Usage**:

```console
$ aleph program upload [OPTIONS] PATH ENTRYPOINT
```

**Arguments**:

* `PATH`: Path to your source code. Can be a directory, a .squashfs file or a .zip archive  \[required]
* `ENTRYPOINT`: Your program entrypoint. Example: `main:app` for Python programs, else `run.sh` for a script containing your launch command  \[required]

**Options**:

* `--name TEXT`: Name for your program
* `--runtime TEXT`: Hash of the runtime to use for your program. You can also create your own runtime and pin it. Currently defaults to `63f07193e6ee9d207b7d1fcf8286f9aee34e6f12f101d2ec77c1229f92964696` (Use `aleph program runtime-checker` to inspect it)
* `--compute-units INTEGER`: Number of compute units to allocate. Compute units correspond to a tier that includes vcpus, memory, disk and gpu presets. For reference, run: `aleph pricing --help`
* `--vcpus INTEGER`: Number of virtual CPUs to allocate
* `--memory INTEGER`: Maximum memory (RAM) in MiB to allocate
* `--timeout-seconds FLOAT`: If vm is not called after [timeout_seconds] it will shutdown  \[default: 30.0]
* `--internet / --no-internet`: Enable internet access for your program. By default, internet access is disabled  \[default: no-internet]
* `--updatable / --no-updatable`: Allow program updates. By default, only the source code can be modified without requiring redeployement (same item hash). When enabled (set to True), this option allows to update any other field. However, such modifications will require a program redeployment (new item hash)  \[default: no-updatable]
* `--beta / --no-beta`: If true, you will be prompted to add message subscriptions to your program  \[default: no-beta]
* `--persistent / --no-persistent`: Create your program as persistent. By default, programs are ephemeral (serverless): they only start when called and then shutdown after the defined timeout delay.  \[default: no-persistent]
* `--skip-volume / --no-skip-volume`: Skip prompt to attach more volumes  \[default: no-skip-volume]
* `--persistent-volume TEXT`: Persistent volumes are allocated on the host machine and are not deleted when the VM is stopped.
Requires at least `name`, `persistence`, `mount` and `size_mib`. For more info, see the docs: https://docs.aleph.im/computing/volumes/persistent/
Example: --persistent_volume name=data,persistence=host,size_mib=100,mount=/opt/data
* `--ephemeral-volume TEXT`: Ephemeral volumes are allocated on the host machine when the VM is started and deleted when the VM is stopped.
Requires at least `name`, `mount` and `size_mib`.
Example: --ephemeral-volume name=temp,size_mib=100,mount=/tmp/data
* `--immutable-volume TEXT`: Immutable volumes are pinned on the network and can be used by multiple VMs at the same time. They are read-only and useful for setting up libraries or other dependencies.
Requires at least `name`, `ref` (message hash) and `mount` path. `use_latest` is True by default, to use the latest version of the volume, if it has been amended. See the docs for more info: https://docs.aleph.im/computing/volumes/immutable/
Example: --immutable-volume name=libs,ref=25a3...8d94,mount=/lib/python3.11/site-packages
* `--skip-env-var / --no-skip-env-var`: Skip prompt to set environment variables  \[default: no-skip-env-var]
* `--env-vars TEXT`: Environment variables to pass. They will be public and visible in the message, so don't include secrets. Must be a comma separated list. Example: `KEY=value` or `KEY=value,KEY=value`
* `--address TEXT`: Address of the payer. In order to delegate the payment, your account must be authorized beforehand to publish on the behalf of this address. See the docs for more info: https://docs.aleph.im/protocol/permissions/
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  \[default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-messages / --no-print-messages`: \[default: no-print-messages]
* `--print-code-message / --no-print-code-message`: \[default: no-print-code-message]
* `--print-program-message / --no-print-program-message`: \[default: no-print-program-message]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph program update`

Update the code of an existing program (item hash will not change)

**Usage**:

```console
$ aleph program update [OPTIONS] ITEM_HASH PATH
```

**Arguments**:

* `ITEM_HASH`: Item hash to update  \[required]
* `PATH`: Path to your source code. Can be a directory, a .squashfs file or a .zip archive  \[required]

**Options**:

* `--private-key TEXT`
* `--private-key-file PATH`: \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: \[default: no-print-message]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph program delete`

Delete a program

**Usage**:

```console
$ aleph program delete [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Item hash to unpersist  \[required]

**Options**:

* `--reason TEXT`: Reason for deleting the program  \[default: User deletion]
* `--keep-code / --no-keep-code`: Keep the source code intact instead of deleting it  \[default: no-keep-code]
* `--private-key TEXT`
* `--private-key-file PATH`: \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: \[default: no-print-message]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph program list`

List all programs associated to an account

**Usage**:

```console
$ aleph program list [OPTIONS]
```

**Options**:

* `--address TEXT`: Owner address of the programs
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--json / --no-json`: Print as json instead of rich table  \[default: no-json]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph program persist`

Recreate a non-persistent program as persistent (item hash will change). The program must be updatable and yours

**Usage**:

```console
$ aleph program persist [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Item hash to persist  \[required]

**Options**:

* `--keep-prev / --no-keep-prev`: Keep the previous program intact instead of deleting it  \[default: no-keep-prev]
* `--private-key TEXT`
* `--private-key-file PATH`: \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: \[default: no-print-message]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph program unpersist`

Recreate a persistent program as non-persistent (item hash will change). The program must be updatable and yours

**Usage**:

```console
$ aleph program unpersist [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Item hash to unpersist  \[required]

**Options**:

* `--keep-prev / --no-keep-prev`: Keep the previous program intact instead of deleting it  \[default: no-keep-prev]
* `--private-key TEXT`
* `--private-key-file PATH`: \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: \[default: no-print-message]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph program logs`

Display the logs of a program

Will only show logs from the selected CRN

**Usage**:

```console
$ aleph program logs [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Item hash of program  \[required]

**Options**:

* `--private-key TEXT`
* `--private-key-file PATH`: \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--domain TEXT`: URL of the CRN (Compute node) on which the program is running
* `--chain [ARB|AVAX|BASE|BLAST|BOB|BSC|CSDK|CYBER|DOT|ETH|FRAX|INK|LINEA|LISK|METIS|MODE|NEO|NULS|NULS2|OP|POL|SOL|TEZOS|WLD|ZORA]`: Chain for the address
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph program runtime-checker`

Check versions used by a runtime (distribution, python, nodejs, etc)

**Usage**:

```console
$ aleph program runtime-checker [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Item hash of the runtime to check  \[required]

**Options**:

* `--private-key TEXT`
* `--private-key-file PATH`: \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--verbose / --no-verbose`: \[default: no-verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

## `aleph instance`

Manage instances (VMs) on aleph.im & twentysix.cloud

**Usage**:

```console
$ aleph instance [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* [`create`](#aleph-instance-create): Create and register a new instance on aleph.im
* [`delete`](#aleph-instance-delete): Delete an instance, unallocating all resources associated with it.
* [`list`](#aleph-instance-list): List all instances associated to an account
* [`reboot`](#aleph-instance-reboot): Reboot an instance
* [`allocate`](#aleph-instance-allocate): Notify a CRN to start an instance (for Pay-As-You-Go and confidential instances only)
* [`logs`](#aleph-instance-logs): Retrieve the logs of an instance
* [`stop`](#aleph-instance-stop): Stop an instance
* [`confidential-init-session`](#aleph-instance-confidential-init-session): Initialize a confidential communication session with the VM
* [`confidential-start`](#aleph-instance-confidential-start): Validate the authenticity of the VM and start it
* [`confidential`](#aleph-instance-confidential): Create (optional), start and unlock a confidential VM (all-in-one command)
* [`gpu`](#aleph-instance-gpu): Create and register a new GPU instance on aleph.im

### `aleph instance create`

Create and register a new instance on aleph.im

**Usage**:

```console
$ aleph instance create [OPTIONS]
```

**Options**:

* `--payment-type [hold|superfluid|nft]`: Payment method, either holding tokens, NFTs, or Pay-As-You-Go via token streaming
* `--payment-chain [AVAX|BASE|ETH|SOL]`: Chain you want to use to pay for your instance
* `--hypervisor [qemu|firecracker]`: Hypervisor to use to launch your instance. Always defaults to QEMU, since Firecracker is now deprecated for instances  \[default: qemu]
* `--name TEXT`: Name of your new instance
* `--rootfs TEXT`: Hash of the rootfs to use for your instance. Defaults to Ubuntu 22. You can also create your own rootfs and pin it
* `--compute-units INTEGER`: Number of compute units to allocate. Compute units correspond to a tier that includes vcpus, memory, disk and gpu presets. For reference, run: `aleph pricing --help`
* `--vcpus INTEGER`: Number of virtual CPUs to allocate
* `--memory INTEGER`: Maximum memory (RAM) in MiB to allocate
* `--rootfs-size INTEGER`: Rootfs size in MiB to allocate
* `--timeout-seconds FLOAT`: If vm is not called after [timeout_seconds] it will shutdown  \[default: 30.0]
* `--ssh-pubkey-file PATH`: Path to a public ssh key to be added to the instance  \[default: /home/$USER/.ssh/id_rsa.pub]
* `--address TEXT`: Address of the payer. In order to delegate the payment, your account must be authorized beforehand to publish on the behalf of this address. See the docs for more info: https://docs.aleph.im/protocol/permissions/
* `--crn-hash TEXT`: Hash of the CRN to deploy to (only applicable for confidential and/or Pay-As-You-Go instances)
* `--crn-url TEXT`: URL of the CRN to deploy to (only applicable for confidential and/or Pay-As-You-Go instances)
* `--confidential / --no-confidential`: Launch a confidential instance (requires creating an encrypted volume)  \[default: no-confidential]
* `--confidential-firmware TEXT`: Hash to UEFI Firmware to launch confidential instance  \[default: ba5bb13f3abca960b101a759be162b229e2b7e93ecad9d1307e54de887f177ff]
* `--gpu / --no-gpu`: Launch an instance attaching a GPU to it  \[default: no-gpu]
* `--premium / --no-premium`: Use Premium GPUs (VRAM > 48GiB)
* `--skip-volume / --no-skip-volume`: Skip prompt to attach more volumes  \[default: no-skip-volume]
* `--persistent-volume TEXT`: Persistent volumes are allocated on the host machine and are not deleted when the VM is stopped.
Requires at least `name`, `persistence`, `mount` and `size_mib`. For more info, see the docs: https://docs.aleph.im/computing/volumes/persistent/
Example: --persistent_volume name=data,persistence=host,size_mib=100,mount=/opt/data
* `--ephemeral-volume TEXT`: Ephemeral volumes are allocated on the host machine when the VM is started and deleted when the VM is stopped.
Requires at least `name`, `mount` and `size_mib`.
Example: --ephemeral-volume name=temp,size_mib=100,mount=/tmp/data
* `--immutable-volume TEXT`: Immutable volumes are pinned on the network and can be used by multiple VMs at the same time. They are read-only and useful for setting up libraries or other dependencies.
Requires at least `name`, `ref` (message hash) and `mount` path. `use_latest` is True by default, to use the latest version of the volume, if it has been amended. See the docs for more info: https://docs.aleph.im/computing/volumes/immutable/
Example: --immutable-volume name=libs,ref=25a3...8d94,mount=/lib/python3.11/site-packages
* `--crn-auto-tac / --no-crn-auto-tac`: Automatically accept the Terms & Conditions of the CRN if you read them beforehand  \[default: no-crn-auto-tac]
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  \[default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: \[default: no-print-message]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance delete`

Delete an instance, unallocating all resources associated with it. Associated VM will be stopped and erased.
Immutable volumes will not be deleted.

**Usage**:

```console
$ aleph instance delete [OPTIONS] ITEM_HASH
```

**Arguments**:

* `ITEM_HASH`: Instance item hash to forget  \[required]

**Options**:

* `--reason TEXT`: Reason for deleting the instance  \[default: User deletion]
* `--chain [AVAX|BASE|ETH|SOL]`: Chain you are using to pay for your instance
* `--domain TEXT`: Domain of the CRN where an associated VM is running. It ensures your VM will be stopped and erased on the CRN before the instance message is actually deleted
* `--private-key TEXT`
* `--private-key-file PATH`: \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: \[default: no-print-message]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance list`

List all instances associated to an account

**Usage**:

```console
$ aleph instance list [OPTIONS]
```

**Options**:

* `--address TEXT`: Owner address of the instances
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--chain [AVAX|BASE|ETH|SOL]`: Chain for the address
* `--json / --no-json`: Print as json instead of rich table  \[default: no-json]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance reboot`

Reboot an instance

**Usage**:

```console
$ aleph instance reboot [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to reboot  \[required]

**Options**:

* `--domain TEXT`: CRN domain on which the VM is running
* `--chain [AVAX|BASE|ETH|SOL]`: Chain you are using to pay for your instance
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance allocate`

Notify a CRN to start an instance (for Pay-As-You-Go and confidential instances only)

**Usage**:

```console
$ aleph instance allocate [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to allocate  \[required]

**Options**:

* `--domain TEXT`: CRN domain on which the VM will be allocated
* `--chain [AVAX|BASE|ETH|SOL]`: Chain you are using to pay for your instance
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance logs`

Retrieve the logs of an instance

**Usage**:

```console
$ aleph instance logs [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to retrieve the logs from  \[required]

**Options**:

* `--domain TEXT`: CRN domain on which the VM is running
* `--chain [AVAX|BASE|ETH|SOL]`: Chain you are using to pay for your instance
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance stop`

Stop an instance

**Usage**:

```console
$ aleph instance stop [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to stop  \[required]

**Options**:

* `--domain TEXT`: CRN domain on which the VM is running
* `--chain [ARB|AVAX|BASE|BLAST|BOB|BSC|CSDK|CYBER|DOT|ETH|FRAX|INK|LINEA|LISK|METIS|MODE|NEO|NULS|NULS2|OP|POL|SOL|TEZOS|WLD|ZORA]`: Chain you are using to pay for your instance
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance confidential-init-session`

Initialize a confidential communication session with the VM

**Usage**:

```console
$ aleph instance confidential-init-session [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to initialize the session for  \[required]

**Options**:

* `--domain TEXT`: CRN domain on which the session will be initialized
* `--chain [AVAX|BASE|ETH|SOL]`: Chain you are using to pay for your instance
* `--policy INTEGER`: \[default: 1]
* `--keep-session / --no-keep-session`: Keeping the already initiated session
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance confidential-start`

Validate the authenticity of the VM and start it

**Usage**:

```console
$ aleph instance confidential-start [OPTIONS] VM_ID
```

**Arguments**:

* `VM_ID`: VM item hash to start  \[required]

**Options**:

* `--domain TEXT`: CRN domain on which the VM will be started
* `--chain [AVAX|BASE|ETH|SOL]`: Chain you are using to pay for your instance
* `--firmware-hash TEXT`: Hash of the UEFI Firmware content, to validate measure (ignored if path is provided)  \[default: 89b76b0e64fe9015084fbffdf8ac98185bafc688bfe7a0b398585c392d03c7ee]
* `--firmware-file TEXT`: Path to the UEFI Firmware content, to validate measure (instead of the hash)
* `--vm-secret TEXT`: Secret password to start the VM
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
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
* `--policy INTEGER`: \[default: 1]
* `--confidential-firmware TEXT`: Hash to UEFI Firmware to launch confidential instance  \[default: ba5bb13f3abca960b101a759be162b229e2b7e93ecad9d1307e54de887f177ff]
* `--firmware-hash TEXT`: Hash of the UEFI Firmware content, to validate measure (ignored if path is provided)  \[default: 89b76b0e64fe9015084fbffdf8ac98185bafc688bfe7a0b398585c392d03c7ee]
* `--firmware-file TEXT`: Path to the UEFI Firmware content, to validate measure (instead of the hash)
* `--keep-session / --no-keep-session`: Keeping the already initiated session
* `--vm-secret TEXT`: Secret password to start the VM
* `--payment-type [hold|superfluid|nft]`: Payment method, either holding tokens, NFTs, or Pay-As-You-Go via token streaming
* `--payment-chain [AVAX|BASE|ETH|SOL]`: Chain you want to use to pay for your instance
* `--name TEXT`: Name of your new instance
* `--rootfs TEXT`: Hash of the rootfs to use for your instance. Defaults to Ubuntu 22. You can also create your own rootfs and pin it
* `--compute-units INTEGER`: Number of compute units to allocate. Compute units correspond to a tier that includes vcpus, memory, disk and gpu presets. For reference, run: `aleph pricing --help`
* `--vcpus INTEGER`: Number of virtual CPUs to allocate
* `--memory INTEGER`: Maximum memory (RAM) in MiB to allocate
* `--rootfs-size INTEGER`: Rootfs size in MiB to allocate
* `--timeout-seconds FLOAT`: If vm is not called after [timeout_seconds] it will shutdown  \[default: 30.0]
* `--ssh-pubkey-file PATH`: Path to a public ssh key to be added to the instance  \[default: /home/$USER/.ssh/id_rsa.pub]
* `--address TEXT`: Address of the payer. In order to delegate the payment, your account must be authorized beforehand to publish on the behalf of this address. See the docs for more info: https://docs.aleph.im/protocol/permissions/
* `--gpu / --no-gpu`: Launch an instance attaching a GPU to it  \[default: no-gpu]
* `--premium / --no-premium`: Use Premium GPUs (VRAM > 48GiB)
* `--skip-volume / --no-skip-volume`: Skip prompt to attach more volumes  \[default: no-skip-volume]
* `--persistent-volume TEXT`: Persistent volumes are allocated on the host machine and are not deleted when the VM is stopped.
Requires at least `name`, `persistence`, `mount` and `size_mib`. For more info, see the docs: https://docs.aleph.im/computing/volumes/persistent/
Example: --persistent_volume name=data,persistence=host,size_mib=100,mount=/opt/data
* `--ephemeral-volume TEXT`: Ephemeral volumes are allocated on the host machine when the VM is started and deleted when the VM is stopped.
Requires at least `name`, `mount` and `size_mib`.
Example: --ephemeral-volume name=temp,size_mib=100,mount=/tmp/data
* `--immutable-volume TEXT`: Immutable volumes are pinned on the network and can be used by multiple VMs at the same time. They are read-only and useful for setting up libraries or other dependencies.
Requires at least `name`, `ref` (message hash) and `mount` path. `use_latest` is True by default, to use the latest version of the volume, if it has been amended. See the docs for more info: https://docs.aleph.im/computing/volumes/immutable/
Example: --immutable-volume name=libs,ref=25a3...8d94,mount=/lib/python3.11/site-packages
* `--crn-auto-tac / --no-crn-auto-tac`: Automatically accept the Terms & Conditions of the CRN if you read them beforehand  \[default: no-crn-auto-tac]
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  \[default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph instance gpu`

Create and register a new GPU instance on aleph.im

**Usage**:

```console
$ aleph instance gpu [OPTIONS]
```

**Options**:

* `--payment-chain [AVAX|BASE]`: Chain you want to use to pay for your instance
* `--name TEXT`: Name of your new instance
* `--rootfs TEXT`: Hash of the rootfs to use for your instance. Defaults to Ubuntu 22. You can also create your own rootfs and pin it
* `--compute-units INTEGER`: Number of compute units to allocate. Compute units correspond to a tier that includes vcpus, memory, disk and gpu presets. For reference, run: `aleph pricing --help`
* `--vcpus INTEGER`: Number of virtual CPUs to allocate
* `--memory INTEGER`: Maximum memory (RAM) in MiB to allocate
* `--rootfs-size INTEGER`: Rootfs size in MiB to allocate
* `--premium / --no-premium`: Use Premium GPUs (VRAM > 48GiB)
* `--timeout-seconds FLOAT`: If vm is not called after [timeout_seconds] it will shutdown  \[default: 30.0]
* `--ssh-pubkey-file PATH`: Path to a public ssh key to be added to the instance  \[default: /home/$USER/.ssh/id_rsa.pub]
* `--address TEXT`: Address of the payer. In order to delegate the payment, your account must be authorized beforehand to publish on the behalf of this address. See the docs for more info: https://docs.aleph.im/protocol/permissions/
* `--crn-hash TEXT`: Hash of the CRN to deploy to (only applicable for confidential and/or Pay-As-You-Go instances)
* `--crn-url TEXT`: URL of the CRN to deploy to (only applicable for confidential and/or Pay-As-You-Go instances)
* `--skip-volume / --no-skip-volume`: Skip prompt to attach more volumes  \[default: no-skip-volume]
* `--persistent-volume TEXT`: Persistent volumes are allocated on the host machine and are not deleted when the VM is stopped.
Requires at least `name`, `persistence`, `mount` and `size_mib`. For more info, see the docs: https://docs.aleph.im/computing/volumes/persistent/
Example: --persistent_volume name=data,persistence=host,size_mib=100,mount=/opt/data
* `--ephemeral-volume TEXT`: Ephemeral volumes are allocated on the host machine when the VM is started and deleted when the VM is stopped.
Requires at least `name`, `mount` and `size_mib`.
Example: --ephemeral-volume name=temp,size_mib=100,mount=/tmp/data
* `--immutable-volume TEXT`: Immutable volumes are pinned on the network and can be used by multiple VMs at the same time. They are read-only and useful for setting up libraries or other dependencies.
Requires at least `name`, `ref` (message hash) and `mount` path. `use_latest` is True by default, to use the latest version of the volume, if it has been amended. See the docs for more info: https://docs.aleph.im/computing/volumes/immutable/
Example: --immutable-volume name=libs,ref=25a3...8d94,mount=/lib/python3.11/site-packages
* `--crn-auto-tac / --no-crn-auto-tac`: Automatically accept the Terms & Conditions of the CRN if you read them beforehand  \[default: no-crn-auto-tac]
* `--channel TEXT`: Aleph.im network channel where the message is or will be broadcasted  \[default: ALEPH-CLOUDSOLUTIONS]
* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--print-message / --no-print-message`: \[default: no-print-message]
* `--verbose / --no-verbose`: \[default: verbose]
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

## `aleph domain`

Manage custom domain (DNS) on aleph.im & twentysix.cloud

**Usage**:

```console
$ aleph domain [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* [`add`](#aleph-domain-add): Add and link a Custom Domain.
* [`attach`](#aleph-domain-attach): Attach resource to a Custom Domain.
* [`detach`](#aleph-domain-detach): Unlink Custom Domain.
* [`info`](#aleph-domain-info): Show Custom Domain Details.

### `aleph domain add`

Add and link a Custom Domain.

**Usage**:

```console
$ aleph domain add [OPTIONS] FQDN
```

**Arguments**:

* `FQDN`: Domain name. ex: aleph.im  \[required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--target [ipfs|program|instance]`: IPFS|PROGRAM|INSTANCE
* `--item-hash TEXT`: Item hash
* `--owner TEXT`: Owner address. Defaults to current account address
* `--ask / --no-ask`: Prompt user for confirmation  \[default: ask]
* `--help`: Show this message and exit.

### `aleph domain attach`

Attach resource to a Custom Domain.

**Usage**:

```console
$ aleph domain attach [OPTIONS] FQDN
```

**Arguments**:

* `FQDN`: Domain name. ex: aleph.im  \[required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--item-hash TEXT`: Item hash
* `--catch-all-path TEXT`: Choose a relative path to catch all unmatched route or a 404 error
* `--ask / --no-ask`: Prompt user for confirmation  \[default: ask]
* `--help`: Show this message and exit.

### `aleph domain detach`

Unlink Custom Domain.

**Usage**:

```console
$ aleph domain detach [OPTIONS] FQDN
```

**Arguments**:

* `FQDN`: Domain name. ex: aleph.im  \[required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--ask / --no-ask`: Prompt user for confirmation  \[default: ask]
* `--help`: Show this message and exit.

### `aleph domain info`

Show Custom Domain Details.

**Usage**:

```console
$ aleph domain info [OPTIONS] FQDN
```

**Arguments**:

* `FQDN`: Domain name. ex: aleph.im  \[required]

**Options**:

* `--private-key TEXT`: Your private key. Cannot be used with --private-key-file
* `--private-key-file PATH`: Path to your private key file  \[default: /home/$USER/.aleph-im/private-keys/ethereum.key]
* `--help`: Show this message and exit.

## `aleph node`

Get node info on aleph.im & twentysix.cloud

**Usage**:

```console
$ aleph node [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* [`compute`](#aleph-node-compute): Get all compute node (CRN) on aleph network
* [`core`](#aleph-node-core): Get all core node (CCN) on aleph

### `aleph node compute`

Get all compute node (CRN) on aleph network

**Usage**:

```console
$ aleph node compute [OPTIONS]
```

**Options**:

* `--json / --no-json`: Print as json instead of rich table  \[default: no-json]
* `--active / --no-active`: Only show active nodes  \[default: no-active]
* `--address TEXT`: Owner address to filter by
* `--payg-receiver TEXT`: PAYG (Pay-As-You-Go) receiver address to filter by
* `--crn-url TEXT`: CRN Url to filter by
* `--crn-hash TEXT`: CRN hash to filter by
* `--ccn-hash TEXT`: Linked CCN hash to filter by
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

### `aleph node core`

Get all core node (CCN) on aleph

**Usage**:

```console
$ aleph node core [OPTIONS]
```

**Options**:

* `--json / --no-json`: Print as json instead of rich table  \[default: no-json]
* `--active / --no-active`: Only show active nodes  \[default: no-active]
* `--address TEXT`: Owner address to filter by
* `--ccn-hash TEXT`: CCN hash to filter by
* `--debug / --no-debug`: \[default: no-debug]
* `--help`: Show this message and exit.

## `aleph about`

Display the informations of Aleph CLI

**Usage**:

```console
$ aleph about [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* [`version`](#aleph-about-version)

### `aleph about version`

**Usage**:

```console
$ aleph about version [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
