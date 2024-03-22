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

| Property                   | Description                                                                        |
|----------------------------|------------------------------------------------------------------------------------|
| `totalAccounts`            | The amount of indexed accounts by account type                                     |
| `totalAccesses`            | The total amount of events registered across all program accounts                  |
| `totalAccessesByProgramId` | The amount of events registered by each signer (user) interacting with the program |
| `startTimestamp`           | The timestamp of the first indexed event                                           |
| `endTimestamp`             | The timestamp of the last indexed event                                            |

### Accounts
Get all accounts, their addresses, Anchor IDL type and contents:

```graphql
{
  accounts {
    name
    programId
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

| Property    | Description                                                            |
|-------------|------------------------------------------------------------------------|
| `name`      | Indexer-assigned name of the account. By default, it is the `address`. |
| `address`   | Address of the account.                                                |
| `type`      | Type of the account. Possible types depend on the IDLs definitions.    |
| `programId` | Which program created the account. Usually the one the IDL belongs to. |
| `data`      | Parsed data from the account. Properties depend on its `type`.         |

### Indexing state
Get the current progress of the indexer. The indexer first fetches all transaction signatures recorded involving given account,
then fetches the actual transactions and processes them as events into the database.

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

| Property    | Description                                                                                                                   |
|-------------|-------------------------------------------------------------------------------------------------------------------------------|
| `accurate`  | If the indexer has fetched all transactions signatures in order for the progress to be accurate.                              |
| `progress`  | How much percent of all transactions have been fetched and processed. Is measured relative to fetched transaction signatures. |
| `pending`   | Shows which time spans of transactions are waiting to be fetched and processed.                                               |
| `processed` | Shows which time span has already been processed.                                                                             |

### General account stats
By default, the generator creates code to calculate stats for the last 1 hour, 24 hours, 7 days, and total for how many times
an account has been accessed, meaning how many times an instruction has been invoked involving the account:

```graphql
{
  accountStats(account: "7ekbc8F72Zm4KKQwbgSe7UTaiprHb8nkmbA2ti5hKoCX", blockchain: "solana", type: "access") {
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
        accessesByProgramId
        startTimestamp
        endTimestamp
      }
    }
  }
}
```

| Property              | Description                                                     |
|-----------------------|-----------------------------------------------------------------|
| `last1h`              | Stats for the last hour.                                        |
| `last24h`             | Stats for the last 24 hours.                                    |
| `last7d`              | Stats for the last 7 days.                                      |
| `total`               | Total aggregated stats.                                         |
| `accesses`            | Amount of accesses. Available on all time spans.                |
| `accessesByProgramId` | Amount of accesses by each signer. Available on all time spans. |
| `startTimestamp`      | The timestamp of the first indexed event during the time span.  |
| `endTimestamp`        | The timestamp of the last indexed event during the time span.   |

### Account time series stats
Similar to the general account stats, but returns a time series of stats for a given account and time frame:
```graphql
{
  accountTimeSeriesStats(timeFrame: Month, account: "7ekbc8F72Zm4KKQwbgSe7UTaiprHb8nkmbA2ti5hKoCX", type: "access", blockchain: "solana") {
    series {
      date
      value {
        ...on AccessTimeStats {
          accesses
          accessesByProgramId
          startTimestamp
          endTimestamp
        }
      }
    }
  }
}
```

| Property | Description                                       |
|----------|---------------------------------------------------|
| `date`   | The beginning timestamp of the time series entry. |
| `value`  | The stats for the given timestamp.                |

### Processed instructions (Events)
Get the latest ten processed `OrderUnstake` instructions (events) for a given account:

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

| Property       | Description                         |
|----------------|-------------------------------------|
| `id`           | The unique identifier of the event. |
| `timestamp`    | The timestamp of the event.         |
| `type`         | The Anchor IDL type of the event.   |
| `signer`       | The signer of the event.            |
| `info`         | The parsed data of the event.       |

## Architecture
The indexer generator creates all the necessary files to run a Solana indexer without any additional coding required.
In case you want to modify the indexer, you can do so by editing the generated files in the `packages/<idl-name>` directory.

The indexer generator creates the following directories/files in the `src` directory:

- [`api`](#graphql-schema): Contains the GraphQL schema and resolvers
- [`dal` ](#data-access-layer): Contains the data access layer and database models
- [`domain`](#business-logic): Contains the business logic (worker loop, account discovery, statistics calculation)
- [`parsers`](#event-parser): Contains the event parser which transforms a parsed Solana instruction into a business event
- [`utils/layouts`](#layouts): Contains the basic Solana layout definitions and types for accounts and instructions, generated from the IDL
- `constants.ts`: Contains the indexer's constants, like the program ID
- `types.ts`: Contains the extended types, like account and statistics types

**Note:** If you want to add more functionality from scratch to the indexer, you should also check out the [EVM Indexer Guide](evm-indexer.md#3-indexer-services-and-architecture).
This architecture overview only covers the basic structure of the generated Solana indexer.

### GraphQL Schema
The GraphQL schema is generated from the IDL and contains basic queries and types to interact with the indexer.
Example queries are provided in the [Supported Queries](#supported-queries) section.

#### APISchema
The generated `APISchema` class in `schema.ts` inherits from the `IndexerAPISchema` class, provided by the Aleph Indexer Framework.

Three types of queries are defined by the Indexer Generator:

- `accounts`: Returns all accounts and their data
- `events`: Returns all events of a given type for a given account
- `globalStats`: Returns global statistics about the indexed program

As you probably noticed, there are queries that are not generated by the Indexer Generator, but are part of the Aleph Indexer Framework:

- `accountState`: Returns the current progress of the indexer
- `accountStats`: Returns general account stats
- `accountTimeSeriesStats`: Returns a time series of stats for a given account and time frame

You can modify the `accountStats` and `accountTimeSeriesStats` queries to return different stats or add new queries
to the schema by modifying the `customStatsType` and `customTimeSeriesTypesMap` properties in the `APISchema` class.
The `customTimeSeriesTypesMap` is a map of the stats type identifier to the corresponding time series stats type:

```typescript
// This is generated by default
customTimeSeriesTypesMap: { access: Types.AccessTimeStats }
```

#### Resolvers
The resolvers are defined in the `resolvers.ts` file and are responsible for fetching the data from the [`MainDomain`](#maindomain) class and returning it to the client.

#### Types
The `types.ts` file contains the `GraphQLObjectType` definitions for the queries and types defined in the schema.

### Data Access Layer
The Data Access Layer (DAL) is responsible for interacting with the database and storing the indexed data.
The DAL is based on [LevelDB](https://github.com/google/leveldb), a fast key-value storage engine, and extended by the framework to support indexes and mapping functions.

#### Define a DAL
By default, the Indexer Generator only creates the `EventStorage` class, which is responsible for storing the events in the database.
A DAL needs a name, path, primary key, optionally indexes, and potentially a map function to correctly store and retrieve BigNumbers/BNs.
The generated `EventStorage` class is very similar to the [basic example](evm-indexer.md#6-data-storage) provided in the EVM Indexer Guide.

```typescript
export type EventStorage = EntityStorage<MarinadeFinanceEvent>

