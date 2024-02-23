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