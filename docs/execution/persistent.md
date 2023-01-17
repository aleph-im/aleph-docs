# Persistent Execution

## Introduction

The Aleph.im network can run programs in two different manners:

* [on-demand execution](on_demand.md) runs programs only when needed, saving on resources. This is great to run programs
  that are responding to user requests or API calls and can shutdown after processing the event.
* __persistent execution__ runs programs continuously.  These are always running and great to run programs that cannot
  afford to stop or need to handle incoming connections such as polling data from a websocket or AMQP API.

When a program is created with persistent execution enabled, the Aleph.im scheduler will find a Compute Resource Node
(CRN) with enough resources to run the program and schedule the program to start on that node.

Persistent programs are designed to always run exactly once, and the scheduler will reallocate the program on another
CRN would the current one go offline. 

> ⚠️ Automatic data migration across hosts in case such events happen is not available yet.

## Message Specification

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

## Prerequisites

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

## Step 2: Run a program in a persistent manner

To run the program in a persistent manner on the Aleph.im network, use: 

```shell
aleph program upload --persistent ./src/ main:app
```

You can stop the execution of the program using:

```shell
aleph unpersist $MESSAGE_ID
```

## Find your program

TODO: Locate the CRN where your program is running.

## Conclusion

In this tutorial, you learned how to create and deploy persistent Virtual Machines on the Aleph.im network. You should now have a better understanding of how to use Aleph.im for distributed computing.