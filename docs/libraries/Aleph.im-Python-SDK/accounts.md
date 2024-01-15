# Accounts

To send data to the aleph.im network, you need to have an account.
This account can be made using any of the supported wallet providers.

## Supported chains

As of version 0.8.0, the following chains are supported:
- Ethereum (and all EVM compatible chains)
- Solana
- Polkadot / Substrate
- NULS (1 & 2)
- Tezos
- Cosmos / Tendermint

## Private keys

You will need to instantiate an account using a private key accepted by the
corresponding account provider.

If you don't want to handle the private key yourself, you can use the
"fallback" helper. This will search or create a private key file (named by the PRIVATE_KEY_FILE env, default: `ethereum.key`) in the
ALEPH_CONFIG_HOME's "private-keys" directory (default: `~/.aleph.im/private-keys/`).

!!! note
    `get_fallback_account` will use the same private key file as for Ethereum as for every other chain that uses the same 64-bytes format.

## Usage

All chains provide a `get_fallback_account` function. Example using Ethereum:

```python
from aleph.sdk.chains.ethereum import get_fallback_account

account = get_fallback_account()
```

Another example setting the private key manually as raw bytes:

```python
from aleph.sdk.chains.ethereum import ETHAccount

prv = bytes.fromhex("xxxxxx")
account = ETHAccount(prv)
```

### Polkadot / Substrate

DOT/Substrate accounts are a bit different. You pass them mnemonics, and optionally an address_type.

Example using Substrate (if you already used a fallback on ethereum or nuls, you might consider deleting the private key file):

```python
from aleph.sdk.chains.substrate import get_fallback_account

account = get_fallback_account()
```

Another example setting the mnemonics manually:

```python
from aleph.sdk.chains.substrate import DOTAccount

account = DOTAccount("payment shy team bargain chest fold bless artwork identify breeze pelican category")
```

!!! warning
    Do not use this dummy private key, it's just an example!

You can also change the address_type (0 for polkadot, 2 for canary, 42 generic...).

```python
from aleph.sdk.chains.substrate import DOTAccount
account = DOTAccount("payment shy team bargain chest fold bless artwork identify breeze pelican category")
account.get_address()  # '5CGNMKCscqN2QNcT7Jtuz23ab7JUxh8wTEtXhECZLJn5vCGX'
account = DOTAccount("payment shy team bargain chest fold bless artwork identify breeze pelican category", 
                     address_type=0)
account.get_address()  # '1CfVeTwUcdVqucy4wwv8AsjSjJ8ezh5Xjd1rXButPoc6WJY'
```