# Managing instances

## Creating an instance

To create an instance, you need to have an account with enough ALEPH tokens to pay for the instance creation.

You can either choose to lock ALEPH tokens on the Ethereum network, or ALEPH payment streams on Avalanche.

### Retrieve your SSH key

Without an SSH key, you won't be able to dial into your instance.
On ubuntu and similar linux distros, you can retrieve it using the following command:

```shell
cat ~/.ssh/id_rsa.pub
```

### Generate an SSH key

If you don't have an SSH key, you can generate one using the following command:

```shell
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

Follow the instructions and save your keypair in the default location.
You may then add this SSH key to your SSH agent using the following command:

```shell
ssh-add ~/.ssh/id_rsa
```

### Pay by holding/locking ALEPH tokens

Aleph.im offers two ways to pay for instances: by holding ALEPH tokens on the Ethereum network, or by using ALEPH payment streams on Avalanche.
In this example, we will reserve ALEPH tokens by signing an aleph.im message.

- This will not cost any gas fees, nor will it prevent you from using your ALEPH tokens for other purposes.
- If your account ceases to hold enough ALEPH tokens, your instance will be stopped.

```typescript
import { newAccount } from '@aleph-sdk/ethereum';
import { authenticatedAlephHttpClient } from '@aleph-sdk/client';

const { account } = newAccount();
const client = authenticatedAlephHttpClient(account);
// You need an SSH key to connect to the instance
const sshKey = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC3...";

const instance = await client.createInstance({
    authorized_keys: [sshKey],
    resources: {
      vcpus: 1,
      memory: 2000,
    },
    payment: {
        chain: "ETH",
        type: "hold",
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
This reward address allows you to select a node to run your instance on.

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

This address can also be retrieved using the [aleph.im CLI](../../tools/aleph-client/usage.md#aleph-node-compute).

#### Create a payment stream

This example runs in your browser. You need to have an Ethereum wallet connected to the Avalanche network.

The user will first need to sign the Superfluid transaction to transfer ALEPH tokens on their behalf. This will cost additional AVAX.
Then they will sign the aleph.im message for free to create the instance:

```typescript
import { authenticatedAlephHttpClient } from '@aleph-sdk/client';
import { getAccountFromProvider } from '@aleph-sdk/superfluid';

const account = await getAccountFromProvider(window.ethereum);
const client = authenticatedAlephHttpClient(account);
// 0.88 ALEPH per hour = 8 Compute Units = 8 vCPUs + 16 GB RAM + 100 GB storage
await account.increaseALEPHFlow(streamRewardAddress, 0.88);
await client.createInstance({
    authorized_keys: [sshKey],
    resources: {
      vcpus: 8,
      memory: 16000,
    },
    payment: {
        chain: "AVAX",
        type: "superfluid",
        receiver: streamRewardAddress,
    },
});
```