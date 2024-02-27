Deleting messages on aleph.im uses special FORGET messages. These messages are
sent to the network, and are then propagated to all nodes. Once a node receives
a FORGET message, it will delete the message from its database.

To delete any kind of messages (post, aggregate, ...), you must send a FORGET message to the network, with the hash
of the post you want to delete. You may also forget multiple posts at a time.

## Usage

```python
async def forget(
        self,
        hashes: List[str],
        reason: Optional[str],
        storage_engine: StorageEnum = StorageEnum.storage,
        channel: Optional[str] = None,
        address: Optional[str] = None,
        sync: bool = False,
    ) -> Tuple[AlephMessage, MessageStatus]:
```

### Arguments

#### Required arguments

| Parameter        | Description                                                        |
|------------------|--------------------------------------------------------------------|
| `hashes`         | The hashes of the messages to forget. Can put several hashes here. |
| `reason`         | The reason for forgetting the message.                             |
| `storage_engine` | The storage engine to use. `ipfs` or `storage`                     |

#### Optional arguments

| Parameter | Description                                                                           |
|-----------|---------------------------------------------------------------------------------------|
| `channel` | The channel of the message. If not provided, the default channel will be used.        |
| `address` | The address of the message. If not provided, the address of the account will be used. |
| `sync`    | Wait for a confirmation from the API in a blocking manner.                            |

### Example

Here is a simple example of how to use the `forget` for a post:

```python
from aleph.sdk.chains.ethereum import get_fallback_account
from aleph.sdk.client import AuthenticatedAlephHttpClient
import ssl
import certifi

ssl_context = ssl.create_default_context(cafile=certifi.where())
async def main():
    account = get_fallback_account()
    async with AuthenticatedAlephHttpClient(account, ssl_context=ssl_context) as client:
        message, status = await client.forget(
            hashes=["f02cd3ae058ff144f633ae87942e34f9352698ebd3a25bdb1de44b682427c98b"],
            reason="I don't like this post",
            channel="MY_CHANNEL",
            sync=True,
        )
        return message, status

import asyncio
message, status = asyncio.run(main())
print(message.content)
```

output:

```
address='0x...' time=1709029093.1242812 hashes=[<ItemHash value='f02cd3ae058ff144f633ae87942e34f9352698ebd3a25bdb1de44b682427c98b' item_type=<ItemType.storage: 'storage'>>] aggregates=[] reason="I don't like this post"
```

!!! note
    More information in the [deleting message section](../../../../protocol/messages/#deleting-messages).