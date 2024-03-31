# Indexer Setup Guide for an EVM based Blockchain
This guide provides a comprehensive walkthrough for setting up an indexer on a EVM based blockchain (like ethereum, binance smart chain or oasys) capable of tracking smart contract events and exposing them through a GraphQL API. It covers initial project setup, installation of dependencies, and configuration steps to track events across different networks (mainnet, testnet, etc). The setup includes detailed instructions for configuring the indexer's architecture, managing event tracking and handling, setting up a local database for data storage, and exposing the indexed data via a GraphQL API.

## 1. Project Initialization

### 1.1 Create Project Directory
Open your terminal and execute the following commands to create a new directory for your project and navigate into it:

```sh
mkdir my-awesome-indexer && cd my-awesome-indexer
```

### 1.2 Initialize Node.js Project
Initialize a new Node.js project by running:

```sh
npm init -y
```
This command creates a default package.json file in your project directory.

### 1.3 Install Required Packages
Install the necessary Node.js packages for the indexer framework and the specific blockchain you intend to index (ethereum in this case) by executing:

```sh
npm install @aleph-indexer/core @aleph-indexer/framework @aleph-indexer/ethereum
```

### 1.4 Configure Package.json
To use ES6 module syntax, which is recommended for this project, add the following line to your package.json:

```sh
"type": "module"
```

## 2. Indexer Configuration
### 2.1 Supported Blockchains
To index events from various blockchains, you need to install specific packages for each blockchain. Below is a list of packages for some of the supported blockchains:

- EVM:
  - **Ethereum**: @aleph-indexer/ethereum
  - **Binance Smart Chain**: @aleph-indexer/bsc
  - **Oasys L1**: @aleph-indexer/oasys
  - **Oasys L2 (Homeverse)**: @aleph-indexer/oasys-verse
- Others
  - **Solana**: @aleph-indexer/solana

This indexer setup allows you to track multiple blockchains simultaneously by installing the corresponding package for each blockchain you wish to index.

### 2.2 Setup Index.js
Create a src directory in your project, and within it, create an index.js file. This file will serve as the main entry point for your indexer's configuration. Initially, set up the indexer to track events from the ethereum mainnet and testnet:

```js
// src/index.js
import indexer, { BlockchainChain } from '@aleph-indexer/framework'

indexer.init({
  projectId: 'my-awesome-indexer',
  apiPort: 8080,
  supportedBlockchains: [
    { chain: BlockchainChain.Ethereum, id: 'ethereum-mainnet' },
    { chain: BlockchainChain.Ethereum, id: 'ethereum-testnet' }
  ],
})
```

This basic setup prepares your indexer to connect with the specified blockchain networks and start tracking events. Further configurations will be discussed in the following sections to fully enable event tracking, data processing, and API exposure.

## 3. Indexer Services and Architecture
### 3.1 Overview of Services
The indexer's architecture is designed for scalability and high availability, incorporating three key microservices: fetcher, parser, and indexer. These services can be horizontally scaled to meet demand and are interconnected through an abstract transport layer, allowing for flexible deployment strategies.

- **Fetcher**: Responsible for retrieving blockchain data.
- **Parser**: Parses the data into a structured format.
- **Indexer**: Indexes the parsed data for efficient querying.

By default, these services communicate using the Thread transport layer, which employs memory buffers for inter-thread communication.

### 3.2 Configure Microservices
To avoid the "Error: If selected transport is 'Thread'..." message and ensure your services are correctly configured, modify your index.js file with the following additional configuration settings:

```js
// src/index.js
import indexer, { BlockchainChain } from '@aleph-indexer/framework'

indexer.init({
  ...,
  fetcher: { instances: 1 },
  parser: { instances: 1 },
  indexer: { 
    worker: { instances: 1 } 
  }
})
```
This setup ensures that one instance of each microservice is running, allowing them to communicate locally using worker threads.

