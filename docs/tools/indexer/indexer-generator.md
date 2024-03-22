# Generate Solana Indexers from IDL

The Aleph Indexer Generator simplifies the process of creating indexers for Solana programs, by using Anchor's IDLs. It generates the necessary boilerplate code for launching your own Solana indexer on our [open-source, multi-threaded node.js framework](https://github.com/aleph-im/aleph-indexer-framework), using [moleculer](https://moleculer.services/).

## Getting started
### 1. Clone the repository
```bash
git clone https://github.com/aleph-im/solana-indexer-library.git
```

### 2. Navigate to the project's root directory
```bash
cd solana-indexer-library
```

### 3. Install the necessary dependencies and build the project:
```bash
npm install && npm run build
```

### 4. Generate your indexer from a local or remote Anchor IDL:
#### Using local IDL file
1. Move a copy of the idl of your program to the path:
```bash
solana-indexer-library/src/idl/<idl-name>.json
```
2. Run the generate command, passing the IDL name as an argument:
```bash
npm run generate <idl-name>
```
3. Optionally, include your program's address as a second argument:
```bash
npm run generate <idl-name> <program-address>
``` 

#### Remote IDL
1. Ensure [Anchor](https://www.anchor-lang.com/docs/installation) is installed locally and that the program you want to index has an initialized IDL account. A simple way to check for this is to run the following command:
```bash
anchor idl fetch <program-address>
```
This way you can also retrieve the IDL file from the program's address:
```bash
anchor idl fetch -o <out-file.json> <program-address>
```
2. If it is your own program, you can use the following command to initialize the IDL account:
```bash
anchor idl init -f <target/idl/program-name.json> <program-address>
```
3. Run the generate command of the indexer generator, providing your program's address:
```bash
npm run generate <program-address>
``` 

## Run the indexer
1. Navigate to the generate package directory
```bash
cd packages/<idl-name>
```
2. Install dependencies and build the package
```bash
npm i && npm run build
```
3. Add your RPC on SOLANA_RPC (and SOLANA_MAIN_PUBLIC_RPC, if you get rate-limit problems) to the .env file
```bash
SOLANA_RPC=<your-rpc-url>
SOLANA_MAIN_PUBLIC_RPC=<your-rpc-url>
```
4. Run the npm start command
```bash
npm run start
```

If you wait for a moment you will see a message warning you that it is now running a GraphQL server on [http://localhost:8080](http://localhost:8080).

## Deploying your Indexer to Aleph.im
To deploy your indexer, read this [documentation](https://github.com/aleph-im/aleph-indexer-library?tab=readme-ov-file#building-and-deploying-an-indexer)

## Supported Queries
For these example queries, we generated an indexer for the [Marinade Finance Liquid Staking Program](https://github.com/marinade-finance/liquid-staking-program) using:
```bash
npm run generate MarBmsSgKXdrN1egZf5sqe1TMai9K1rChYNDJgjq7aD
```

**Note:** Before doing any queries, let the indexer run for a while to fetch some data.
It starts fetching the latest transactions and continues back in time until it indexes all transactions.
In the meantime, new transactions are fetched and indexed in real-time.

### Total program accounts and instruction invocations
Return global stats about the amount of accounts and total amount of instructions processed by the indexer:
```graphql
{
    globalStats {
        totalAccounts {
            State
            TicketAccountData
        }
        totalAccesses
        totalAccessesByProgramId
        startTimestamp
        endTimestamp
    }
}
```

| Property                 | Description                                                                        |
|--------------------------|------------------------------------------------------------------------------------|
| totalAccounts            | The amount of indexed accounts by account type                                     |
| totalAccesses            | The total amount of events registered across all program accounts                  |
| totalAccessesByProgramId | The amount of events registered by each signer (user) interacting with the program |
| startTimestamp           | The timestamp of the first indexed event                                           |
| endTimestamp             | The timestamp of the last indexed event                                            |

### Accounts
Get all accounts, their addresses, Anchor type and contents:
```graphql
{
  accounts {
    address
    type
    data {
      ...on State {
        msolMint
        adminAuthority
        liqPool {
          lpLiquidityTarget
          lpMaxFee {
            basisPoints
          }
          lpMinFee {
            basisPoints
          }
          treasuryCut {
            basisPoints
          }
        }
        # and other fields, see generated GraphQL schema
      }
      ... on TicketAccountData {
        beneficiary
        stateAddress
        lamportsAmount
        # and other fields, see generated GraphQL schema
      }
    }
  }
}
```

### Indexing state
Get the current progress of the indexer. Accurate means that the indexer fetched all transaction signatures belonging to
that account, progress tells you how much percent of all transactions have been fetched and processed.
```graphql
{
  accountState(account: "8szGkuLTAux9XMgZ2vtY39jVSowEcpBfFfD8hXSEqdGC", blockchain: "solana", type: transaction) {
    accurate
    progress
    pending
    processed
  }
}
```

### General account stats
Get accesses in the last hour, day, week or in total:
```graphql
{
  accountStats(account: "7ekbc8F72Zm4KKQwbgSe7UTaiprHb8nkmbA2ti5hKoCX", blockchain: "solana") {
    stats {
      last1h {
        accesses
      }
      last24h {
        accesses
      }
      last7d {
        accesses
      }
      total {
        accesses
      }
    }
  }
}
```

### Account time series stats
Get aggregated accesses by signing wallet and month:
```graphql
{
  accountTimeSeriesStats(timeFrame:Month, account: "7ekbc8F72Zm4KKQwbgSe7UTaiprHb8nkmbA2ti5hKoCX", type: "access", blockchain: "solana") {
    series {
      date
      value {
        ...on AccessTimeStats {
          accessesByProgramId
        }
      }
    }
  }
}
```

### Processed instructions (Events)
Get the latest 1000 processed instructions:
```graphql
{
  events(account: "7ekbc8F72Zm4KKQwbgSe7UTaiprHb8nkmbA2ti5hKoCX", types: OrderUnstake, limit: 10) {
    id
    timestamp
    type
    signer
    ...on OrderUnstakeEvent {
      info {
        state
        msolAmount
        burnMsolFrom
        burnMsolAuthority
        newTicketAccount
      }
    }
  }
}
```

## Architecture
The indexer generator creates all the necessary files to run a Solana indexer without any additional coding required.
In case you want to modify the indexer, you can do so by editing the generated files in the `packages/<idl-name>` directory.

The indexer generator creates the following directories/files in the `src` directory:

- `api`: Contains the GraphQL schema and resolvers
- `dal`: Contains the data access layer and database models
- `domain`: Contains the business logic (worker loop, account discovery, statistics calculation)
- `parsers`: Contains the event parser which transforms a parsed Solana instruction into a business event
- `utils/layouts`: Contains the basic Solana layout definitions and types for accounts and instructions, generated from the IDL
- `constants.ts`: Contains the indexer's constants, like the program ID
- `types.ts`: Contains the extended types, like account and statistics types

### GraphQL schema
The GraphQL schema is generated from the IDL and contains basic queries and types to interact with the indexer.
Example queries are provided in the [Supported Queries](#supported-queries) section.