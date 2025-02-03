# Computing on Aleph.im

Aleph.im offers a decentralized computing framework that allows users to run
applications on the network.

Two execution models are available:

 - [Functions](../guides/python/getting_started.md#understanding-alephim-programs) follow a serverless 
   approach to easily deploy and maintain applications.
 - [Instances](../guides/python/getting_started.md#understanding-alephim-instances) are designed to 
   provide a persistent environment for users to interact with directly.

In both cases, user workloads are executed inside virtual machines (VMs)
isolated from each other.

## Overview of VMsS

There are several types of VMs available on the network:

- [On-demand VM](#on-demand-execution)
- [Persistent VM](#persistent-execution)
- [Instance VM](#instance-vms)

An [On-demand VM](#on-demand-execution) is created on a [Compute Resource Node](../nodes/compute/index.md)
(CRN) and is destroyed once the program has finished executing. This is great
for programs that are responding to user requests or API calls (using ASGI) and can shutdown
after processing the event. They are also cheaper to run as they only require
one tenth of the $ALEPH tokens to hold, compared to a [Persistent VM](#persistent-execution).

A [Persistent VM](#persistent-execution) can be used to run programs that cannot afford to stop or need
to handle incoming connections such as polling data from a websocket or AMQP API.

Instances are similar to Persistent VMs, but are specifically designed to run with
a SSH key supplied by the user. This allows the user to connect to the VM and
interact with it directly. They do not rely on code execution, but rather on
the user's ability to connect to the VM and run commands on it.
They cost as much as Persistent VMs.

## On-demand Execution

On how to deploy a simple Python microVM, see our [Python microVM guide](../guides/python/getting_started.md)

## Persistent Execution

When a program is created with persistent execution enabled, the aleph.im scheduler will find a Compute Resource Node
(CRN) with enough resources to run the program and schedule the program to start on that node.

Persistent programs are designed to always run exactly once, and the scheduler will reallocate the program on another
CRN would the current one go offline. 

> ⚠️ Automatic data migration across hosts in case such events happen is not available yet.

### Message Specification

The execution model of a program is defined in the field `message.content.on` of messages of type `PROGRAM` and is 
non exclusive. The same program can therefore be available as both persistent instance and on demand at the same time.

```javascript
message = {
    ...,
    "content": {
        ...,
        "on": {
          "http": false,
          "persistent": true
        },
        "resources": {
          "vcpus": 1,
          "memory": 128,
        }
    }
}
```

### Prerequisites

Before you begin this tutorial, ensure that you have the following:

* A computer with Python and the [aleph-client](https://github.com/aleph-im/aleph-client/) utility installed
* An Ethereum account with at least 2000 ALEPH token
* Working knowledge of Python

## Step 1: Create your program

Let's consider the following example from the 
  [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/first-steps/). Any other ASGI compatible 
Python framework should work as well.

> Running programs written in any language that works on Linux is possible. This will be documented later.

Create a file named `src/main.py`:
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Test the application locally:
```shell
cd ./src/
uvicorn main:app --reload
```

### Step 2: Run a program in a persistent manner

To run the program in a persistent manner on the aleph.im network, use: 

```shell
aleph program upload --persistent ./src/ main:app
```

You can stop the execution of the program using:

```shell
aleph unpersist $MESSAGE_ID
```

### Find your program

TODO: Locate the CRN where your program is running.

## Instance VMs

TODO: Document Instance VMs