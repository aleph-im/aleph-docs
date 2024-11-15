# Posts

Posts are unique data entries, that can be amended later on. For example:

- Events
- Blog posts
- Comments
- and even be used to emulate a [public database](https://github.com/aleph-im/active-record-sdk)

## Getting posts

To get posts you have two options, either use the `getPosts` function, and get
the posts in their amended state, or use `getMessage` and only get the unique POST
messages at the time of the call.

```typescript
import { AlephHttpClient } from '@aleph-sdk/client';

const client = new AlephHttpClient();
const posts = await client.getPosts({ channels: ["MY_CHANNEL"] });
console.log(posts);
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

Creating a post is as simple as calling the `createPost` function on the client.

```typescript
import { newAccount } from '@aleph-sdk/ethereum';
import { AuthenticatedAlephHttpClient } from '@aleph-sdk/client';

const { account } = newAccount();
const client = new AuthenticatedAlephHttpClient(account);
const message = await client.createPost({
    content: { hello: "world" },
    postType: "testtype",
    channel: "MY_CHANNEL",
});
console.log(message);
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

- The `postType` must be "amend"
- When calling `createPost`, you must pass the hash of the post you want to amend as `ref`

Example:

```typescript
import { newAccount } from '@aleph-sdk/ethereum';
import { AuthenticatedAlephHttpClient } from '@aleph-sdk/client';

const { account } = newAccount();
const client = new AuthenticatedAlephHttpClient(account);
const message = await client.createPost({
    content: { hello: "aleph" },
    postType: "amend",
    ref: "02afdbf33ff2c6ddb46349298a4598a8801cec61dbaa8f3a17ba9d1ad6dd8cb1",
    channel: "MY_CHANNEL",
});
console.log(message);
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

```typescript
import { newAccount } from '@aleph-sdk/ethereum';
import { AuthenticatedAlephHttpClient } from '@aleph-sdk/client';

const { account } = newAccount();
const client = new AuthenticatedAlephHttpClient(account);
const message = await client.forget({
    hashes: ["02afdbf33ff2c6ddb46349298a4598a8801cec61dbaa8f3a17ba9d1ad6dd8cb1"],
    reason: "I don't like this post",
    channel: "MY_CHANNEL",
});
```

!!! note

    More information on posts and messages in general can be found in the
    [protocol section](../../protocol/messages.md).
