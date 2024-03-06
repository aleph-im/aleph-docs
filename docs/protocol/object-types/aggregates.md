# Aggregates

AGGREGATE messages are a global key/value store mechanism. They allow users to

## Content format

The `content` field of a FORGET message must contain the following fields:

- `address [str]`: The address to which the aggregate belongs. See [permissions](../permissions.md).
- `key [str]`: The user-defined ID of the aggregate.
- `time [float]`: The epoch timestamp of the message.
- `content [Dict]`: The key/value pairs making up the aggregate, as a dictionary.

## Update aggregates

Users can update aggregates by sending additional AGGREGATE messages with the same content key. 
Updates are ordered by their content time field to match the order in which the user sent the messages originally.
The contents of the two messages are merged. Keys already present in the original message will be updated while new
keys will be added.

Example:
* Original aggregate content: `{"a": 1, "b": 2}`
* Update: `{"b": 3, "c": 4}`
* Result: `{"a": 1, "b": 3, "c": 4}`

## Retrieve aggregates

Users can retrieve aggregates by using the `/api/v0/aggregates/{address}.json` endpoint.
Specify the `keys` URL parameter to filter the response by content key. Example:

`GET /api/v0/aggregates/<my-address>.jon?keys=key1,key2`