// [...] generated keys

export function createEventDAL(path: string): EventStorage {
  return new EntityStorage<MarinadeFinanceEvent>({
    name: 'event',
    path,
    key: [idKey],  // The primary key of the event
    indexes: [
      {
        name: EventDALIndex.AccountTimestamp,
        key: [accountKey, timestampKey],  // Index for faster retrieval
      },
      {
        name: EventDALIndex.AccountTypeTimestamp,
        key: [accountKey, typeKey, timestampKey],
      },
    ],
    // [...] generated mapFn for correctly storing and retrieving BigNumbers/BNs
  })
}
```

#### Use the DAL
Use the `EventStorage` class to store the events in the database like this:

```typescript
const eventStorage = createEventDAL('path/to/db')
await eventStorage.save(event)
```

Query the events from an index like in this example of the generated `AccountDomain` class:

```typescript
export class AccountDomain {
  
  // [...] generated methods
  
  async getEventsByTime(
    startDate: number,
    endDate: number,
    opts: any,
  ): Promise<StorageStream<string, MarinadeFinanceEvent>> {
    return await this.eventDAL
      .useIndex(EventDALIndex.AccountTimestamp)
      .getAllFromTo(
        [this.info.address, startDate],
        [this.info.address, endDate],
        opts,
      )
  }
}
```

Where opts can contain the following properties:

```typescript
const opts = {
  limit: 10,
  reverse: true,
}
```

The `.getAllFromTo` method returns a `StorageStream` object, which is an async iterable that can be used in a `for await` loop:

```typescript
for await (const event of accountDomain.getEventsByTime(0, Date.now(), opts)) {
  console.log(event)
}
```

The passed arrays are the start and end keys of the index, in which between (and including) the two keys the events are fetched.

### Business Logic
The `domain` directory contains multiple central classes that are responsible for the business logic of the indexer.

#### MainDomain
The `MainDomain` class is the central class of the indexer and is responsible for the worker loop, account discovery, and statistics calculation.

It configures the `discoveryInterval` and `stats` interval, which are the intervals in milliseconds in which the account discovery and statistics calculation are executed.

Furthermore, a `discoverAccounts` method is provided, which is called in the worker loop and is responsible for discovering new accounts and adding them to be indexed in their own `AccountDomain`.
Usually, the discovery process is more complex and therefore has its own discoverer class. A working example is generated in the `domain/discoverer` directory.

See [the EVM Guide's section on event handling](evm-indexer.md#4-event-tracking-and-handling) for more information on how these domain classes work.

#### WorkerDomain
The `WorkerDomain` class takes actual care of the worker loop and is responsible for the worker's lifecycle.
This includes filtering and parsing instructions, adding new accounts to the indexer and retrieving their `AccountDomain`s.

An interesting method in the `WorkerDomain` class is `onNewAccount`:

```typescript
export default class WorkerDomain
  extends IndexerWorkerDomain
  implements SolanaIndexerWorkerDomainI, IndexerWorkerDomainWithStats {
  
  // [...] generated methods and constructor
  
  async onNewAccount(
    config: AccountIndexerConfigWithMeta<MarinadeFinanceAccountInfo>,
  ): Promise<void> {
    const {blockchainId, account, meta} = config
    const {apiClient} = this.context

    const accountTimeSeries = await createAccountStats(
      blockchainId,
      account,
      apiClient,
      this.eventDAL,
      this.statsStateDAL,
      this.statsTimeSeriesDAL,
    )

    this.accounts[account] = new AccountDomain(
      meta,
      this.eventDAL,
      accountTimeSeries,
    )

    console.log('Account indexing', this.context.instanceName, account)
  }
}
```

It is called when a new account is discovered and is responsible for creating a new `AccountDomain` for the account and storing it in the `accounts` object.
You can trigger additional actions here, like setting up additional stats calculations, sending a notification or logging the event.

See [the EVM Guide's section on implementing event handling](evm-indexer.md#52-implementing-event-handlers) for more information on how to implement event handlers in the `WorkerDomain`.

#### AccountDomain
The `AccountDomain` class is responsible for the business logic of a single account.
It contains methods to fetch account events, calculate retrieve account statistics, and holds the DAL as well stats classes.

#### Statistics Calculation
The `domain/stats` directory contains classes that are responsible for calculating the accounts' recent statistics and time series statistics.

While the `statsAggregator.ts` and `timeSeries.ts` both define which events should be aggregated to generate certain stats objects,
the `timeSeriesAggregator.ts` class is responsible for calculating the time series stats from the events.

This happens in the `processAccessStats` method, which has a monadic signature:

```typescript
  protected processAccessStats(
    acc: AccessTimeStats,
    curr: MarinadeFinanceEvent | AccessTimeStats,
  ): AccessTimeStats
