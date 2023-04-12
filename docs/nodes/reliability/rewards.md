# Rewards

Node operators and stakers receive rewards for contributing to the aleph.im network and its ecosystem.

## Core Channel Nodes

A [Core Channel Node](../core_channel.md) (CCN) is active when it is registered on the [aleph.im account page](
https://account.aleph.im), has enough ALEPH token staked on it and has a [score](scores.md) non null.

The performance score of a CCN affects the rewards distributed to the operator and stakers of the node the following way:

- No reward is distributed when the score is below 20% .
- A direct proportion of the reward is distributed when the score is between 20% and 80%.
- The complete reward is distributed when the score is equal to or greater than 80%

The rewards distribured does not depend on the score of other nodes in the network. Less token from the pool
will be distributed.

### Node Operators

CCN operators share a reward pool for running these nodes. See [our article on Core Channel Nodes](
https://medium.com/aleph-im/aleph-im-staking-go-live-part-1-core-channel-nodes-and-node-operators-97bfcd43157d) 
and the [Tokenomics update](https://medium.com/aleph-im/aleph-im-tokenomics-update-nov-2022-fd1027762d99) for 
details.

When the scoring system will become active, the reward pool will be distributed to node operators based on the 
20%-80% distribution described above.

$$
max\_rewards = \frac{15 000 ALEPH}{count(core\_channel\_nodes)}
$$

$$
rewards = max\_rewards * multiplier(score(node), 20\%, 80\%)
$$

### Stakers

Stakers share a second reward pool. See [our article on Stakers Tokenomics](
https://medium.com/aleph-im/aleph-im-staking-go-live-part-2-stakers-tokenomics-663164b5ec78) and the
[Tokenomics update](https://medium.com/aleph-im/aleph-im-tokenomics-update-nov-2022-fd1027762d99) for details.

When the scoring system will become active, the reward pool will be distributed to stakers based on the 
20%-80% distribution described above.

When the same wallet is used to stake on multiple nodes, the stake is distributed equally amongst these nodes
and the score of each node affect the proportion of the rewards dedicated to it.

$$
balance\_ratio = \frac{balance}{\sum_{staker}^{stakers}{balance(staker)} * count(nodes\_staked)}
$$

$$
rewards = 15 000 ALEPH * \sum_{node}^{nodes\_staked}{multiplier(score(node), 20\%, 80\%) * balance\_ratio}
$$

## Compute Resource Nodes

Rewards for running a compute resource node (CRN) will follow the [Tokenomics update](and the
[Tokenomics update](https://medium.com/aleph-im/aleph-im-tokenomics-update-nov-2022-fd1027762d99) we published in
November. 

The rewards for running a performant CRN will range from 500 to 3000 tokens per month, depending on its location and the number of other nodes hosted on the same network. Running a performant node on a crowded network should result in a similar reward as today while decentralizing the network will result in higher rewards.

The reward of a CRN is the sum of a fixed amount and a decentralization bonus, multiplied by the score according to the
20%-80% rule stated above.

$$
decentralization\_score = (1 - \frac{nodes\_with\_identical\_asn}{total\_nodes})^2
$$

$$
max\_rewards = 500 + decentralization\_score * 2500
$$

$$
rewards = max\_rewards * multiplier(score, 20\%, 80\%)
$$
