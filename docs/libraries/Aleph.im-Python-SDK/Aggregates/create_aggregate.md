To create an aggregate, you need to call the `create_aggregate` function </br>
You must be connected to an account and authenticated to use this function. You can use the `AuthenticatedAlephHttpClient` class to authenticate.

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