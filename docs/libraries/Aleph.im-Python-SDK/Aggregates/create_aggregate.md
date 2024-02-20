To create an aggregate, you need to call the `create_aggregate` function </br>
You must be connected to an account and authenticated to use this function. You can use the `AuthenticatedAlephHttpClient` class to authenticate.

!!! note
    Since creating an Aggregate message mutates the value of the specific key,
    if the key exists, the value object will be updated (mutated) with the object you are saving. <br>
    <br> An exemple is given at the end of this page.

## Usage

```python
    def create_aggregate(
        account,
        key,
        content,
        address,
        channel,
        session,
        api_server)
```

### Parameters

#### Required Parameters

| Parameter | Description                        |
|-----------|------------------------------------|
| `account` | The account to use for the request |
| `key`     | The key of the aggregate           |
| `content` | The content of the aggregate       |


#### Optional Parameters

| Parameter    | Default value           | Description                                                                             |
|--------------|-------------------------|-----------------------------------------------------------------------------------------|
| `address`    | None                    | The address of the aggregate. If not provided, the address of the account will be used. |
| `channel`    | "TEST"                  | The channel of the aggregate. If not provided, the default channel will be used.        |
| `session`    | None                    | The session of the aggregate. If not provided, the default session will be used.        |
| `api_server` | "https://api2.aleph.im" | The API server to use. If not provided, the default API server will be used.            |


### Example

Here is a simple example of how to use the `create_aggregate` function:

```python
    from aleph.sdk.chains.ethereum import ETHAccount
    from aleph.sdk.client import AuthenticatedAlephHttpClient
    
    async def main():
        prv = bytes.fromhex("xxxxxx")
        account = ETHAccount(prv)
        async with AuthenticatedAlephHttpClient(account) as client:
            message, status = await client.create_aggregate(
                "profile",
                {"bio": "tester", "name": "MY_NAME on Ethereum"},
            )
            print(message.content)
```

### Output

```json
{
    "address": "0x...",
    "key": "profile",
    "content": {"bio": "tester", "name": "MY_NAME on Ethereum"},
    "time": 1689081614.4252806
}
```

## Update / mutate an aggregate

> Using the same key as the one used in the previous example, we will update the content of the aggregate.

To mutate an aggregate you need to call the create_aggregate function (it will
create an AGGREGATE type message for you and submit it).

You need a valid account and instantiate an authenticated client:

```python
from aleph.sdk.chains.ethereum import get_fallback_account
from aleph.sdk.client import AuthenticatedAlephHttpClient

async def main():
    account = get_fallback_account()
    async with AuthenticatedAlephHttpClient(account) as client:
        message, status = await client.create_aggregate(
            "profile",
            {"bio": "Modify", "name": "modify on Ethereum"},
        )
        print(message.content)
```
outputs:
```json
{
    "key": "profile",
    "content": {"bio": "Modify", "name": "modify on Ethereum"},
    "address": "0x...",
    "time": 1689081614.4252806
}
```