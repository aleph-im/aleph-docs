To get posts you have two options:

- [get_posts](#get_posts) to get the posts in their amended state.
- [get_message](#get_message) to only get the unique POST messages at the time of the call.

# get_posts

Since version 0.8.0, `get_posts` uses a PostFilter object to specify the filters:

## Usage

```python
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

```python
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

async def main():
    async with AlephHttpClient() as client:
        message = await client.get_message(
            "142f99fbbe63befc868d16a4e389395cd1abc812b0eecaba72e08b8709caafd6"
        )
        return message

import asyncio
message = asyncio.run(main())
print(message.content)
```

outputs:

```
address='0x...' time=1709026357.038 content={'body': [{'appId': '0', 'chain': 'mumbai', 'payment': [{'payment': {'fee': 0, 'name': 'Standard', 'owner': '0x...', 'periodType': 'MONTH', 'limitPeriod': 6, 'loadingTime': 5, 'paymentType': 0, 'trialPeriod': 0, 'paymentTokens': [{'price': '10000000', 'token': '0x...', 'firstAmount': '0'}, {'price': '10000000000000000000', 'token': '0x...', 'firstAmount': '0'}]}, 'paymentId': '0x...'}, {'payment': {'fee': 0, 'name': 'Premium', 'owner': '0x...', 'periodType': 'YEAR', 'limitPeriod': 1, 'loadingTime': 10, 'paymentType': 0, 'trialPeriod': 0, 'paymentTokens': [{'price': '250000000', 'token': '0x...', 'firstAmount': '0'}, {'price': '250000000000000000000', 'token': '0x...', 'firstAmount': '0'}]}, 'paymentId': '0x...'}]}, {'appId': '1', 'chain': 'mumbai', 'payment': [{'payment': {'fee': 0, 'name': 'Standard', 'owner': '0x...', 'periodType': 'MONTH', 'limitPeriod': 6, 'loadingTime': 5, 'paymentType': 0, 'trialPeriod': 0, 'paymentTokens': [{'price': '20000000', 'token': '0x...', 'firstAmount': '0'}, {'price': '17000000000000000000', 'token': '0x...', 'firstAmount': '0'}]}, 'paymentId': '0x...'}, {'payment': {'fee': 0, 'name': 'Premium', 'owner': '0x...', 'periodType': 'YEAR', 'limitPeriod': 1, 'loadingTime': 1, 'paymentType': 0, 'trialPeriod': 0, 'paymentTokens': [{'price': '1200000000000000000000', 'token': '0x...', 'firstAmount': '0'}]}, 'paymentId': '0x...'}]}, {'appId': '2', 'chain': 'mumbai', 'payment': [{'payment': {'fee': 0, 'name': 'Check', 'owner': '0x...', 'periodType': 'ONETIME', 'limitPeriod': 1, 'loadingTime': 0, 'paymentType': 0, 'trialPeriod': 0, 'paymentTokens': [{'price': '3000000', 'token': '0x...', 'firstAmount': '0'}]}, 'paymentId': '0x...'}]}, {'appId': '3', 'chain': 'mumbai', 'payment': [{'payment': {'fee': 0, 'name': 'test Pay', 'owner': '0x...', 'periodType': 'DAY', 'limitPeriod': 30, 'loadingTime': 0, 'paymentType': 0, 'trialPeriod': 0, 'paymentTokens': [{'price': '500000', 'token': '0x...', 'firstAmount': '0'}]}, 'paymentId': '0x...'}, {'payment': {'fee': 0, 'name': 'OTP', 'owner': '0x...', 'periodType': 'ONETIME', 'limitPeriod': 1, 'loadingTime': 1, 'paymentType': 0, 'trialPeriod': 0, 'paymentTokens': [{'price': '10000000000000000', 'token': '0x...', 'firstAmount': '0'}]}, 'paymentId': '0x...'}]}, {'appId': '4', 'chain': 'mumbai', 'payment': [{'payment': {'fee': 0, 'name': 'Salaries', 'owner': '0x...', 'periodType': 'WEEK', 'limitPeriod': 4, 'loadingTime': 2, 'paymentType': 0, 'trialPeriod': 0, 'paymentTokens': [{'price': '3000000000', 'token': '0x...', 'firstAmount': '0'}]}, 'paymentId': '0x...'}]}, {'appId': '5', 'chain': 'mumbai', 'payment': [{'payment': {'fee': 0, 'name': 'Monthly', 'owner': '0x...', 'periodType': 'MONTH', 'limitPeriod': 6, 'loadingTime': 5, 'paymentType': 0, 'trialPeriod': 0, 'paymentTokens': [{'price': '1000000', 'token': '0x...', 'firstAmount': '0'}, {'price': '1000000000000000000', 'token': '0x...', 'firstAmount': '0'}]}, 'paymentId': '0x...'}]}], 'tags': ['']} ref='8336aa904697b4358d1c84f495c5e90114b4906182715a56afd2dc5c10837be5' type='amend'
```
