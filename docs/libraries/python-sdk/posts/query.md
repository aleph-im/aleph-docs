To get posts you have two options:

- [get_posts](#get_posts) to get the posts in their amended state.
- [get_message](#get_message) to only get the unique POST messages at the time of the call.

# get_posts

Since version 0.8.0, `get_posts` uses a PostFilter object to specify the filters:

## Usage

```py
async def get_posts(
        self,
        page_size: int = DEFAULT_PAGE_SIZE, # Default is 200
        page: int = 1, # Default is 1
        post_filter: Optional[PostFilter] = None,
        ignore_invalid_messages: Optional[bool] = True,
        invalid_messages_log_level: Optional[int] = logging.NOTSET,
) -> PostsResponse:
```

### Arguments

#### Required arguments

| Parameter   | Description                             |
|-------------|-----------------------------------------|
| `page_size` | The number of posts to return per page. |
| `page`      | The page number to return.              |

#### Optional arguments

| Parameter                    | Description                                 |
|------------------------------|---------------------------------------------|
| `post_filter`                | A PostFilter object to specify the filters. |
| `ignore_invalid_messages`    | If True, invalid messages will be ignored.  |
| `invalid_messages_log_level` | The log level to use for invalid messages.  |

### Example

```python
from aleph.sdk.client import AlephHttpClient
from aleph.sdk.query.filters import PostFilter

async def main():
    async with AlephHttpClient() as client:
        posts = await client.get_posts(
            post_filter=PostFilter(channels=["MY_CHANNEL"])
        )
        return posts

import asyncio
posts = asyncio.run(main())
print(posts)
```

outputs something akin to:

```
"pagination_page": 1,
"pagination_total": 26,
"pagination_per_page": 200,
"pagination_item": "posts",
"posts": [...] -- The list of every posts
```

# get_message

## Usage

```py
async def get_message(
        self,
        item_hash: str,
        message_type: Optional[Type[GenericMessage]] = None,
) -> GenericMessage:
```

### Arguments

#### Required arguments

| Parameter     | Description                           |
|---------------|---------------------------------------|
| `item_hash`   | The hash of the message to retrieve.  |

#### Optional arguments

| Parameter       | Description                      |
|-----------------|----------------------------------|
| `message_type`  | The type of message to retrieve. |

### Example

```python
from aleph.sdk.client import AlephHttpClient
from aleph_message.models import PostMessage
from pprint import pprint

async def main():
    async with AlephHttpClient() as client:
        message = await client.get_message(
            "1b68afb5b5229a4b209d30769cb5286de38c321d9a5e29a22d9a4bc692f1b9c3",
            message_type=PostMessage
        )
        return message

import asyncio
message = asyncio.run(main())
pprint(message.content.dict())
```

outputs:

```
 {'address': '0xbC80BeEcBd67549E70cb1C729e903818E6370D37',
 'content': {'hello': 'world'},
 'ref': None,
 'time': 1709626034.404321,
 'type': 'testtype'}
```
