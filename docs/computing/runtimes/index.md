# Introduction

A program runtime is an operating system and software stack that enables your program to run on the aleph.im network.

Runtimes are customized Linux root filesystems that integrate with the aleph.im infrastructure and provide access to
APIs, as well as quick responses to HTTP requests and other events.

The project provides official runtimes with all you need for most programs. Additionally, you can build and publish
custom runtimes, and use any available runtime on the network for your program.

- [Use existing runtimes](#existing-runtimes)
- [Create custom runtimes](./custom.md)

## Existing Runtimes

### Official runtime with Debian 11, Python 3.9 and NodeJS 14

Aleph.im provides users with a default runtime based on [Debian 11 "bullseye"](https://wiki.debian.org/DebianBullseye),
the current stable version of the Debian project which can
be [found on the Explorer](https://explorer.aleph.im/address/ETH/0x101d8D16372dBf5f1614adaE95Ee5CCE61998Fc9/message/STORE/bd79839bf96e595a06da5ac0b6ba51dea6f7e2591bb913deccded04d831d29f4).
This runtime is built with software available in the distribution, including Python 3.9 and Nodejs 14.

To optimize performance, this runtime uses a custom [Linux init](https://en.wikipedia.org/wiki/Init) process. This
process is specially designed to quickly launch the right endpoint in response to events such as HTTP requests. This is
especially useful when using [on-demand execution](../index.md#on-demand-execution).

[//]: # (Not available yet)

[//]: # (### Official minimal runtime for binaries &#40;Rust, Go, ...&#41;)

[//]: # ()

[//]: # (This official minimal runtime is designed to run Linux binaries quickly and efficiently. It is built on a minimal)

[//]: # (system, and does not include interpreters or virtual machines for popular programming languages. This makes launching)

[//]: # (binaries fast and efficient.)

### Third-party runtimes

Use third-party runtimes available on the network by specifying their `item_hash` when creating your program.

## Init process

[On-demand Execution](../index.md#on-demand-execution) relies on a custom [Linux init](https://en.wikipedia.org/wiki/Init) process,
optimized to launch the right endpoint in response to events such as HTTP requests. This custom init consists in two
simple programs, 
[init0.sh](https://raw.githubusercontent.com/aleph-im/aleph-vm/main/runtimes/aleph-alpine-3.13-python/init0.sh) 
and [init1.py](https://raw.githubusercontent.com/aleph-im/aleph-vm/main/runtimes/aleph-alpine-3.13-python/init1.py).

Use these in your custom runtime by copying them to `/rootfs/sbin/init` and 
`/mnt/rootfs/root/init1.py` respectively.

[Persistent Execution](../index.md#persistent-execution) may use the same init process, but this is not required. If you do not make use
of the capabilities provided by the aleph.im ecosystem, using the default of your distribution 
(ex: [systemd](https://systemd.io/), [OpenRC](https://github.com/OpenRC/openrc), ...) should work as well.
