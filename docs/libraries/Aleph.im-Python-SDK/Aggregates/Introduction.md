Aggregates are a key-value store specific to an account.
Each time a new aggregate message is received for a specific account, the
nodes update the aggregate for this account.

Like a dictionary update, if a key already exists, it is updated,
otherwise it is created.

The aggregate object inherits from the [`Message`](broken-reference) object structure as follows:

```
{
  // Message info
  channel:
  time:
  type:
  
  // Sender info
  chain:
  sender:
  
  // Content
  hash_type:
  item_content:
    key:
    address:
    content:
    time:
  item_hash:
  item_type:
}
```

| <mark>**channel**</mark> - text                 | Channel of the message. Ideally, an application would decide and use one channel.                                                                                              |
|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <mark>**time**</mark> - float                   | Time the aggregate was created in seconds.                                                                                                                                     |
| <mark>**type**</mark> - text                    | <p>Text representing the message object type.</p><p>Value is <code>AGGREGATE</code>.</p>                                                                                       |
|                                                 |                                                                                                                                                                                |
| <mark>**chain**</mark> - text                   | <p>The chain used by the sender's account. <br>Value can be <code>NULS2</code>, <code>ETH</code>, <code>DOT</code>, <code>CSDK</code>, <code>SOL</code>, <code>AVAX</code></p> |
| <mark>**sender**</mark> -text                   | Chain address who sent and is signing the Aggregate Message.                                                                                                                   |
|                                                 | -                                                                                                                                                                              |
| <mark>**hash\_type**</mark> - optional text     | Defaults to sha256. This is the only supported value for now.                                                                                                                  |
| <mark>**item\_content**</mark> - JSON string    | <p>JSON string representing the content of the aggregate. </p><p>See below for the content of the string.</p>                                                                  |
|                                                 |                                                                                                                                                                                |
| items\_content.<mark>**key**</mark> - text      | The indexed key to reference the value (`item_content.content`) is stored under.                                                                                               |
| item\_content.<mark>**address**</mark> - text   | Chain address to associate the `Aggregate` with.                                                                                                                               |
| item\_content.<mark>**content**</mark> - object | Value object stored for the key.                                                                                                                                               |
| item\_content.<mark>**time**</mark> - timestamp | Time the object was created.                                                                                                                                                   |
|                                                 |                                                                                                                                                                                |
| <mark>**item\_hash**</mark> - hash              | The hash of the item\_content encrypted with SHA256.                                                                                                                           |
| <mark>**item\_type**</mark> - optional text     | `ipfs`, `inline` or `storage`                                                                                                                                                  |