# Create

An [aggregate](../../../protocol/object-types/aggregates.md) is a form of key-value store on the distributed  using `AuthenticatedAlephHttpClient.create_aggregate` as described below.
aleph.im database.

Initialize an `AuthenticatedAlephHttpClient` with an [account](../accounts.md) to write to aleph.im.

!!! note
    Since creating an Aggregate message mutates the value of the specific key,
    if the key exists, the value object will be updated (mutated) with the object you are saving. <br>
    <br> An exemple is given at the end of this page.

## Usage

```py
class AuthenticatedAlephHttpClient:
    ...
    async def create_aggregate(
        self,
        key: str,
        content: Mapping[str, Any],
        address: Optional[str] = None,
        channel: Optional[str] = None,
        inline: bool = True,
        sync: bool = False,
    ) -> Tuple[AlephMessage, MessageStatus]:
```

### Arguments

#### Required arguments

| Parameter | Description                                                                                                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------|
| `key`     | An identifier you define for this aggregate                                                                           |
| `content` | The data to store as a dictionary<br> [More information](../../../protocol/object-types/aggregates.md#content-format) |

#### Optional arguments

| Parameter | Description                                                                             |
|-----------|-----------------------------------------------------------------------------------------|
| `address` | The address of the aggregate. If not provided, the address of the account will be used. |
| `channel` | The channel of the aggregate. If not provided, the default channel will be used.        |
| `inline`  | Store the data in the message itself and not as attachment                              |
| `sync`    | Wait for a confirmation from the API in a blocking manner. See [message status](../     |


### Example

Here is a simple example of how to use the `create_aggregate` function:

```python
from aleph.sdk.chains.ethereum import get_fallback_account
from aleph.sdk.client import AuthenticatedAlephHttpClient

async def main():
    account = get_fallback_account()
    async with AuthenticatedAlephHttpClient(account) as client:
        message, status = await client.create_aggregate(
            "profile",
            {"bio": "tester", "name": "MY_NAME on Ethereum"},
            sync=True,
        )
        return message, status
        
import asyncio
message, status = asyncio.run(main())
```

### Output

`message.content`
```json
address='0x...' time=1708620733.752511 key='profile' content={'bio': 'tester', 'name': 'MY_NAME on Ethereum'}
```

## Update / mutate an aggregate

As we said before, calling `create_aggregate()` function with an **existing key** with<br>the **same account** or **a [message delegate](./delegate.md)** to your account will update the content of the aggregate.

```python
from aleph.sdk.chains.ethereum import get_fallback_account
from aleph.sdk.client import AuthenticatedAlephHttpClient

async def main():
    account = get_fallback_account()
    async with AuthenticatedAlephHttpClient(account) as client:
        message, status = await client.create_aggregate(
            "profile",
            {"bio": "Modify", "name": "modify on Ethereum"},
            sync=True,)
        return message, status

import asyncio
message, status = asyncio.run(main())
```

`message.content`
outputs:

```json
address='0x...' time=1708620771.7611551 key='profile' content={'bio': 'Modify', 'name': 'modify on Ethereum'}
```