## 4. Event Tracking and Handling
### 4.1 Define Entrypoints
To start tracking and handling events, create two key entry points in the src/indexer directory: main.js and worker.js. These files will define how your indexer interacts with incoming blockchain data.

- **main.js**: Serves as the primary entry point for the indexer and the interface for the API. It will orchestrate the indexing process and manage communication with the worker instances.
- **worker.js**: Handles the processing of blockchain data, including filtering and indexing events.

Create a folder named indexer inside src, then create the main.js and worker.js files with basic class structures extending the framework's domain classes:

```js
// src/indexer/main.js
import { IndexerMainDomain } from '@aleph-indexer/framework'
export default class MainDomain extends IndexerMainDomain { }
```

```js
// src/indexer/worker.js
import { IndexerWorkerDomain } from '@aleph-indexer/framework'
export default class WorkerDomain extends IndexerWorkerDomain { }
```

Update your index.js to include these new entry points:
```js
// src/index.js
import path from 'path'
import { fileURLToPath } from 'url'

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

import indexer, { BlockchainChain } from '@aleph-indexer/framework'

indexer.init({
  ...,
  indexer: {
    main: {
      domainPath: path.join(__dirname, './indexer/main.js')
    },
    worker: { 
      instances: 1,
      domainPath: path.join(__dirname, './indexer/worker.js')
    }
  }
})
```

### 4.2 Configuring Tracked Contracts
To specify which contracts your indexer should track, you need to add configurations within the main.js file. Use the indexAccounts method to register contracts and their events for tracking:

```js
// src/indexer/main.js
import { IndexerMainDomain } from '@aleph-indexer/framework'

export default class MainDomain extends IndexerMainDomain {
  async init() {
    await super.init()
    await this.indexAccounts([
      {
        // The `Aleph.im v2` ERC20 token contract on the network with id `ethereum-mainnet`
        blockchainId: 'ethereum-mainnet',
        account: '0x27702a26126e0B3702af63Ee09aC4d1A084EF628',
        index: { logs: true },
      },
      {
        // The `Aleph.im v2` ERC20 token contract on the network with id `ethereum-testnet`
        blockchainId: 'ethereum-testnet',
        account: '0xC751491ae7dec5139a219d6094EF3fAd540A6de1',
        index: { logs: true },
      },
    ])
  }
}
```
This setup enables your indexer to start tracking events emitted by the specified contracts on both the ethereum mainnet and testnet (Goerli).

## 5. Blockchain Configuration and Data Processing
### 5.1 Environment Variables
For the indexer to interact with the blockchain networks effectively, it requires access to RPC (Remote Procedure Call) URLs. These URLs are necessary for fetching data from the blockchain. Define the environment variables in a .env file at the root of your project. Each variable should be prefixed with the blockchain ID specified in your configuration, ensuring the indexer can differentiate between multiple networks:

```sh
# .env file example
ETHEREUM_TESTNET_RPC=https://goerli.gateway.tenderly.co
ETHEREUM_TESTNET_EXPLORER_URL=https://api-goerli.etherscan.io/api?module=contract&action=getabi&address=$ADDRESS

ETHEREUM_MAINNET_RPC=https://eth.drpc.org
ETHEREUM_MAINNET_EXPLORER_URL=https://api.etherscan.io/api?module=contract&action=getabi&address=$ADDRESS
```
Ensure your project loads these environment variables, for example, by using the dotenv package.

### 5.2 Implementing Event Handlers
In the worker.js file, implement handlers for processing the blockchain data. These handlers filter and index the events based on your criteria. By overriding specific methods, you can define custom logic for how events from each blockchain network are processed:

