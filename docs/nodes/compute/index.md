# Introduction

Aleph.im compute resource nodes (CRN) are decentralized computing infrastructure components that form a vital part of the
aleph.im network. These nodes work collectively to provide distributed and secure computing power, storage, and other
resources to users and applications on the platform.

Compute resource nodes are designed to support a wide range of tasks, including off-chain smart contract execution,
decentralized application (dApp) hosting, and decentralized file storage. These nodes enable users to access and utilize
decentralized computing resources without relying on centralized servers or cloud providers, ensuring better privacy,
security, and control over their data and applications.

In return for their contributions, node
operators are rewarded with ALEPH tokens, creating an incentive system for maintaining a healthy and robust ecosystem.

The aleph.im network relies on a peer-to-peer architecture, where compute resource nodes communicate with each other to
share information and coordinate tasks. This architecture ensures that the network remains resilient against single
points of failure, as the removal of one node does not impact the overall functioning of the system.

Furthermore, aleph.im employs advanced cryptographic techniques and consensus algorithms to ensure that the compute
resource nodes

## Hardware requirements:

- **Platform**: A bare metal server is required since virtual servers are often too slow and unable to run nested virtualization.
- **Processor** using x86_64 (alias amd64) architecture (2 options):
    - Min. 8 cores / 16 threads, 3.0ghz+ CPU (gaming CPU for fast boot-up of microVMs)
    - Min. 12 core / 24 threads, 2.4ghz+ CPU (datacenter CPU for multiple concurrent loads)
- **Memory**: Min. 64GB of RAM
- **Storage**: 1TB (NVME SSD preferred, datacenter fast HDD possible under conditions, you’ll want a big and fast cache)
- **Connectivity**: Minimum of 500 Mbit/s, both IPv4 and IPv6 configured

## Requirements

### 1. Installation
Follow the [installation guide](./installation/debian-12.md) to install the server.

### 2. Registration
Follow the [registration](https://medium.com/aleph-im/step-by-step-on-how-to-create-and-register-your-compute-resource-node-e5308130fbf7) guide first.
