# Introduction

A **runtime** is an operating system and software stack that enables your program to run on the aleph.im network.

Runtimes are customized Linux root filesystems that integrate with the aleph.im infrastructure and provide access to
APIs, as well as quick responses to HTTP requests and other events.

The project provides official runtimes with all you need for most programs and in most case you will simply use those.

Additionally, you can build and publish custom runtimes, and use any available runtime on the network for your program.

- [Use existing runtimes](#existing-runtimes)
- [Create custom runtimes](./custom.md)

## Existing Runtimes
### Official runtimes

Aleph.im provides users with a default runtime based on [Debian 12 "bookworkm"](https://wiki.debian.org/DebianBookworm),
the current stable version of the Debian project which can
be [found on the Explorer](https://explorer.aleph.im/address/ETH/0x101d8D16372dBf5f1614adaE95Ee5CCE61998Fc9/message/STORE/63f07193e6ee9d207b7d1fcf8286f9aee34e6f12f101d2ec77c1229f92964696).
This runtime is built with software available in the distribution, including Python 3.11 and Nodejs.

There is also a [Debian 11 "bullseye"](https://wiki.debian.org/DebianBullseye) runtime, which is deprecated but kept for compatibilities reason.

These are maintained as part of the aleph-vm  repository, the code is available in the [`/runtime` folder](https://github.com/aleph-im/aleph-vm/tree/main/runtimes) 

[//]: # (Not available yet)

[//]: # (### Official minimal runtime for binaries &#40;Rust, Go, ...&#41;)

[//]: # ()

[//]: # (This official minimal runtime is designed to run Linux binaries quickly and efficiently. It is built on a minimal)

[//]: # (system, and does not include interpreters or virtual machines for popular programming languages. This makes launching)

[//]: # (# &#40;binaries fast and efficient.&#41;)

### Third-party runtimes

Runtimes made available on the network by third party can also be used by specifying their `item_hash` when creating your program.

User can also build and use their own runtime by uploading them to the aleph network, see  [Create custom runtimes](./custom.md)

##  Init process

To optimize performance, runtime uses a custom [Linux init](https://en.wikipedia.org/wiki/Init) process. This
process is specially designed to quickly launch the right endpoint in response to events such as HTTP requests. This is
especially useful when using [on-demand execution](../index.md#on-demand-execution).

This custom init consists in two simple programs, [init0.sh](https://raw.githubusercontent.com/aleph-im/aleph-vm/main/runtimes/aleph-alpine-3.13-python/init0.sh) and [init1.py](https://raw.githubusercontent.com/aleph-im/aleph-vm/main/runtimes/aleph-alpine-3.13-python/init1.py).

Use these in your custom runtime by copying them to `/rootfs/sbin/init` and 
`/mnt/rootfs/root/init1.py` respectively.

[Persistent Execution](../index.md#persistent-execution) may use the same init process, but this is not required. If you do not make use
of the capabilities provided by the aleph.im ecosystem, using the default of your distribution 
(ex: [systemd](https://systemd.io/), [OpenRC](https://github.com/OpenRC/openrc), ...) should work as well.

## List of official runtimes



### Functions
Runtime used for functions

| name                                                         | hash                                                                | filesystem |
|--------------------------------------------------------------|---------------------------------------------------------------------|------------|
| Official runtime with Debian 11, Python 3.9 & Node.js 14     | bd79839bf96e595a06da5ac0b6ba51dea6f7e2591bb913deccded04d831d29f4    | ext4       |
| **Official runtime with Debian 12, Python 3.11**             | 63f07193e6ee9d207b7d1fcf8286f9aee34e6f12f101d2ec77c1229f92964696    | ext4       |
| Official Node.js LTS runtime (with nvm support) on Debian 11 | 3c238dd3ffba73ab9b2cccb90a11e40e78aff396152de922a6d794a0a65a305e    | ext4       |
| Deprecated Debian runtime                                    | f873715dc2feec3833074bd4b8745363a0e0093746b987b4c8191268883b2463    | ext4       |


[//]: # (Web and current SDK)
[//]: # (`63f07193e6ee9d207b7d1fcf8286f9aee34e6f12f101d2ec77c1229f92964696`)
[//]: # (Old doc)
[//]: # (`bd79839bf96e595a06da5ac0b6ba51dea6f7e2591bb913deccded04d831d29f4`)
[//]: # (Old one in the SDK)
[//]: # (`f873715dc2feec3833074bd4b8745363a0e0093746b987b4c8191268883b2463`)

### Instances

#### Roofs for Firecracker
| name                 | hash                                                             | filesystem |
|----------------------|------------------------------------------------------------------|------------|
| Debian 11 “Bullseye” | 887957042bb0e360da3485ed33175882ce72a70d79f1ba599400ff4802b7cee7 | BTRFS      |
| Debian 12 “Bookworm” | 6e30de68c6cedfa6b45240c2b51e52495ac6fb1bd4b36457b3d5ca307594d595 | BTRFS      |
| Ubuntu 22.04 LTS     | 77fef271aa6ff9825efa3186ca2e715d19e7108279b817201c69c34cedc74c27 | BTRFS      |


#### QEMU Disk Image
QEMU "runtimes" are regular disk image. The image uploaded to the network are the one directly provided by their respective project, specifically the cloud variant with cloud-init enabled.

| name                 | hash                                                             | filesystem |
|----------------------|------------------------------------------------------------------|------------|
| Debian 11 “Bullseye” | f7e68c568906b4ebcd3cd3c4bfdff96c489cd2a9ef73ba2d7503f244dfd578de | disk img   |
| Debian 12 “Bookworm” | b6ff5c3a8205d1ca4c7c3369300eeafff498b558f71b851aa2114afd0a532717 | disk img   |
| Ubuntu 22.04 LTS     | 4a0f62da42f4478544616519e6f5d58adb1096e069b392b151d47c3609492d0c | disk img   |

#### Confidential Computing Disk
No runtime or disk image are provided at the moment for confidential computing.

#### Firmware for Confidential computing
The runtime for the confidential image are custom-built OVMF file that are used to validate, decrypt and start confidential VM. Refer to the [confidential section](../../computing/confidential/index.md)

* Confidential firmware item hash : `ba5bb13f3abca960b101a759be162b229e2b7e93ecad9d1307e54de887f177ff`
* Hash for verification for the confidentiality validation process `89b76b0e64fe9015084fbffdf8ac98185bafc688bfe7a0b398585c392d03c7ee`
