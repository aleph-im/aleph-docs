# Managing instances

## Creating an instance

To create an instance, you need to have an account with enough ALEPH tokens to pay for the instance creation.

You can either choose to lock ALEPH tokens on the Ethereum network, or ALEPH payment streams on Avalanche.

### Pay by holding/locking ALEPH tokens

```typescript
import { newAccount } from '@aleph-sdk/ethereum';
import { authenticatedAlephHttpClient } from '@aleph-sdk/client';

const account = newAccount();
const client = authenticatedAlephHttpClient(account);

const instance = await client.createInstance({
    name: "My instance",
    description: "This is my first instance",
    chain: "ethereum",
    payment: {
        type: "hold",
        amount: 1000,
    },
});
```

### Pay by ALEPH payment streams

For this, two steps are required in this order:
- First, create a payment stream on Avalanche with Superfluid
- Then create the instance message

Currently, this is only supported in a browser environment.

#### Interlude: Fetching Core Channel & Compute Resource Nodes

Before creating the payment stream, you need a valid CRN stream reward address.
You can fetch this information from the Core Channel aggregate of the official node status account:

```typescript
import { alephHttpClient } from '@aleph-sdk/client';

const client = alephHttpClient();
const nodesAggregateAddress = "0xa1B3bb7d2332383D96b7796B908fB7f7F3c2Be10";
const aggregateKey = "corechannel";

const corechannel = await client.fetchAggregate(nodesAggregateAddress, aggregateKey);
const resourceNodes = corechannel["resource_nodes"];

// Select a fitting node to create the payment stream
const node = resourceNodes[0];
const streamRewardAddress = node["stream_reward"];
```

This info can also be retrieved using the aleph.im CLI:

```shell
#### Create a payment stream

```typescript
import { authenticatedAlephHttpClient } from '@aleph-sdk/client';
import { getAccountFromProvider } from '@aleph-sdk/superfluid';

const account = await getAccountFromProvider(window.ethereum);
const client = authenticatedAlephHttpClient(account);
account.increaseALEPHFlow();