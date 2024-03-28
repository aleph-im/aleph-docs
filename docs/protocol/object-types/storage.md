# File storage

Users can store files on the aleph.im network using STORE messages. 
By publishing a STORE message, users can:

* store a file in the native aleph.im storage system
* pin an IPFS CID on the aleph.im network.

STORE messages tell the aleph.im network to store data on behalf of the
user. The data can either be pinned to IPFS or stored in the native
aleph.im storage system depending on the content item type.

## STORE message content format

The `content` field of a STORE message must contain the
following fields:

* `address [str]`: The address to which the file belongs. See [permissions](../permissions.md).
* `time [float]`: The epoch timestamp of the message.
* `item_type [str]`: `storage` or `ipfs`. Determines the network to use to fetch and store the file.
* `item_hash [str]`: Hash of the file to store. Must be a CIDv0 for IPFS, or a SHA256 hash for native storage.
* `ref [Optional[str]]`: Optional reference to another file/STORE message. See `Updating files`.


## Updating files

While files on the aleph.im network are immutable, you can use the `ref` field of STORE messages to create
a virtual filename and update it.

When posting a STORE message, you can specify a value of your own liking to the `ref` field (ex: `ref: my-dynamic-nft`).
If you do not specify a value, it is automatically set to the item hash of the STORE message.

From that point, you can then update your file by sending additional STORE messages with the same `ref` value.
These messages will be considered as updates of the original.

> Updating a file does not delete the previous versions. Each file is preserved on the aleph.im network until you emit
> a FORGET message targeting these files.
