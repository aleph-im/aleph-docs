# Rewards

Node operators and stakers receive rewards for contributing to the aleph.im network and its ecosystem.

## Core Channel Nodes

A [Core Channel Node](../core/index.md) (CCN) is active when it is registered on the [aleph.im account page](
https://account.aleph.im), has enough ALEPH token staked on it and has a [score](scores.md) non null.

The performance score of a CCN affects the rewards distributed to the operator and stakers of the node the following way:

 - No reward is distributed when the score is below 20% .
 - A direct proportion of the reward is distributed when the score is between 20% and 80%.
 - (x - 0.2) / 0.6
 - The complete reward is distributed when the score is equal to or greater than 80%

The second factor that affects the rewards of a CCN is its linking to
[Compute Resource Nodes](../compute/index.md) (CRN). A CCN can have up to 5 CRNs linked to it, and the CCN will incur a penalty if it has less than 3 working CRNs linked.
The penalty is of 10% of the rewards for each spot unfilled or filled with a defaulting CRN (score of 0), with a maximum penalty of 30%.

This gives the following distribution:

 - From 3 to 5 CRNs linked = 100% of rewards
 - 2 CRNs linked = 90% of rewards
 - 1 CRN linked = 80% of rewards
 - 0 CRN linked = 70% of rewards

The rewards distributed does not depend on the score of other nodes in the network. Less token from the pool
will be distributed when nodes do not perform well enough.

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
linkage(node) = 70 \% + \sum_{crn}^{linked\_CRNs(node)}{10 \%\ if\ score(crn) > 0\ else\ 0 \%}
$$

$$
rewards = max\_rewards * linkage * multiplier(score(node), 20\%, 80\%)
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
linkage(node) = 70 \% + \sum_{crn}^{linked\_CRNs(node)}{10 \%\ if\ score(crn) > 0\ else\ 0 \%}
$$

$$
rewards = 15 000 ALEPH * \sum_{node}^{nodes\_staked}{multiplier(score(node), 20\%, 80\%) * balance\_ratio * linkage(node)}
$$

## Compute Resource Nodes

Rewards for running a compute resource node (CRN) will follow the
[Tokenomics update](https://medium.com/aleph-im/aleph-im-tokenomics-update-nov-2022-fd1027762d99) we published in November 2022. 

The rewards for running a performant CRN will range from 250 to 1500 tokens per month, depending on its location and the number of other nodes hosted on the same network. Running a performant node on a crowded network should result in a similar reward as today while decentralizing the network will result in higher rewards.

The reward of a CRN is the sum of a fixed amount and a decentralization bonus, multiplied by the score according to the
20%-80% rule stated above.

$$
decentralization\_score = (1 - \frac{nodes\_with\_identical\_asn}{total\_nodes})^2
$$

$$
max\_rewards = 250 + decentralization\_score * 1250
$$

$$
rewards = max\_rewards * multiplier(score, 20\%, 80\%)
$$