```

You need to make sure that everything that goes into the `curr` object is correctly handles and integrated into the `acc` object, which will be the final result of the aggregation.

**Note:** Events can sometimes be out of order, so you need to make sure that the aggregation is idempotent and can handle out-of-order events!

### Event Parser
The `parsers` directory contains the event parser, which is responsible for transforming a parsed Solana instruction into a business event.

Parsed Solana instruction means, that the encoded instruction data/parameters are decoded and transformed into a more human-readable format through the [provided layouts of the IDL](#layouts).

You may modify the way the events are built, in case you need additional data from the instruction or its overarching transaction.
This information is available in the `parse` method's `ixCtx` parameter:

```typescript
  parse(
    ixCtx: SolanaParsedInstructionContext,
    account: string,
  ): MarinadeFinanceEvent {
    const { instruction, parentInstruction, parentTransaction } = ixCtx
```

### Layouts
The `utils/layouts` directory contains the basic Solana layout definitions and types for accounts and instructions, generated from the IDL.

It is generally not advised to modify these files, as they are generated from the IDL and should be kept in sync with the IDL.

## Conclusion
The Aleph Indexer Generator simplifies the process of creating Solana indexers by generating all necessary boilerplate code.
It provides a solid foundation for building a Solana indexer and can be extended with additional functionality following the provided architecture or the [EVM Indexer Guide](evm-indexer.md).

If you have any questions or need help with the indexer generator, feel free to reach out to us on [Telegram](https://t.me/alephim) or open an issue on the [GitHub repository](https://github.com/aleph-im/aleph-indexer-library/issues).
