# Posts

Posts are unique data entries, that can be amended later on. For example:

- Events
- Blog posts
- Comments
- and even be used to emulate a [public database](https://github.com/aleph-im/active-record-sdk)

## Getting posts

To get posts you have two options, either use the `get_posts` function, and get
the posts in their amended state, or use `get_message` and only get the unique POST
messages at the time of the call.

Since version 0.8.0, `get_posts` uses a PostFilter object to specify the filters:

```python
from aleph.sdk.client import AlephHttpClient
from aleph.sdk.query.filters import PostFilter

async def main():
    async with AlephHttpClient() as client:
        posts, status = await client.get_posts(
            post_filter=PostFilter(channels=["MY_CHANNEL"])
        )
        print(posts)
```
outputs something akin to:
```json
{
    "posts": [...],
    "pagination_page": 1,
    "pagination_total": 1337,
    "pagination_per_page": 20,
    "pagination_item": "posts"
}
```


# Creating a post

Creating a post is as simple as calling the `create_post` function on the client.

```python
from aleph.sdk.chains.sol import get_fallback_account
from aleph.sdk.client import AuthenticatedAlephHttpClient

async def main():
    account = get_fallback_account()
    async with AuthenticatedAlephHttpClient(account) as client:
        message, status = await client.create_post(
            {"hello": "world"},
            post_type="testtype",
            channel="MY_CHANNEL",
        )
        print(message)
```
outputs:
```json
{
    "chain": "SOL",
    "channel": "MY_CHANNEL",
    "sender": "21hKNCB7xmDZ1pgteuJPbhKN1aDvsvPJRJ5Q95G5gyCW",
    "type": "POST",
    "time": "2023-07-11T13:20:14.604485+00:00",
    "item_type": "inline",
    "item_content": "{\"type\":\"testtype\",\"address\":\"21hKNCB7xmDZ1pgteuJPbhKN1aDvsvPJRJ5Q95G5gyCW\",\"content\":{\"hello\":\"world\"},\"time\":1573570575.2818618}",
    "content": {
        "type": "testtype",
        "address": "21hKNCB7xmDZ1pgteuJPbhKN1aDvsvPJRJ5Q95G5gyCW",
        "content": {
            "hello": "world"
        },
        "time": 1573570575.2818618
    },
    "size": 130,
    "item_hash": "02afdbf33ff2c6ddb46349298a4598a8801cec61dbaa8f3a17ba9d1ad6dd8cb1",
    "signature": "G7yJjMCPgvX04Dd9rsz0oEuuRFa4PfuKAMOPA3Oblf6vd5YA1x15jvWLL2WycnnzYLEl0usjTiVxBl530ZOmYgw="
}
```

# Amending a post

Amending is similar to creating a new post, but with two differences:

- The `post_type` must be "amend"
- When calling `create_post`, you must pass the hash of the post you want to amend as `ref`

Example:

```python
from aleph.sdk.chains.sol import get_fallback_account
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
        print(message.content)
```
outputs:
```json
{
    "type": "amend",
    "address": "21hKNCB7xmDZ1pgteuJPbhKN1aDvsvPJRJ5Q95G5gyCW",
    "content": {
        "hello": "aleph"
    },
    "time": 1573570575.2818618,
    "ref": "02afdbf33ff2c6ddb46349298a4598a8801cec61dbaa8f3a17ba9d1ad6dd8cb1"
}
```

# Deleting a post

Deleting messages on aleph.im uses special FORGET messages. These messages are
sent to the network, and are then propagated to all nodes. Once a node receives
a FORGET message, it will delete the message from its database.

To delete a post, you must send a FORGET message to the network, with the hash
of the post you want to delete. You may also forget multiple posts at a time.

```python
from aleph.sdk.chains.sol import get_fallback_account
from aleph.sdk.client import AuthenticatedAlephHttpClient

async def main():
    account = get_fallback_account()
    async with AuthenticatedAlephHttpClient(account) as client:
        message, status = await client.forget(
            hashes=["02afdbf33ff2c6ddb46349298a4598a8801cec61dbaa8f3a17ba9d1ad6dd8cb1"],
            reason="I don't like this post",
            channel="MY_CHANNEL",
        )
        print(message.content)
```

!!! note
    More information on posts and messages in general can be found in the
    [protocol section](../../protocol/messages.md).
