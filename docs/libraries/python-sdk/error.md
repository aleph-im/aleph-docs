Using `get_message_error()` will show you the error code and some details about an error message.

!!!note

    It will return `None` if everything went well. In this case, use `get_message()` to get more information if needed.

## Usage

```py
async def get_message_error(
        self,
        item_hash: str,
    ) -> Optional[Dict[str, Any]]:
```

### Arguments

| Parameter   | Description                           |
|-------------|---------------------------------------|
| `item_hash` | The hash of the message to retrieve.  |

## Example

```python
from aleph.sdk.client import AlephHttpClient

async def main():
    async with AlephHttpClient() as client:
        message = await client.get_message_error(
            "09bd7c17a79a2e9e9d80e1d680d98fc02382f60b7fee5767817d846650ac5e4b"
        )
        return message

import asyncio
message = asyncio.run(main())
print(message)
```

output:

```
{'error_code': 101, 'details': None}
```

---

For the example above, I tried to amend a post using a wrong reference:
```python
from aleph.sdk.chains.ethereum import get_fallback_account
from aleph.sdk.client import AuthenticatedAlephHttpClient
import asyncio

async def main():
    account = get_fallback_account()
    async with AuthenticatedAlephHttpClient(account) as client:
        message, status = await client.create_post(
            {"hello": "world"},
            post_type="amend",
            channel="MY_CHANNEL",
            ref="Test"
        )
        return message, status

message, status = asyncio.run(main())
```

## Error Codes

Here is a list of error codes and their meanings:

| Error Code | Error Description                                                                                |
|------------|--------------------------------------------------------------------------------------------------|
| -1         | **Internal error**: *An unexpected internal error occurred*.                                     |
| 0          | **Invalid format**: *The data format provided is invalid*.                                       |
| 1          | **Invalid signature**: *The signature provided is invalid*.                                      |
| 2          | **Permission denied**: *Access to the resource is denied*.                                       |
| 3          | **Content unavailable**: *The requested content is not available*.                               |
| 4          | **File unavailable**: *The requested file is not available*.                                     |
| 5          | **Balance insufficient**: *The account balance is too low for the operation*.                    |
| 100        | **No target for the post amend**: *Target post for amendment not specified*.                     |
| 101        | **Target not found for the post amend**: *Specified target post not found*.                      |
| 102        | **Trying to amend an amend post**: *Amending an already amended post is not allowed*.            |
| 200        | **Store reference not found**: *Reference to the store not found*.                               |
| 201        | **Updating a store update**: *Attempting to update an already updated store*.                    |
| 300        | **VM reference not found**: *Reference to the virtual machine not found*.                        |
| 301        | **VM volume not found**: *Specified volume for the virtual machine not found*.                   |
| 302        | **VM amend not allowed**: *Amending the virtual machine is not allowed*.                         |
| 303        | **Updating a VM update**: *Attempting to update an already updated virtual machine*.             |
| 304        | **VM volume too small**: *Specified volume for the virtual machine is too small*.                |
| 500        | **No target for the forget message**: *Target message for forgetting not specified*.             |
| 501        | **Target not found for the forget message**: *Specified target message not found*.               |
| 502        | **Trying to forget a forget message**: *Forgetting an already forgotten message is not allowed*. |

!!! notes

    Fore more information, see the [pyaleph message status](https://github.com/aleph-im/pyaleph/blob/main/src/aleph/types/message_status.py#L28) section.
