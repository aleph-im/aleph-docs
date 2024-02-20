Inside most Messages, there is an **"address"** field. This is the address for which the message applies (for which address to apply this aggregate, who posted that item…).</br>

With a security key, you can delegate some rights to your messages to another account. You can interact with a message in two cases:<br>

- The sender == the person that posts the original message.
- The owner of the message has a security key for your address.

## Setup and Create a security key

The only way to set up a security key is to send a special AGGREGATE message on the **"security"** channel.<br>
Only the account itself can have the right to send an AGGREGATE message on the **"security"** channel, this feature can't be delegated at this moment.<br>

The way to structure a security key:

- Must be an **object**
- The subkey has to be called `authorizations`
- the authorizations subkey value is an array of objects as follows:

```python
{'authorizations': [
    {
        'address': '<ADDRESS_TO_AUTHORIZE>',
        'types': ['AGGREGATE'],
        'post_types': ['chat'],
        'aggregate_keys': ['testkey', 'preferences'],
        'chains': ['ETH'],
        'channels': ['MYCHANNEL']
    }
]}
```

> If some filter is set only messages that match the filter set (all options selected) will be accepted except for:
>
> - post_types only apply to POST Messages
> - aggregate_keys only apply to AGGREGATE Messages

### Parameters

#### Required Parameters

| Parameter | Type   | Description                                                                |
|-----------|--------|----------------------------------------------------------------------------|
| `address` | String | account address to authorize to write on behalf of the aggregate's address |


#### Optional Parameters

| Parameter       | Type   | Description                                                                           |
|-----------------|--------|---------------------------------------------------------------------------------------|
| `types`         | String | Can be Post, Aggregate, or Store; Only these types will be accepted from this address |
| `post_types`    | String | Only those post types will be writeable by the address                                |
| `aggregate_key` | String | Only those keys will be writeable by the address                                      |
| `chains`        | String | Only accept the passed address on a specific chain                                    |
| `channels`      | String | Only messages from these channels will be accepted                                    |

### Exemple

Here is an example of how to create a security key:

```python
import { ItemType } from 'aleph-sdk-ts/dist/messages/message';
import { Publish as publishAggregate } from 'aleph-sdk-ts/dist/messages/aggregate';
import { ETHAccount } from 'aleph-sdk-ts/dist/chains/ethereum';

(async () => {
    account = ETHAccount.fromPrivateKey('0x...');
    await publishAggregate({
        account: account,
        key: 'security',
        content: {'authorizations': [
            {
                'address': '0x...',
                'types': ['AGGREGATE'],
                'aggregate_keys': ['testkey'],
            }
        ]},
        channel: 'security',
    })
})();
```

As you can see, we specified the delegate account will only be able to update the testkey field of the owner's aggregates.`
