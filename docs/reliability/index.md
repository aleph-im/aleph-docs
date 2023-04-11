# Methods

## Introduction

[Aleph.im](https://aleph.im/#/) relies on a collection of servers named _nodes_, that run different tasks.

- [Core Channel Nodes](../nodes/core_channel.md) store JSON messages, copy them to other Core Channel Nodes and provide an API to fetch these messages.
- [Compute Resource Nodes](../nodes/compute_resource.md) allow users to run their own programs in Linux virtual machines in a way similar to AWS Lambda.

Node operators receive Aleph tokens as a reward for keeping their node up and running.

The current tool used to check the status of the nodes is very basic, and the project needs a more advanced tool that gives a _score_ to each node based on its availability and performance.

## Materials and Methods

The page https://account.aleph.im/ displays the nodes registered on the platform.

This page fetches the data in JSON from an AGGREGATE message on aleph.im, available from core channel nodes on the path [/api/v0/aggregates/0xa1B3bb7d2332383D96b7796B908fB7f7F3c2Be10.json?keys=corechannel&limit=50](https://api2.aleph.im/api/v0/aggregates/0xa1B3bb7d2332383D96b7796B908fB7f7F3c2Be10.json?keys=corechannel&limit=50) .

This AGGREGATE message contains the information about registered Core Channel Nodes (CCN) and Compute Resource Nodes (CRN) on the aleph.im network, including their multiaddress (for CCNs) or url (for CRNs).

Based on this information, the status and performance of the nodes can be sampled and a score can be assigned to each node. 

### Metrics

A program regularly measures the status and performance of the nodes, and publishes this data as POST messages on the network with the type `aleph-scoring-metrics`.

This program sends multiple HTTP requests to each node in order to evaluate how well it behaves.

#### Common metrics

Some metrics are common to all node types:

1. Software version: We compare the version of the node to the latest version available. Node operators have a grace period to update their node to the latest release.
2. Automatic System Number (ASN): Gives a rough estimate of where the server is located. This helps us score the decentralization of the nodes.

#### Metrics for Core Channel Nodes

1. Base latency: The base latency to respond to a request, measured by calling `/api/v0/info/public.json` (no processing on that page).
2. Metrics latency: The latency to fetch public node metrics, measured by calling `/metrics.json`
<!-- 3. The following variables from the metrics.json response:
    a. `pyaleph_status_sync_pending_txs_total`
    b. `pyaleph_status_sync_pending_messages_total`
    c. `pyaleph_status_chain_eth_height_remaining_total` -->
3. Aggregate latency: The latency to fetch a large aggregate, measured by calling `/api/v0/aggregates/0xa1B3bb7d2332383D96b7796B908fB7f7F3c2Be10.json?keys=corechannel&limit=50`.
4. File download latency: The latency to fetch a 6.7 kB file, measured by calling `/api/v0/storage/raw/50645d4ccfddb7540e7bb17ffa5609ec8a980e588e233f0e2c4451f6f9da6ebd`

Metrics are only valid if the HTTP response code is a success.

The metrics for a CCN have the following form:
```json
{
    "measured_at":1680715202.614388,
    "node_id":"5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03",
    "url":"http://12.13.14.15:4024/",
    "asn":12345,
    "as_name":"INTERNET-SERVICE-PROVIDER, AD",
    "version":"v0.5.0",
    "base_latency":0.0545351505279541,
    "metrics_latency":0.05013394355773926,
    "aggregate_latency":0.03859257698059082,
    "file_download_latency":0.04321122169494629,
    "txs_total":0,
    "pending_messages":3430570,
    "eth_height_remaining":114822
},
```

### Metrics for Compute Resource Nodes

1. Base latency: The base latency to respond to a request, measured by calling `/about/login`. Should return HTTP code `401 Unauthorized`.
2. Diagnostic VM latency: The latency to call a common user program, measured by calling `/vm/67705389842a0a1b95eaa408b009741027964edc805997475e95c505d642edd8`
3. Full check latency: The latency to run a collection of checks on the node, measured by calling `/status/check/fastapi`.

The metrics for a CRN have the following form
```json
{
    "measured_at":1680715253.669524,
    "node_id":"8cd07f3a5ff98f2a78cfc366c13fb123eb8d29c1ca37c79df190425d5b9e424d",
    "url":"https://node01.crn.domain.org/",
    "asn":12345,
    "as_name":"INTERNET-SERVICE-PROVIDER, AD",
    "base_latency":0.9623174667358398,
    "diagnostic_vm_latency":0.06729602813720703,
    "full_check_latency":0.5257446765899658
},
```

### Scores

For each node, a global score is computed from the metrics. The global score is computed as a value between 0 and 1, and is rounded to a percentage when displayed.

A score of 0 indicates that the node is disfunctionnal and should not be used. A score of 1 indicates that the node is fully functionnal and behaves perfectly.

The complete formula is based on the principles below. The formula is being tuned to take into account the reality of the nodes of the network, and feedback from community and node operators in particular is welcome.

#### Aggregation over time

The score of a node is based on the previous four weeks of metrics and is published daily.

This provides a resistance against noise in metrics, making the score more stable over time. The value of the score is therefore representative of the global behaviour of a node and is not expected to change quickly.

The other consequence is that poor performance impacts the score for a long duration. A tolerance allows short downtime for maintenance without penalizing the score. 

For each numeric metric taken into consideration when computing the score, percentiles are compared to a reference value.

#### How the score is computed

To illustrate, the `base_latency` of CRNs contributes to the node's score in the following manner:

1. The 25th percentile reflects the `base_latency` value below which 25% of the samples taken during the sampling period fall.
2. The 95th percentile reflects the `base_latency` value below which 95% of the samples taken during the sampling period fall.
3. If the node fails to respond, a default value of 100 seconds is assigned.
4. A scaling factor of 1/2 is applied.
5. The resulting value is bounded between zero and one.

The final formula for the contribution of the `base_latency` in the score is:

> \sqrt{(1 - percentile(25)(base\_latency)) / 2) * (1 - percentile(95)(base\_latency)) / 2)}

![](https://pad.okeso.net/uploads/08d97b12-ea85-42e1-9e00-028df1abf455.png)

By taking the 25th and 95th percentiles, the `base_latency` value is calculated in relation to the distribution of samples during the sampling period.

The scaling factor of 1/2 adjusts the base_latency score accordingly, so the score reflects half of the measured latency, in seconds.

#### Publishing

Scores are published as a POST message on aleph.im, with the type `aleph-scoring-scores`.


## Improving the score of your nodes

### 1. Ensure that your node is up to date

- Running the latest version of the node software.
- Installing all system updates

### 2. Ensure that the node uses performant hardware

Fast enough CPU ? Enought RAM ? Fast enough disk and bandwidth connectivity ?

### 3. Decentralize the network

Run nodes to unpopular hostings or internet service providers.

> decentralization_score = 1 - (
>    measurements.nodes_with_identical_asn / measurements.total_nodes
> )

TODO: Check what we communicated about this, the plan was to give less than 40% of the rewards to nodes where 60% of the nodes are located.

https://medium.com/aleph-im/aleph-im-tokenomics-update-nov-2022-fd1027762d99

> The rewards for running a performant CRN will range from 500 to 3000 tokens per month, depending on its location and the number of other nodes hosted on the same network. Running a performant node on a crowded network should result in a similar reward as today while decentralizing the network will result in higher rewards.

>    max_reward(node) = 500 + 2500 * (decentralization(node) — 1)**2
