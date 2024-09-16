# Decentralized IPFS Pinning
## Overview
Aleph.im introduces decentralized [InterPlanetary File System (IPFS)](https://ipfs.tech/)
pinning in its decentralized cloud platform. This feature aligns with the company's emphasis on decentralization
and resistance to censorship, aiming to improve data storage and sharing.

### How To Use
Aleph.im's decentralized IPFS pinning is available to all users, using Aleph.im's SDKs:

- [Python SDK](../libraries/python-sdk/index.md)
- [TypeScript SDK](../libraries/typescript-sdk/index.md)

## IPFS Pinning Explained
IPFS pinning is a process in the distributed file system, IPFS, which links computing devices with a unified file system.
It involves persistently storing data on a specific node to ensure its availability in the network,
preventing data loss as new data is added. For more information, see the [IPFS documentation](https://docs.ipfs.io/concepts/persistence/).

### Centralized Pinning: A Closer Look
Traditional IPFS pinning often uses a centralized model, relying on a single node or service for data storage.
This approach can pose risks to data availability and integrity in case of node failures or service disruptions.

### Aleph.im's Decentralized Approach
Aleph.im adopts a decentralized pinning method, spreading data across multiple [Core Channel Nodes](../nodes/core/index.md) in its network.
This strategy enhances data redundancy and resilience, mitigating risks associated with single-node failures.

This approach to decentralized pinning is part of Aleph.im's commitment to full decentralization.
It aims to give users increased control over their data, while improving the network's data availability and security.
