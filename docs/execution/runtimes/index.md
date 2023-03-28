# Introduction

A program runtime is an operating system and software stack that enables your program to run on the aleph.im network.

Runtimes are customized Linux root filesystems that integrate with the Aleph.im infrastructure and provide access to
APIs, as well as quick responses to HTTP requests and other events.

The project provides official runtimes with all you need for most programs. Additionally, you can build and publish
custom runtimes, and use any available runtime on the network for your program.

- [Use existing runtimes](./existing.md)
- [Create custom runtimes](./custom.md)


## Init process

[On-demand Execution](../on_demand.md) relies on a custom [Linux init](https://en.wikipedia.org/wiki/Init) process,
optimized to launch the right endpoint in response to events such as HTTP requests. This custom init consists in two
simple programs, 
[init0.sh](https://raw.githubusercontent.com/aleph-im/aleph-vm/main/runtimes/aleph-alpine-3.13-python/init0.sh) 
and [init1.py](https://raw.githubusercontent.com/aleph-im/aleph-vm/main/runtimes/aleph-alpine-3.13-python/init1.py).

Use these in your custom runtime by copying them to `/rootfs/sbin/init` and 
`/mnt/rootfs/root/init1.py` respectively.

[Persistent Execution](../persistent.md) may use the same init process, but this is not required. If you do not make use
of the capabilities provided by the Aleph.im ecosystem, using the default of your distribution 
(ex: [systemd](https://systemd.io/), [OpenRC](https://github.com/OpenRC/openrc), ...) should work as well.
