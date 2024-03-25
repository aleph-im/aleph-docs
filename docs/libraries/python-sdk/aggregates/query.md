## Usage

It exists two methods to query an aggregate:

- `fetch_aggregate`: Query a single key
- `fetch_aggregates`: Query all keys.

```py
def fetch_aggregate(
    self,
    address: str,
    key: str) -> Coroutine[Any, Any, dict[str, dict]]
)
```

```py
def fetch_aggregates(
    self,
    address: str,
    keys: Optional[Iterable[str]] = None
) -> Dict[str, Dict]:
```

### Arguments

| Parameter | Description                              |
|-----------|------------------------------------------|
| `address` | The address of the aggregate sought.     |
| `key`     | The identifier for the aggregate sought. |


## Example

### Fetch aggregates

```python
from aleph.sdk.client import AlephHttpClient
import asyncio

async def main():
    async with AlephHttpClient() as client:
        aggregates = await client.fetch_aggregates(
            "0xbC80BeEcBd67549E70cb1C729e903818E6370D37",
        )
        return aggregates
    
aggregates = asyncio.run(main())
```

> outputs:
`aggregate`
```
{'profile': {'bio': 'Modify', 'name': 'modify on Ethereum'}, 'testing': {'bio': 'tester', 'name': 'Antony'}}
```

---

### Fetch aggregate

```python
from aleph.sdk.client import AlephHttpClient
import asyncio

async def main():
    async with AlephHttpClient() as client:
        aggregate = await client.fetch_aggregate(
            "0xbC80BeEcBd67549E70cb1C729e903818E6370D37",
            "profile",
        )
        return aggregate

aggregate = asyncio.run(main())
```

> output:
`aggregate`
```json
{'bio': 'Modify', 'name': 'modify on Ethereum'}
```

!!! note

    It is also possible to retrieve an aggregate from the API endpoint [like this](../../../protocol/object-types/aggregates.md#retrieve-aggregates).