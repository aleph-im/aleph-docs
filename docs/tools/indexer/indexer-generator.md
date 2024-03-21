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
```bash
npm i && npm run build
npm run start <program-name>
```

If you wait for a moment you will see a message warning you that it is now running a GraphQL server on [http://localhost:8080](http://localhost:8080).

## Deploying your Indexer to Aleph.im
To deploy your indexer, read this [documentation](https://github.com/aleph-im/aleph-indexer-library?tab=readme-ov-file#building-and-deploying-an-indexer)

## Supported Queries
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
    }
}
```

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
  accountState(account: "8szGkuLTAux9XMgZ2vtY39jVSowEcpBfFfD8hXSEqdGC", blockchain: solana, type: transaction) {
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
  accountStats(account: "7ekbc8F72Zm4KKQwbgSe7UTaiprHb8nkmbA2ti5hKoCX", blockchain: solana) {
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
  accountTimeSeriesStats(timeFrame:Month, account: "7ekbc8F72Zm4KKQwbgSe7UTaiprHb8nkmbA2ti5hKoCX", type: "access", blockchain: solana) {
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