```js
// src/indexer/worker.js
import { IndexerWorkerDomain } from '@aleph-indexer/framework'

export default class WorkerDomain extends IndexerWorkerDomain {
  async onNewAccount(config) {
    const { account } = config
    const { instanceName } = this.context

    console.log(`New account [${account}] tracked by worker [${instanceName}]`)
  }

  async ethereumTestnetFilterLog(context, entity) {
    return this.filterEVMLog('ethereum-testnet', context, entity)
  }

  async ethereumTestnetIndexLogs(context, entities) {
    return this.indexEVMLogs('ethereum-testnet', context, entities)
  }

  async ethereumMainnetFilterLog(context, entity) {
    return this.filterEVMLog('ethereum-mainnet', context, entity)
  }

  async ethereumMainnetIndexLogs(context, entities) {
    return this.indexEVMLogs('ethereum-mainnet', context, entities)
  }

  async filterEVMLog(blockchainId, context, entity) {
    const eventSignature = entity.parsed?.signature
    console.log(`Filter ${blockchainId} logs`, eventSignature)

    // Here we can filter the received events before passing them to the next step in the pipeline
    // In this example we are going to let them all to pass
    return true
  }

  async indexEVMLogs(blockchainId, context, entities) {
    console.log(`Index ${blockchainId} logs`, JSON.stringify(entities, null, 2))

    // This is the right place to handle the incoming events and parse with own business logic 
    // before saving them in a database
  }
}
```

These methods allow fine-grained control over which events are indexed and how they are processed, ensuring that your indexer is tailored to the specific needs of your application.

- The `[BlockchainId]filterLog()` method will be used to filter the events we want to process in a later stage. It could be useful for example to only take into account `Transfer` kind of events on a contract and skip the rest
- The `[BlockchainId]indexLog()` will be called at the end of the pipeline and is the place to handle the received information. For example send the event to and external queue, store it in a database, etc.

