To query keys from an account aggregate, you need to call the
`fetch_aggregate` function on the client.

Since version 0.8.0, only the asynchronous methods are available.

As per usual, use `asyncio.run` to run the asynchronous code:

```python
import asyncio
from aleph.sdk.client import AlephHttpClient

async def main():
    async with AlephHttpClient() as client:
        aggregate = await client.fetch_aggregate(
            "0x06DE0C46884EbFF46558Cd1a9e7DA6B1c3E9D0a8",
            "profile",
        )
        print(aggregate)

if __name__ == "__main__":
    asyncio.run(main())
```
outputs:
```json
{"bio": "tester", "name": "Moshe on Ethereum"}
```