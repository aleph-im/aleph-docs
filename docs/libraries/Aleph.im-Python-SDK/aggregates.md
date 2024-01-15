# Aggregates

Aggregates are a key-value store specific to an account.
Each time a new aggregate message is received for a specific account, the
nodes update the aggregate for this account.

Like a dictionary update, if a key already exists, it is updated,
otherwise it is created.

## Query aggregate of an account

To query keys from an account aggregate, you need to call the
`fetch_aggregate` function on the client.

Since version 0.8.0, only the asynchronous methods are available.

As per usual, use `asyncio.run` to run the asynchronous code:

```python
import asyncio
from aleph.sdk.client import AlephHttpClient

async def main():
    async with AlephHttpClient() as client:
        aggregate = await client.fetch_aggregate(
            "0x06DE0C46884EbFF46558Cd1a9e7DA6B1c3E9D0a8",
            "profile",
        )
        print(aggregate)

if __name__ == "__main__":
    asyncio.run(main())
```
outputs:
```json
{"bio": "tester", "name": "Moshe on Ethereum"}
```

## Mutate aggregate
To mutate an aggregate you need to call the create_aggregate function (it will
create an AGGREGATE type message for you and submit it).

You need a valid account and instantiate an authenticated client:

```python
from aleph.sdk.chains.ethereum import get_fallback_account
from aleph.sdk.client import AuthenticatedAlephHttpClient

async def main():
    account = get_fallback_account()
    async with AuthenticatedAlephHttpClient(account) as client:
        message, status = await client.create_aggregate(
            "profile",
            {"bio": "tester", "name": "Moshe on Ethereum"},
        )
        print(message.content)
```
outputs:
```json
{
    "key": "profile",
    "content": {"bio": "tester", "name": "Moshe on Ethereum"},
    "address": "0x...",
    "time": 1689081614.4252806
}
```

## Delegate write access to an aggregate key

If you want to set an aggregate on another address than the one of your
account, this address should have something similar to this in its
"security" key:

```python
async with AuthenticatedAlephHttpClient(account) as client:
    aggregate = await client.fetch_aggregate('YOUR_ADDRESS', 'security')
    print(aggregate)
```
outputs:
```json
{
    "authorizations": [
        {
            "address": "TARGET_ADDRESS",
            "types": ["AGGREGATE"],
            "aggregate_keys": ["testkey"]
        }
    ]
}
```
The owner of `TARGET_ADDRESS` can then set content of the `testkey` key of
`YOUR_ADDRESS`'s aggregate:

```python
async with AuthenticatedAlephHttpClient(account) as client:
    # Assuming 'account' is TARGET_ADDRESS
    message, status = await client.create_aggregate(
        "testkey",
        {"access": "alien"},
        address="YOUR_ADDRESS",
    )
    print(message.content)
```
outputs:
```json
{
    "key": "testkey",
    "content": {"access": "alien"},
    "address": "TARGET_ADDRESS",
    "time": 1689081614.4252806
}
```
`AggregateMessage.content.address` tracks who posted this change to your aggregate.
This way you can audit the trail of changes to the aggregate.

!!! note

    For more information on the authorizations model, see the [permissions section](../../protocol/permissions.md).
    For more general information on messages and their types, see the [messages section](../../protocol/messages.md).




