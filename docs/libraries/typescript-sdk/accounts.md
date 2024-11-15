# Accounts

To send data to the aleph.im network, you need to have an account.
This account can be made using any of the supported wallet providers.

## Supported chains
- [Ethereum (and all EVM compatible chains)](https://npmjs.com/package/@aleph-sdk/ethereum)
- [Avalanche](https://npmjs.com/package/@aleph-sdk/avalanche)
- [Solana](https://npmjs.com/package/@aleph-sdk/solana)
- [Polkadot / Substrate](https://npmjs.com/package/@aleph-sdk/substrate)
- [NULS 2](https://npmjs.com/package/@aleph-sdk/nuls2)
- [Tezos](https://npmjs.com/package/@aleph-sdk/tezos)
- [Cosmos / Tendermint](https://npmjs.com/package/@aleph-sdk/cosmos)

## Usage

Chains provide a `newAccount` function for testing purposes. Example using Ethereum:

```typescript
import { newAccount } from '@aleph-sdk/ethereum';

const { account } = newAccount();
```

### Browser wallets
Most chains allow you to retrieve an account from a browser based wallet (ex: Metamask).

```typescript
import { getAccountFromProvider } from '@aleph-sdk/ethereum';

const account = getAccountFromProvider(window.ethereum);
```

### Node.js/Server wallets
You can also retrieve an account from a private key or mnemonic (or generate one on the fly) like this:

```typescript
import { importAccountFromPrivateKey } from '@aleph-sdk/ethereum';

// just an example, DO NOT USE THIS private key!
account = importAccountFromPrivateKey("0x0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef0");
```

### Streaming payments (Superfluid)

In January 2024, the network started supporting a new payment model, together with the launch of the [TwentySix Cloud](https://www.twentysix.cloud/) platform, where users pay using streams of ALEPH tokens on compatible chains.

```typescript
import { getAccountFromProvider } from '@aleph-sdk/superfluid';

const account = getAccountFromProvider(window.ethereum);

// initialize the wallet
await account.init();

// increase a flow (in ALEPH/hour)
const receiver = "0x1234567890123456789012345678901234567890";
account.increaseALEPHFlow(receiver, 1);

// get the net flow of ALEPH/hour
const flow = account.getALEPHFlow();
```