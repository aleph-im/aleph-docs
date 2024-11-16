# Aggregates

Aggregates are a key-value store specific to an account.
Each time a new aggregate message is received for a specific account, the
nodes update the aggregate for this account.

Like a dictionary update, if a key already exists, it is updated,
otherwise it is created.

## Query aggregate of an account

To query keys from an account aggregate, you need to call the
`fetchAggregate` function on the client.

```typescript
import { AlephHttpClient } from '@aleph-sdk/client';

const client = new AlephHttpClient();
const profileData = await client.fetchAggregate("0x06DE0C46884EbFF46558Cd1a9e7DA6B1c3E9D0a8", "profile");
console.log(profileData);
```
outputs:
```json
{"bio": "tester", "name": "Moshe on Ethereum"}
```

## Mutate aggregate
To mutate an aggregate you need to call the create_aggregate function (it will
create an AGGREGATE type message for you and submit it).

You need a valid account and instantiate an authenticated client:

```typescript
import { AuthenticatedAlephHttpClient } from '@aleph-sdk/client';
import * as ethereum from '@aleph-sdk/ethereum';

const { account } = ethereum.newAccount();
const client = new AuthenticatedAlephHttpClient(account);
```

Then you can create a new aggregate message:

```typescript
const message = await client.createAggregate({
    key: "profile",
    content: {"bio": "tester", "name": "Moshe on Ethereum"},
});

console.log(message.content);
```
outputs:
```json
{
    "key": "profile",
    "content": {"bio": "tester", "name": "Moshe on Ethereum"},
    "address": "0x...",
    "time": 1234567890.123456
}
```

## Delegate write access to another account

If you want to delegate write access to a specific key in your aggregates, you can
use the security aggregate like explained in the [Python SDK's section on write access delegation](../python-sdk/aggregates/delegate.md).