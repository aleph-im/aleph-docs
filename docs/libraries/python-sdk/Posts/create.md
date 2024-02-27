Creating a post by calling `create_post()` function on the client.

Call this same function if you want to update / amend a post. see [below](#update-amending-a-post) for more information.

## Usage

```python
async def create_post(
        self,
        post_content,
        post_type: str,
        ref: Optional[str] = None,
        address: Optional[str] = None,
        channel: Optional[str] = None,
        inline: bool = True,
        storage_engine: StorageEnum = StorageEnum.storage,
        sync: bool = False,
) -> Tuple[PostMessage, MessageStatus]:
```

### Arguments

#### Required arguments

| Parameter      | Description                                                                                                        |
|----------------|--------------------------------------------------------------------------------------------------------------------|
| `post_content` | The data to store as a dictionary.<br> [More information](../../../../protocol/object_types/posts/#content-format) |
| `post_type`    | An arbitrary content type that helps to describe the post_content. <br> ex: `ammend` / `blog` / `chat` `comment`.  |

#### Optional arguments

| Parameter        | Description                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ref`            | A searchable reference string of your choice to save to the `item_content.ref`. Can be the reference to another post, an address, transaction hash, etc. <br> Mostly used with the `ammend` post_type. |
| `address`        | Address the Post should be associated with or the address that submitted the Post.                                                                                                                     |
| `channel`        | The channel where the message will be posted.                                                                                                                                                          |
| `inline`         | Flag to indicate if the content should be inlined in the message or not.                                                                                                                               |
| `storage_engine` | The storage engine to use. `ipfs` or `storage`.                                                                                                                                                        |
| `sync`           | Wait for a confirmation from the API in a blocking manner.                                                                                                                                             |

### Example

```python
from aleph.sdk.chains.ethereum import get_fallback_account
from aleph.sdk.client import AuthenticatedAlephHttpClient

async def main():
    account = get_fallback_account()
    async with AuthenticatedAlephHttpClient(account) as client:
        message, status = await client.create_post(
            {"hello": "world"},
            post_type="testtype",
            channel="MY_CHANNEL",
        )
        return message, status

import asyncio
message, status = asyncio.run(main())
print(message.content)
```

outputs:
```
address='0x...' time=1709023369.209453 content={'hello': 'world'} ref=None type='testtype'
```

## Update / amending a post

Amending is similar to creating a new post, but with two differences:

- The `post_type` must be "amend"
- When calling `create_post`, you must pass the hash of the post you want to amend as `ref`

Example:

```python
from aleph.sdk.chains.ethereum import get_fallback_account
from aleph.sdk.client import AuthenticatedAlephHttpClient

async def main():
    account = get_fallback_account()
    async with AuthenticatedAlephHttpClient(account) as client:
        message, status = await client.create_post(
            {"hello": "aleph"},
            post_type="amend",
            ref="02afdbf33ff2c6ddb46349298a4598a8801cec61dbaa8f3a17ba9d1ad6dd8cb1",
            channel="MY_CHANNEL",
        )
        return message, status

import asyncio
message, status = asyncio.run(main())
print(message.content)
```

outputs:
```
address='0xbC80BeEcBd67549E70cb1C729e903818E6370D37' time=1709025582.8660538 content={'hello': 'aleph'} ref='02afdbf33ff2c6ddb46349298a4598a8801cec61dbaa8f3a17ba9d1ad6dd8cb1' type='amend'
```
