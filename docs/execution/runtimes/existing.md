# Existing Runtimes

### Official runtime with Debian 11, Python 3.9 and NodeJS 14

Aleph.im provides users with a default runtime based on [Debian 11 "bullseye"](https://wiki.debian.org/DebianBullseye),
the current stable version of the Debian project which can
be [found on the Explorer](https://explorer.aleph.im/address/ETH/0x101d8D16372dBf5f1614adaE95Ee5CCE61998Fc9/message/STORE/bd79839bf96e595a06da5ac0b6ba51dea6f7e2591bb913deccded04d831d29f4).
This runtime is built with software available in the distribution, including Python 3.9 and Nodejs 14.

To optimize performance, this runtime uses a custom [Linux init](https://en.wikipedia.org/wiki/Init) process. This
process is specially designed to quickly launch the right endpoint in response to events such as HTTP requests. This is
especially useful when using [on-demand execution](../on_demand.md).

[//]: # (Not available yet)

[//]: # (### Official minimal runtime for binaries &#40;Rust, Go, ...&#41;)

[//]: # ()

[//]: # (This official minimal runtime is designed to run Linux binaries quickly and efficiently. It is built on a minimal)

[//]: # (system, and does not include interpreters or virtual machines for popular programming languages. This makes launching)

[//]: # (binaries fast and efficient.)

### Third-party runtimes

Use third-party runtimes available on the network by specifying their `item_hash` when creating your program.
