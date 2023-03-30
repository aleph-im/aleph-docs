# Permissions

All aleph.im message types have an `address` content field. 
This is the address of the owner of the object on the aleph.im network.
Ex: a program, a file, a post, an aggregate.

Core Channel Nodes validate that the message sender (the one signing the message) has the right to publish 
on behalf of the object owner.

1. Obvious case: if the sender == the content address, it is authorized.
2. The `security` aggregate of the owner address allows the sender to perform the operation. 

## The security aggregate

The `security` aggregate is a reserved aggregate dedicated to permissions.
It can only be modified by sending an aggregate message on the `security` channel.
An address can only set permissions for itself, meaning that `sender == content.address` must apply for security
aggregate messages.

### The authorizations subkey

Users can specify multiple authorizations for several addresses. This is achieved using the `authorizations` subkey
of the security aggregate.

It is an array of authorization objects. 
Each authorization object has the following fields:
 
| Field             | Description                                             |
|-------------------|---------------------------------------------------------|
| address           | The address to authorize.                               |
| chain             | Optional. Only accept this address on a specific chain. |
| channels          | Optional. Authorized channel list.                      |
| types             | Optional. The authorized message types.                 |
| post_types        | Optional. Specific post types authorized.               |
| aggregate_keys    | Optional. Specific aggregate keys authorized.           |

    Example:
    
    channels: ['blog'] => only post in the "blog" channel will be accepted.
    types: ['POST'] => only POST messages will be accepted from this sender.               
    aggregate_keys: ['profile', 'preferences'] => only those keys will be writeable.

Filters inside an authorization object are exclusive.
For example, if an authorization object is set to `{"address": "xyz", "chain": "ETH", "types": ["AGGREGATE"]}`, 
user xyz will only be able to post aggregate messages on behalf of the owner with his Ethereum address.

To combine multiple permissions, users can specify multiple authorization objects for the same user.