In our example we will accept all the events no matter the schema they have (that's why we are returning always true on the filter method). And then, we will store them in a local database indexed by height to be able to query them later from the graphQL API, but for now let's just log them in console and try if everything works.

> Note: If an error is thrown in some of this methods the current incoming chunk will be marked as not processed and will be retried in a later stage

This is the schema of a parsed event:

```json
{
  "address": "0x27702a26126e0B3702af63Ee09aC4d1A084EF628",
  "topics": [
    "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
    "0x00000000000000000000000007898e6ee58e714af2653013edd99802711a96d8",
    "0x000000000000000000000000c81781d75effd1def296fb8a9480e918cd146d27"
  ],
  "data": "0x000000000000000000000000000000000000000000000025f27390d092ef8669",
  "blockNumber": 19470109,
  "transactionHash": "0x3ab13a526aa428f5856c14e324b31fdd671e80cc961d3d0ee7bd54da83e2bba8",
  "transactionIndex": 235,
  "blockHash": "0x6c21a970018a8e7aefe9d4e88a0cbf38c161c286c49824b01dcf0d88780baf4d",
  "logIndex": 467,
  "removed": false,
  "id": "19470109_0x27702a26126e0b3702af63ee09ac4d1a084ef628_467",
  "height": 19470109,
  "timestamp": 1710867239000,
  "parsed": {
    "eventFragment": {
      "name": "Transfer",
      "anonymous": false,
      "inputs": [
        {
          "name": "_from",
          "type": "address",
          "indexed": true,
          "components": null,
          "arrayLength": null,
          "arrayChildren": null,
          "baseType": "address",
          "_isParamType": true
        },
        {
          "name": "_to",
          "type": "address",
          "indexed": true,
          "components": null,
          "arrayLength": null,
          "arrayChildren": null,
          "baseType": "address",
          "_isParamType": true
        },
        {
          "name": "_value",
          "type": "uint256",
          "indexed": false,
          "components": null,
          "arrayLength": null,
          "arrayChildren": null,
          "baseType": "uint256",
          "_isParamType": true
        }
      ],
      "type": "event",
      "_isFragment": true
    },
    "name": "Transfer",
    "signature": "Transfer(address,address,uint256)",
    "topic": "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef",
    "args": [
      "0x07898e6EE58e714af2653013edd99802711a96d8",
      "0xc81781D75EffD1deF296fb8a9480E918cD146d27",
      {
        "type": "BigNumber",
        "hex": "0x25f27390d092ef8669"
      }
    ]
  }
}
```

## 6. Data Storage
### 6.1 Setting Up Local Database
The indexer requires a database to store and query the processed events efficiently. Utilize the EntityStorage class provided by the @aleph-indexer/core package to manage your data. Create a Data Access Layer (DAL) to abstract database operations:

```js
// src/dal/event.js
import { EntityStorage } from '@aleph-indexer/core'

export const eventDALIndex = {
  BlockchainHeight: 'blockchain_height',
}

const idKey = {
  get: (e) => e.id,
  length: EntityStorage.VariableLength,
}

const blockchainKey = {
  get: (e) => e.blockchain,
  length: EntityStorage.VariableLength,
}

const heightKey = {
  get: (e) => e.height,
  length: 8,
}

export function createEventDAL(path) {
  return new EntityStorage({
    name: 'event',
    path,
    key: [idKey],
    indexes: [
      {
        name: eventDALIndex.BlockchainHeight,
        key: [blockchainKey, heightKey],
      },
    ],
  })
}
```
This setup allows for the efficient storage and retrieval of blockchain events, leveraging indexes to optimize query performance.

The `EntityStorage` class will store event entities using the id field as the primary key and as we have configured one index, it will also manage to update this index each time a new entity is added, updated or removed from the database.

## 6.2 Integrating DAL with Workers
Integrate the DAL into your indexer's worker instances to enable the storage of indexed events. Modify the worker.js file to instantiate the DAL and use it within the event processing methods:

```js
// src/indexer/worker.js
import { IndexerWorkerDomain } from '@aleph-indexer/framework'
import { createEventDAL, eventDALIndex } from '../dal/event.js'

export default class WorkerDomain extends IndexerWorkerDomain {
  constructor(context) {
    super(context)
    this.eventsDAL = createEventDAL(context.dataPath)
  }

  // [...] Other methods

  async indexEVMLogs(blockchainId, context, entities) {
    console.log(`Index ${blockchainId} logs`, JSON.stringify(entities, null, 2))
 
     const entries = entities.map((e) => ({
      id: e.id,
      blockchain: blockchainId,
      address: e.address,
      height: e.height,
      content: e
    }))

    await this.eventsDAL.save(entries) //`save` method to store the incoming events
  }
}
```

This integration ensures that your indexer not only processes blockchain events but also stores them in a structured manner, making them readily accessible for querying and analysis through your API.

## 7. Exposing Data via GraphQL API
### 7.1 Defining GraphQL Schema
To make the indexed data accessible and queryable, you will expose it through a GraphQL API. Define your API schema by creating a GraphQL schema file. This schema specifies the types of data you can query and the queries themselves.

Create a new file schema.js inside the src/api directory with the following content to define your event query schema:

```js
// src/api/schema.js
import {
  GraphQLString,
  GraphQLNonNull,
  GraphQLObjectType,
  GraphQLList,
  GraphQLFloat,
  GraphQLInt,
  GraphQLBoolean,
} from 'graphql'
import { GraphQLLong, GraphQLJSONObject } from '@aleph-indexer/core'
import { IndexerAPISchema } from '@aleph-indexer/framework'

const EventQueryArgs = {
  blockchain: { type: new GraphQLNonNull(GraphQLString) },
  fromHeight: { type: GraphQLFloat },
  limit: { type: GraphQLInt },
  reverse: { type: GraphQLBoolean },
}

const Event = new GraphQLObjectType({
  name: 'Event',
  fields: {
    id: { type: new GraphQLNonNull(GraphQLString) },
    blockchain: { type: new GraphQLNonNull(GraphQLString) },
    address: { type: new GraphQLNonNull(GraphQLString) },
    height: { type: new GraphQLNonNull(GraphQLLong) },
    content: { type: new GraphQLNonNull(GraphQLJSONObject) },
  },
})
const EventList = new GraphQLList(Event)
const types = [Event]

export default class APISchema extends IndexerAPISchema {
  constructor(domain) {
    super(domain, {
      types,
      query: new GraphQLObjectType({
        name: 'Query',
        fields: {
          Events: {
            type: EventList,
            args: EventQueryArgs,
            resolve: (_, args) => this.domain.getEvents(args),
          },
        },
      })
    })
  }
}
```

Then add the absolute path to the config:

```js
// src/index.js
import indexer, { BlockchainChain } from '@aleph-indexer/framework'

indexer.init({
  ...,
  indexer: {
    main: {
      ...,
      apiSchemaPath: path.join(__dirname, './api/schema.js')
    },
  }
})
```

### 7.2 Domain Method Implementation for Data Retrieval
To facilitate data access through our GraphQL API, we implement domain methods that act as a bridge between the API layer and the domain logic. The APISchema class takes the indexer's main class as its first argument. This main class serves as the facade interface, orchestrating data retrieval by communicating with the appropriate worker instance.

Implementing getEvents in the Main Domain:

```js
// src/indexer/main.js
import { IndexerMainDomain } from '@aleph-indexer/framework'

export default class MainDomain extends IndexerMainDomain {
  // Other methods...

  async getEvents(args) {
    const { blockchain } = args;
    // Assuming a single account per blockchain for simplicity
    const [account] = this.accounts[blockchain].values();

    // Use the context API client to delegate the request to the corresponding worker
    const response = await this.context.apiClient
      .useBlockchain(blockchain)
      .invokeDomainMethod({
        account: account,
        method: 'getEvents',
        args: [args],
      });

    const returned = [];
    for await (const item of response) {
      returned.push(item);
    }

    return returned;
  }
}
```
This implementation fetches the specific account being tracked for a given blockchain ID, then uses the context API client to forward the request to the appropriate worker, along with any query parameters from the API request.

Retrieving Events in the Worker Class:
```js
// src/indexer/worker.js
import { IndexerWorkerDomain } from '@aleph-indexer/framework';
import { createEventDAL, eventDALIndex } from '../dal/event.js';

export default class WorkerDomain extends IndexerWorkerDomain {
  // Other methods...

  async getEvents(account, args) {
    let { blockchain, reverse = true, limit = 1000, fromHeight } = args;

    const from = reverse ? undefined : fromHeight;
    const to = reverse ? fromHeight : undefined;

    // Query the events database using the DAL, based on the provided arguments
    return await this.eventsDAL
      .useIndex(eventDALIndex.BlockchainHeight)
      .getAllValuesFromTo(
        [blockchain, from],
        [blockchain, to], {
          reverse, 
          limit 
        });
  }
}
```
In the worker class, we implement the getEvents method to query the database for events based on the provided criteria. This method utilizes the data access layer (DAL) configured for event storage, performing queries that respect the requested blockchain, direction (via reverse), limit, and height range.

> Note: In high-availability (HA) setups with multiple instances, each worker might manage a slice of the events database. This structure necessitates the use of the context API for inter-service communication, ensuring requests are routed to the correct worker based on the account being queried.

These domain methods enable efficient data retrieval from the indexer's storage, making the data accessible via the GraphQL API for client applications.

## 8. Querying the API
### 8.1 Example Queries
With the GraphQL API set up, you can now query the indexed blockchain events. Here's an example query you might run in the GraphiQL interface or send via a GraphQL client:

```gql
query {
  Events(
    blockchain: "ethereum-mainnet",
    reverse: false
    limit: 10
    fromHeight: 0
  ) {
    id
    height
    blockchain
    address
    content
  }
}
```
This query fetches the latest 10 events from the "ethereum-mainnet" blockchain, returning their IDs and data.

## 9. Finalizing and Running the Indexer
### 9.1 Recap of Project Structure
Ensure your project files and directories are organized as follows for optimal management and understanding:

```sh
my-awesome-indexer/
├── .env                # Environment variables for blockchain RPC URLs
├── package.json        # Node project configuration and dependencies
├── src/
│   ├── api/
│   │   └── schema.js   # Defines the GraphQL schema for the API
│   ├── dal/
│   │   └── event.js    # Data access layer for event storage
│   ├── indexer/
│   │   ├── main.js     # Main class for indexer setup and event tracking configuration
│   │   └── worker.js   # Worker class for processing and storing blockchain events
│   └── index.js        # Entry point for the project, sets up the web server and GraphQL API
└── node_modules/       # Installed packages
```
This structure supports a clear separation of concerns, making it easier to manage and extend your indexer.

## 10 Final
This guide has walked you through setting up an indexer for the ethereum blockchain, from initializing the project and configuring the indexer to storing event data and exposing it through a GraphQL API. With the provided structure and examples, you're well-equipped to customize and extend your indexer to suit your specific needs, whether by adding more blockchain networks, optimizing performance, or enhancing security.

### 10.1 Additional resources
- Development support: [https://t.me/alephim/119590](https://t.me/alephim/119590)
- Github: [https://github.com/aleph-im](https://github.com/aleph-im)
- Infrastructure documentation: [docs.aleph.im](https://docs.aleph.im)
- Web3 Cloud: [console.twentysix.cloud](https://console.twentysix.cloud)

### 10.2 Social
- X twentysix.cloud: [https://twitter.com/TwentySixCloud](https://twitter.com/TwentySixCloud)
- X aleph.im: [https://twitter.com/aleph_im](https://twitter.com/aleph_im)
- Community: [https://t.me/alephim](https://t.me/alephim)
- Medium: [https://medium.com/aleph-im](https://medium.com/aleph-im)

## 11 Example indexing other EVM networks (oasys homeverse)

After setting up the ethereum indexer we can add as many other networks and accounts to track as we wish. In this example we are going to index the oasys homeverse network using the same project. This means that our indexer will become multi-chain now allowing us to handle data from different networks on the same process, merging and processing this information to create derivated data that can be queryable from our graphql api or sent to an external queue service.

Here are the steps to add tracking of some homeverse accounts in both testnet and mainnet

### 11.1 In step 1.3 install this packages additionally

```sh
npm install @aleph-indexer/oasys-verse
```

### 11.2 In step 2.2 add the following config to the index.js file

```js
// src/index.js
import indexer, { BlockchainChain } from '@aleph-indexer/framework'

indexer.init({
  // [...]
  supportedBlockchains: [
    // [...],
    { chain: BlockchainChain.OasysVerse, id: 'homeverse-mainnet' },
    { chain: BlockchainChain.OasysVerse, id: 'homeverse-testnet' }
  ],
})
```

### 11.3 In step 4.2 configure the new accounts to be tracked on homeverse

```js
// src/indexer/main.js
import { IndexerMainDomain } from '@aleph-indexer/framework'

export default class MainDomain extends IndexerMainDomain {
  async init() {
    await super.init()
    await this.indexAccounts([
      // [...],
      {
        // The `Tokibune NFT (TBN)` contract on the network with id `homeverse-mainnet`
        blockchainId: 'homeverse-mainnet',
        account: '0x389B9c2873EdD077e6255D8ADdB748788aBAd0Ea',
        index: { logs: true },
      },
      {
        // The `AlephSync` contract on the network with id `homeverse-testnet`
        blockchainId: 'homeverse-testnet',
        account: '0xC0134b5B924c2FCA106eFB33C45446c466FBe03e',
        index: { logs: true },
      },
    ])
  }
}
```

### 11.4 In step 5.1 make sure to add the following env variables to properly configure homeverse networks 

```sh
# .env file
...

HOMEVERSE_TESTNET_RPC=https://rpc.testnet.oasys.homeverse.games
HOMEVERSE_TESTNET_EXPLORER_URL=https://explorer.testnet.oasys.homeverse.games/api?module=contract&action=getabi&address=$ADDRESS

HOMEVERSE_MAINNET_RPC=https://rpc.mainnet.oasys.homeverse.games
HOMEVERSE_MAINNET_EXPLORER_URL=https://explorer.oasys.homeverse.games/api?module=contract&action=getabi&address=$ADDRESS
```

### 11.5 In step 5.2 implement the handlers for the recently added networks

```js
// src/indexer/worker.js
import { IndexerWorkerDomain } from '@aleph-indexer/framework'

export default class WorkerDomain extends IndexerWorkerDomain {
  // [...]
  
  async homeverseTestnetFilterLog(context, entity) {
    return this.filterEVMLog('homeverse-testnet', context, entity)
  }

  async homeverseTestnetIndexLogs(context, entities) {
    return this.indexEVMLogs('homeverse-testnet', context, entities)
  }

  async homeverseMainnetFilterLog(context, entity) {
    return this.filterEVMLog('homeverse-mainnet', context, entity)
  }

  async homeverseMainnetIndexLogs(context, entities) {
    return this.indexEVMLogs('homeverse-mainnet', context, entities)
  }
}
```

This is an example of the new events coming from homeverse:

```json
{
  "address": "0xa0e728b37f645f32bFEDE3d36E3aA0BB2E23cC56",
  "topics": [
    "0x2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0d",
    "0x0000000000000000000000000000000000000000000000000000000000000000",
    "0x000000000000000000000000fb02e831013e9de926fa936becafc9cb107a4ef0",
    "0x000000000000000000000000fb02e831013e9de926fa936becafc9cb107a4ef0"
  ],
  "data": "0x",
  "blockNumber": 173758,
  "transactionHash": "0xca6a02b66edb3737675a7d9196c24665555caf2825ec16dcc14e115aef86316b",
  "transactionIndex": 0,
  "blockHash": "0x1ea319d259d0199f6cd83017ce18aed088240521a99834bf16934b1dbb4724b3",
  "logIndex": 0,
  "removed": false,
  "id": "173758_0xa0e728b37f645f32bfede3d36e3aa0bb2e23cc56_0",
  "height": 173758,
  "timestamp": 1705463689000,
  "parsed": {
    "eventFragment": {
      "name": "RoleGranted",
      "anonymous": false,
      "inputs": [
        {
          "name": "role",
          "type": "bytes32",
          "indexed": true,
          "components": null,
          "arrayLength": null,
          "arrayChildren": null,
          "baseType": "bytes32",
          "_isParamType": true
        },
        {
          "name": "account",
          "type": "address",
          "indexed": true,
          "components": null,
          "arrayLength": null,
          "arrayChildren": null,
          "baseType": "address",
          "_isParamType": true
        },
        {
          "name": "sender",
          "type": "address",
          "indexed": true,
          "components": null,
          "arrayLength": null,
          "arrayChildren": null,
          "baseType": "address",
          "_isParamType": true
        }
      ],
      "type": "event",
      "_isFragment": true
    },
    "name": "RoleGranted",
    "signature": "RoleGranted(bytes32,address,address)",
    "topic": "0x2f8788117e7eff1d82e926ec794901d17c78024a50270940304540a733656f0d",
    "args": [
      "0x0000000000000000000000000000000000000000000000000000000000000000",
      "0xfB02e831013e9de926fa936BeCAFC9cb107a4EF0",
      "0xfB02e831013e9de926fa936BeCAFC9cb107a4EF0"
    ]
  }
}
```

### 11.6 In step 8.1 now you can query the homeverse events changing the blockchain id on the graphql query

```gql
query {
  Events(
    blockchain: "homeverse-mainnet",
    reverse: false
    limit: 10
    fromHeight: 0
  ) {
    id
    height
    blockchain
    address
    content
  }
}
```
