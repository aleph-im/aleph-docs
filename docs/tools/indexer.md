# Indexing Framework

The [aleph.im Indexer Framework](https://github.com/aleph-im/aleph-indexer-framework) is a node.js and
[moleculer](https://moleculer.services/) based framework for building multithreaded indexers to be deployed
on the Aleph.im network.

## Documentation

The documentation for the framework can be found [here](https://aleph-im.github.io/aleph-indexer-framework/).
Examples of working indexers can be found in the [aleph.im Indexer Library](https://github.com/aleph-im/aleph-indexer-library).

## Features

- Index data from multiple blockchains
- Fetch historical event data based on:
    - Transactions
    - Blocks
    - Logs
    - State
- Aggregate data points into buckets
- Index multiple accounts and their events
- Index and aggregate across multiple blockchains at the same time

### Supported Blockchains

The framework currently supports indexing data from the following blockchains:

- Ethereum
- Solana
- BSC

New blockchains can be easily added by implementing a new blockchain adapter.
