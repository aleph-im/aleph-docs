# Scores

For each node, a global score is computed from the [metrics](metrics.md). The global score is computed as a value
between 0 and 1, and is rounded to a percentage when displayed.

A score below 20% indicates that the node is dysfunctional and should not be used.
A score above 80% indicates that the node is fully functional and behaves well.

The complete formula is based on the principles below. The formula is being tuned to take into account the reality of
the nodes of the network, and feedback from community and node operators in particular is welcome.

## Aggregation over time

The score of a node is based on the previous four weeks of metrics and is published daily.

This provides a resistance against noise in metrics, making the score more stable over time. The value of the score is
therefore representative of the global behaviour of a node and is not expected to change quickly.

The other consequence is that poor performance impacts the score for a long duration. A tolerance allows short downtime
for maintenance without penalizing the score.

For each numeric metric taken into consideration when computing the score, percentiles are compared to a reference
value.

## How the score is computed

To illustrate, the `base_latency` of CRNs contributes to the node's score in the following manner:

1. The 25th percentile reflects the `base_latency` value below which 25% of the samples taken during the sampling period
   fall.
2. The 95th percentile reflects the `base_latency` value below which 95% of the samples taken during the sampling period
   fall.
3. If the node fails to respond, a default value of 100 seconds is assigned.
4. A scaling factor of 1/2 is applied.
5. The resulting value is bounded between zero and one.

The final formula for the contribution of the `base_latency` in the score is:

$$
\sqrt{(1 - \frac{percentile(25)(base\_latency)}{2}) * (1 - \frac{percentile(95)(base\_latency)}{2})}
$$

By taking the 25th and 95th percentiles, the `base_latency` value is calculated in relation to the distribution of
samples during the sampling period.

The scaling factor of $1/2$ has been chosen based on the maximal ping time typically measured across the globe, which is
around 0.7 seconds.
A node with such latency would therefore have a maximal score up to 65 % in the case of a single source
of metrics.

## Publishing

Scores are published as a POST message on aleph.im, with the type `aleph-scoring-scores`.

You can [find the scores on the aleph.im Explorer](
https://explorer.aleph.im/address/ETH/0x4D52380D3191274a04846c89c069E6C3F2Ed94e4).

## Improving the score of your nodes

### 1. Ensure that your node is up-to-date:

- Run the latest version of the node software.
- Install all system updates.

### 2. Ensure that the node uses performant hardware

Fast enough CPU ? Enough RAM ? Fast enough storage and bandwidth connectivity ?

### 3. Decentralize the network

While the decentralization of the network does not affect the reliability and performance score
of nodes directly, it has a big effect when computing the rewards.
See the rewards page for more info.
