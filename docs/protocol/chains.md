## Chains

Multiple blockchains are supported when interacting with aleph.im.

The support of a chain consists in the functionalities below. 
The support of a chain may be partial, when only some of these 
functionalities are supported.

1. **Message signature**: \
   Messages on the aleph.im network must be signed using asymmetric a user's private key.
   Different chains may use public-key cryptography differently, resulting in different methods
   of verifying message signatures.
2. **Wallet support** \
   Interacting with aleph.im in a browser and signing messages requires the use of a Wallet application. 
   These applications are often specific to one or a few chains.
3. **Token availability**: \
   Allocating resources on the aleph.im network relies on a fungible onchain token.
   Exchanging that token on a blockchain requires that token to be available on that chain first. 
4. **Balance support** \
   The aleph.im network needs to be aware of user's tokens on each supported chain in order to allow
   users to allocate resources on the network.
5. **Staking support**: \
   Users can help securing the aleph.im network by holding tokens and _staking_ them on 
   [Core Channel Nodes](../nodes/core/index.md) they consider trustworthy. The aleph.im network
   interacts with blockchains to achieve this mechanism.


| Chain     | Symbol | Message signature | Wallet support | Token availability | Balance support | Staking support |
|-----------|--------|-------------------|----------------|--------------------|-----------------|-----------------|
| Ethereum  | ETH    | ✅                 | Metamask       | ✅                  | ✅               | ✅               |
| Polygon   |        | ✅                 | Metamask       |                    |                 |                 |
| Solana    | Sol    | ✅                 |                |                    | ❌               | ❌               |
| Tezos     |        | ✅                 |                |                    |                 |                 |
| Cosmos    |        | ✅                 |                |                    |                 |                 |
| Nuls1     |        | Python only       |                |                    |                 |                 |
| Nuls2     |        | Python only       |                |                    |                 |                 |
| Substrate |        | ✅                 |                |                    |                 |                 |
| Avalanche |        | TypeScript only   |                |                    |                 |                 |
