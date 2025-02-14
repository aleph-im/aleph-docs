# Aggregates

Aggregates are a global key-value store specific to an account. The mechanism to update an account aggregate is to send
an AGGREGATE message.

Each time a new AGGREGATE message is received for a specific account, the
nodes update the aggregate for this account.

Like a dictionary update, if a key already exists, it is updated,
otherwise it is created.

## Content format

The `content` field of an AGGREGATE message must contain the following fields:

- `address [str]`: The address to which the aggregate belongs.
  See [Delegate write access to another account](#delegate-write-access-to-another-account) below.
- `key [str]`: The user-defined ID of the aggregate.
- `time [float]`: The epoch timestamp of the message.
- `content [Dict]`: The key/value pairs making up the aggregate, as a dictionary.

## Update aggregates

Users can update aggregates by sending additional AGGREGATE messages with the same content key.
Updates are ordered by their content time field to match the order in which the user sent the messages originally.
The contents of the two messages are merged. Keys already present in the original message will be updated while new
keys will be added.

Example:

- Original aggregate content: `{"a": 1, "b": 2}`
- Update: `{"b": 3, "c": 4}`
- Result: `{"a": 1, "b": 3, "c": 4}`

## Retrieve aggregates

Users can retrieve aggregates by using the `/api/v0/aggregates/{address}.json` endpoint.
Specify the `keys` URL parameter to filter the response by content key. Example:

`GET /api/v0/aggregates/<my-address>.jon?keys=key1,key2`

## Delegate write access to another account

It is possible for an account to modify the aggregate of another account.

In this case the `content.address` field would be set to the address of the aggregate's account and would be different
from the message sender's address.

To permit delegate write access to a specific key in your aggregates,
use the security aggregate as explained in
the [permissions section](../permissions.md).