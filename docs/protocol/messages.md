# Messages

At its core, the aleph.im network is a messaging system.
All the data that transits on the network is represented by aleph.im messages that represent
all the possible operations on the network.

With aleph.im messages, you can, for example:

* store files
* pin content on IPFS
* create decentralized programs
* set up key/value databases.

Users create, sign and transmit messages to the aleph.im network.
This can be achieved in a variety of ways:

* by posting a message to a Core Channel Node
* by broadcasting the message on the aleph.im peer-to-peer network
* by using the aleph.im smart contracts deployed on supported chains.

## Message format

An aleph.im message is made of multiple fields that can be split between header and content fields.

### Header fields

#### Message info fields

* `type [str]`: the type of the message. Can be one of `AGGREGATE`, `FORGET`, `PROGRAM`,`POST`, `STORE`.
* `time [float]`: Message timestamp.
* `channel [Optional[str]]`: A user-defined string defining the channel of the message. One application ideally has one channel.
* `signature [str]`: The cryptographic signature of the message. This field guarantees the authenticity of the message.

#### Sender info fields

* `sender [str]`: Cryptographic address of the sender. Ex: the user's crypto wallet address.
* `chain [str]`: The blockchain used by the sender.

### Content fields

* `item_hash [str]`: The hash of the message content. See below.
* `item_type [str]`: Identifies where the content field can be found. Can be one of `inline`, `storage`, `ipfs`.
* `item_content [Optional[str]]`: If `item_type == inline`, contains the JSON content of the message serialized as a string.

## Message types

Actual content sent by regular users can currently be of five types:

- AGGREGATE: [aggregates](object-types/aggregates.md) provide a decentralized key/value storage.
- FORGET: delete other messages (see below).
- POST: [posts](object-types/posts.md) provide JSON documents (unique data points, events).
- PROGRAM: create and update [programs](object-types/programs.md) running in VMs (ex: lambda functions).
- STORE: [file storage](object-types/storage.md).


## Item hash, type and content

Messages are uniquely identified by the `item_hash` field. 
This value is obtained by computing the hash of the `content` field. 
Currently, the hash can be obtained in one of two ways. 
If the content of the message is stored on IPFS, the `item_hash` of the message will be the CIDv0 of this content. 
Otherwise, if the message is stored on aleph.im native storage or is included in the message, the item hash will be 
the SHA256 hash of the message in hexadecimal encoding. 
In the first case, the item type will be set to `ipfs`. 
In the second case, the item type will either be `inline` if the content is included in the message (serialized as a
string in the `item_content` field) or `storage`. 
Inline storage will be used for content up to 200kB. Beyond this size, users must upload the content as a file 
on an aleph.im node prior to uploading the message.

## Signature

aleph.im messages are cryptographically signed with the private key of the user. 
The signature covers the `sender`, `chain`, `type` and `item_hash` fields of the message.

## Deleting messages

The aleph.im protocol is GDPR-compliant.
To achieve this objective, we allow users to delete their own data.
This is implemented using a special message type called FORGET.
By sending a FORGET message, users can delete one or more messages from the entire aleph.im network.
Users can forget any type of message, except for FORGET messages themselves.

When a FORGET message is processed by a node, it will immediately mark the target message(s) as forgotten,
meaning that their `content` (and `item_content`) fields will be deleted.
In addition, any content related to the forgotten message(s) will be deleted, if no other message points to the same
content. For example, forgetting a STORE message will delete the associated file, if no other STORE message points
to the same file.

Furthermore, forgotten messages will no longer appear when querying messages from `/api/v0/messages.json`.

### Content format

The `content` field of a FORGET message must contain the
following fields:

- `address [str]`: The address to which the message belongs. See [permissions](./permissions.md).
- `time [float]`: The epoch timestamp of the message.
- `hashes [List[str]]`: The list of message hashes to forget
- `aggregates [List[str]]`: The list of aggregates to forget
- `reason [Optional[str]]`: An optional explanation of why the user wants to forget these hashes.

FORGET messages must specify at least one object to forget.

### Limitations

- At the moment, a user can only forget messages he sent himself.
