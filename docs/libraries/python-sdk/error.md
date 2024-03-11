Using `get_message_error()` will show you the error code and some details about an error message.

!!!note

    It will return `None` if everything went well. In this case, use `get_message()` to get more information if needed.

## Usage

```python
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
