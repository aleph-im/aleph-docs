# Build a Python microVM

This tutorial will guide you through the steps of building a Python microVM to run on the aleph.im network.
We will build a simple HTTP server and add features as we go.

> ℹ This tutorial uses the aleph.im command line interface.

## Requirements

We expect you to know a little Python and have some experience with Python web frameworks such as
[FastAPI](https://fastapi.tiangolo.com/) or Flask. 
The first chapters of the [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/) should cover
enough to get started.

To complete this tutorial, you will use the `aleph` command from 
[aleph-client](../../tools/aleph-client/index.md), the `fastapi` framework to create a
simple API and the `uvicorn` server to test your program on your desktop before uploading it on 
aleph.im.

First, you need a recent version of Python and [pip](https://pip.pypa.io/en/stable/), 
preferably running on Debian 11 or Ubuntu 20.04.

Some cryptographic functionalities of aleph.im use curve secp256k1 and require installing [libsecp256k1](https://github.com/bitcoin-core/secp256k1).
Archiving programs and volumes requires
[Squashfs user space tools](https://github.com/plougher/squashfs-tools).

- Linux: 
``` 
sudo apt-get install -y python-pip libsecp256k1-dev squashfs-tools
``` 

- macOs: 
``` 
brew tap cuber/homebrew-libsecp256k1
brew install libsecp256k1 squashfs
```

You will also need [Uvicorn](https://www.uvicorn.org/) for local testing 
and the [Python aleph.im client](https://github.com/aleph-im/aleph-client) for it's command-line tools:

- Linux/macOs:

``` 
pip3 install "uvicorn[standard]" aleph-client fastapi eth_account
```

## Understanding aleph.im programs

Aleph.im programs are applications running on the aleph.im network.
Each program defines the application to be executed, data to use, computing requirements 
(number of CPUs, amount of RAM) and many more parameters.

Each program is instantiated as a __virtual machine__ running on a Compute Resource Node (CRN).
Virtual machines are emulated computer systems with dedicated resources that run isolated from each other.
Aleph.im Virtual Machines (VMs) are based on Linux.

We support two types of allocation: _on-demand_ and _persistent_. 
_on-demand_ boot extremely fast and can be launched on demand. They are perfect for lightweight applications
that only run once in a while.
_persistent_ functions on the other hand are constantly running, making them suited to run larger applications.

An [On-demand VM](#on-demand-execution) is created on a [Compute Resource Node](../../nodes/compute/index.md)
(CRN) and is destroyed once the program has finished executing. This is great
for programs that are responding to user requests or API calls (using ASGI) and can shutdown
after processing the event. They are also cheaper to run as they only require
one tenth of the $ALEPH tokens to hold, compared to a [Persistent VM](#persistent-execution).

### Runtimes

The base of each VM is a Linux 
[root filesystem](https://en.wikipedia.org/wiki/Root_directory) named __runtime__ and configured
to run programs on the aleph.im platform. 

Aleph.im provides a supported runtime to launch programs written in Python or binaries. 

- Python programs must support the [ASGI interface](https://asgi.readthedocs.io/en/latest/), described in the example below.
- Binaries must listen for HTTP requests on port 8080

You can find runtimes currently supported by aleph.im [here](../../computing/runtimes/index.md#existing-runtimes).

### Volumes

VMs can be extended by specifying additional volumes that will be mounted in the system. 

**Read-only volumes** are useful to separate Python virtual environments, Javascript _node_modules_ 
or static data from the program itself. These volumes can be updated independently of the 
program and the runtime, and maintained by a third party.

**Ephemeral volumes** provide temporary disk storage to a VM during its execution without requiring
more memory.

**Host persistent volumes** are persisted on the VM execution node, but may be garbage collected
by the node without warning.

**Store persistent volumes** (not available yet) are persisted on the aleph.im network. 
New VMs will try to use the latest version of this volume, with no guarantee against conflicts.

## Write a Python program

To create the first program, open your favourite code editor and create a directory named
`my-program`, containing a file named `main.py`.

```
.
└── my-program/
    └── main.py
```

Then write the following code in the file:
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

That's it for your first program.

This code comes from the [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/first-steps/).
Have a look at it for a better understanding of what it does and how it works.

## Test it locally

Before uploading your program on aleph.im, let's test it on your machine.

Aleph.im uses the standard [ASGI interface](https://asgi.readthedocs.io/en/latest/introduction.html) to
interface with programs written in Python. ASGI interfaces with many Python frameworks, including
FastAPI but also [Django](https://www.djangoproject.com/) 
or [Quart](https://github.com/pgjones/quart).

Test your program locally using uvicorn, an ASGI server:

```shell
uvicorn main:app --reload
```

If you are on macOS you can use vagrant to emulate a Linux system:
```shell
vagrant ssh
```

Then go to your working repository and launch:

```shell
python -m uvicorn main:app --reload --host=0.0.0.0
```

Then open `http://127.0.0.1:8000`. 
The `--reload` option will automatically reload your app when the code changes.

> ℹ️ If you are running this on a different system than your desktop, specify the IP address of 
> that system using `uvicorn main:app --reload --host 1.2.3.4`, where `1.2.3.4` is the IP address
> of the system.
> Then open your browser on http://1.2.3.4:8000 instead.

> ℹ Installing uvicorn should add the `uvicorn` command to your shell. If it does not, use
> `python -m uvicorn` to run it.

## Upload your program on aleph.im

After installing [aleph-client](../../tools/aleph-client/index.md), you should have access to the `aleph` command:

```shell
aleph --help
```

Let's upload our program.
The `aleph program CODE_DIR ENTRYPOINT` command will package the `CODE_DIR` code directory and configure the program
to run the `ENTRYPOINT` command.
For Python programs, `ENTRYPOINT` can be the module path to an ASGI application.

This command will upload our Python code and configure `main:app` as the ASGI application.

```shell
aleph program upload ./my-program main:app
```

Press Enter at the following prompt to use the default runtime:
```
Ref of runtime ? [bd79839bf96e595a06da5ac0b6ba51dea6f7e2591bb913deccded04d831d29f4]
```

You should then get a response similar to the following: 
```
Your program has been uploaded on aleph.im .

Available on:
  https://aleph.sh/vm/1d3842fc4257c0fd4f9c7d5c55bba16264de8d44f47265a14f8f6eb4d542dda2
  https://du4ef7cck7ap2t44pvoflo5bmjsn5dke6rzglikpr5xljvkc3wra.aleph.sh
Visualise on:
  https://explorer.aleph.im/address/ETH/0x101d8D16372dBf5f1614adaE95Ee5CCE61998Fc9/message/PROGRAM/1d3842fc4257c0fd4f9c7d5c55bba16264de8d44f47265a14f8f6eb4d542dda2
```

You may get the warning `Message failed to publish on IPFS and/or P2P`. 
This is common and usually not an issue.

> ℹ The second URL uses a hostname dedicated to your VM. Aleph.im identifiers are too long to work
> for URL subdomains, so a base32 encoded version of the identifier is used instead.

> ℹ You can make your own domain point to the VM. See the [advanced](./advanced.md) section.

## Run your program

You can now run your program by opening one of the URLs above. Each URL is unique for one program.

https://aleph.sh/vm/1d3842fc4257c0fd4f9c7d5c55bba16264de8d44f47265a14f8f6eb4d542dda2

This will automatically start your program inside a VM on the aleph.im Compute Resource Node behind
the `aleph.sh` domain name and serve your request.

An important thing to notice is that we did not install any specific dependency for our program,
despite relying on FastAPI.
This is because the official aleph.im runtime is already pre-configured with several typical Python packages.
Of course, you can customize your program to add your own requirements.
Refer to [Adding Python dependencies to a program](./dependency_volume.md) for more information.

## Next steps

Check out the [dependency volume](./dependency_volume.md) page to add additional Python packages to your 
program from the Python Package Index ([PyPI](https://www.pypi.org)). 

Check out [Building a Rust microVM](../rust/rust_microvm.md) to run a program written in another language than Python.

Check out [Advanced Python program features](./advanced.md) for more options and capabilities.
