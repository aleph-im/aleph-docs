In certain contexts, you may want to allow another account to update your aggregate. </br>
This can be done by with the security key

!!! note
    This section will give an example of how to create a security key.
    <br>More information about the security key in the [permissions section](../../../protocol/permissions.md#the-security-aggregate).

## Create a security key

```py
from aleph.sdk.chains.ethereum import get_fallback_account
from aleph.sdk.client import AuthenticatedAlephHttpClient

TARGET_ADDRESS = ...  # Put the target address here
assert TARGET_ADDRESS is not ..., "The target address was not specified"

async def main(target_address: str):
    account = get_fallback_account()
    async with AuthenticatedAlephHttpClient(account) as client:
        message, status = await client.create_aggregate(
            "security",
            {
                "authorizations": [
                    {
                        "address": target_address,
                    }
                ]
            },
            sync=True,
        )
        return message, status
import asyncio
message, status = asyncio.run(main(TARGET_ADDRESS))
```

> Don't forget to replace `TARGET_ADDRESS` with the address you want to delegate to.

At this moment, `TARGET_ADDRESS` should be able to update your aggregate by using [create_aggregate](./create.md) with the delegated account.

You can verify this by fetching the security aggregate:

```py
from aleph.sdk.client import AlephHttpClient
import asyncio

MY_ADDRESS = ...  # Put your address here.
assert MY_ADDRESS is not ..., "The address was not specified"

async def main(my_address: str):
    async with AlephHttpClient() as client:
        aggregate = await client.fetch_aggregate(
            my_address,
            "security"
        )
        return aggregate

aggregate = asyncio.run(main(MY_ADDRESS))
print(aggregate)
```

outputs:

```
{"authorizations": [{"address": "TARGET_ADDRESS"}]}

```

`AggregateMessage.content.address` tracks who posted this change to your aggregate.
This way you can audit the trail of changes to the aggregate.

!!! note

    For more information on the authorizations model, see the [permissions section](../../../protocol/permissions.md).
    For more general information on messages and their types, see the [messages section](../../../protocol/messages.md).
