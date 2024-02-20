## Delegate write access to an aggregate key

In certain contexts, you may want to allow another account to update your aggregate. </br>
This can be done by creating a [security key](./security_key.md)

## Usage

### Prerequisites

First you need to [create an aggregate](./create_aggregate.md) to your own address. </br>
Then [create a security key](./security_key.md) for the account you want to delegate write access to. </br>
After that, you will be able to delegate write access to another account.

### Example

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

    For more information on the authorizations model, see the [permissions section](../../../protocol/permissions.md).
    For more general information on messages and their types, see the [messages section](../../../protocol/messages.md).
