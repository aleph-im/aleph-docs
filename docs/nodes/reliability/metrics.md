# Metrics

A program regularly measures the status and performance of the nodes, and publishes this data as POST messages on the network with the type `aleph-scoring-metrics`.

This program sends multiple HTTP requests to each node in order to evaluate how well it behaves.

## Common metrics

Some metrics are common to all node types:

1. **Software version**: We compare the version of the node to the latest version available. Node operators have a grace period to update their node to the latest release.
2. **Automatic System Number** (ASN): Gives a rough estimate of where the server is located. This helps us score the decentralization of the nodes.

## Metrics for Core Channel Nodes

1. **Base latency**: The base latency to respond to a request, measured by calling `/api/v0/info/public.json` (no processing on that page).
2. **Metrics latency**: The latency to fetch public node metrics, measured by calling `/metrics.json`
[//]: # (3. The following variables from the metrics.json response:)
[//]: # (    a. `pyaleph_status_sync_pending_txs_total`)
[//]: # (    b. `pyaleph_status_sync_pending_messages_total`)
[//]: # (    c. `pyaleph_status_chain_eth_height_remaining_total`)
3. **Aggregate latency**: The latency to fetch a large aggregate, measured by calling `/api/v0/aggregates/0xa1B3bb7d2332383D96b7796B908fB7f7F3c2Be10.json?keys=corechannel&limit=50`.
4. **File download latency**: The latency to fetch a 6.7 kB file, measured by calling `/api/v0/storage/raw/50645d4ccfddb7540e7bb17ffa5609ec8a980e588e233f0e2c4451f6f9da6ebd`

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
}
```

## Metrics for Compute Resource Nodes

1. **Base latency**: The base latency to respond to a request, measured by calling `/about/login`. Should return HTTP code `401 Unauthorized`.
2. **Diagnostic VM latency**: The latency to call a common user program, measured by calling `/vm/67705389842a0a1b95eaa408b009741027964edc805997475e95c505d642edd8`
3. **Full check latency**: The latency to run a collection of checks on the node, measured by calling `/status/check/fastapi`.

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
}
```

## Publishing

Metrics are published as a POST message on aleph.im, with the type `aleph-scoring-metrics`.

You can [find the metrics on the aleph.im Explorer](
https://explorer.aleph.im/address/ETH/0x4D52380D3191274a04846c89c069E6C3F2Ed94e4).
