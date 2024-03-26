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

#### Create an account

All chains provide a `get_fallback_account` function. Example using Ethereum:

```py

from aleph.sdk.chains.ethereum import get_fallback_account


account = get_fallback_account()
```

> Best practice would be creating an account using a key.
> See below

#### Import an account from a private key

=== "Ethereum"

    ```py
    from aleph.sdk.chains.ethereum import ETHAccount

    prv = bytes.fromhex("xxxxxx")
    account = ETHAccount(prv)
    ```

=== "Solana"

    ```py
    from aleph.sdk.chains.solana import SOLAccount

    prv = bytes.fromhex("xxxxxx")
    account = SOLAccount(prv)
    ```

=== "NULS 1 & 2"
    
    ```py
    from aleph.sdk.chains.nuls import NULSAccount

    prv = bytes.fromhex("xxxxxx")
    account = NULSAccount(prv)
    ```

=== "Tezos"

    ```py
    from aleph.sdk.chains.tezos import XTZAccount

    prv = bytes.fromhex("xxxxxx")
    account = XTZAccount(prv)
    ```

=== "Cosmos / Tendermint"

    ```py
    from aleph.sdk.chains.cosmos import CosmosAccount

    prv = bytes.fromhex("xxxxxx")
    account = CosmosAccount(prv)
    ```

=== "Polkadot / Substrate"

    DOT/Substrate accounts are a bit different. You pass them mnemonics, and optionally an address_type.
    
    Example using Substrate (if you already used a fallback on ethereum or nuls, you might consider deleting the private key file):
    
    ```py
    from aleph.sdk.chains.substrate import get_fallback_account
    
    account = get_fallback_account()
    ```
    
    Another example setting the mnemonics manually:
    
    ```py
    from aleph.sdk.chains.substrate import DOTAccount
    
    account = DOTAccount("payment shy team bargain chest fold bless artwork identify breeze pelican category")
    ```
    
    !!! warning
        Do not use this dummy private key, it's just an example!
    
    You can also change the address_type (0 for polkadot, 2 for canary, 42 generic...).
    
    ```py
    from aleph.sdk.chains.substrate import DOTAccount
    account = DOTAccount("payment shy team bargain chest fold bless artwork identify breeze pelican category")
    account.get_address()  # '5CGNMKCscqN2QNcT7Jtuz23ab7JUxh8wTEtXhECZLJn5vCGX'
    account = DOTAccount("payment shy team bargain chest fold bless artwork identify breeze pelican category", 
                         address_type=0)
    account.get_address()  # '1CfVeTwUcdVqucy4wwv8AsjSjJ8ezh5Xjd1rXButPoc6WJY'
    ```
