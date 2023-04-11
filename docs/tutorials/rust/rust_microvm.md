# Building a Rust microVM

> This tutorial follows up the first tutorial [Creating and hosting a Python program on Aleph-VM](../python/getting_started.md).

In this tutorial, we will build and deploy a Rust application on the aleph.im network.

In addition to running Python programs using ASGI as covered in the first tutorial, 
Aleph.im VMs also support any program as long as it listens for HTTP requests on port 8080.

## The application

In this first section, you will run a program written in Rust on an aleph.im VM.

### Requirements

You need a Rust compiler. You can install one using the [official Install Rust guide](https://www.rust-lang.org/tools/install) 
or via your favourite package manager.

  $ sudo apt install rustc cargo

## Write a Rust program

Let's build a very simple HTTP server inspired by the [Building a Single-Threaded Web Server](https://doc.rust-lang.org/book/ch20-01-single-threaded.html)
section of The Rust Programming Language Book:

```shell
$ cargo new example_http_rust
     Created binary (application) `example_http_rust` project
$ cd example_http_rust
```

Filename: `src/main.rs`
```rust
use std::io::prelude::*;
use std::net::TcpListener;
use std::net::TcpStream;

fn main() {

    let listener = TcpListener::bind("0.0.0.0:8080").unwrap();
    println!("Running on 0.0.0.0:8080");
    for stream in listener.incoming() {
        let stream = stream.unwrap();
        handle_connection(stream);
    }
}

fn handle_connection(mut stream: TcpStream) {
    println!("handling connection");

    const MSG: &str = "helloworld";
    let msg = MSG.as_bytes();

    let response = format!("{:x?}", msg);

    let mut buffer = [0; 1024];

    stream.read(&mut buffer).unwrap();

    let response = format!("HTTP/1.1 200 OK\n\nOKIDOK\n{}", response);

    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}
```

## Test it locally

It is usually easy to test Rust programs on your machine.

```shell
cargo run
```

Open `http://127.0.0.1:8080` in your browser to test your new server.

## Upload your program on aleph.im

Let's upload our program.

Compile your program in release mode:
```shell
cargo build --release
```

After installing [aleph-client](https://github.com/aleph-im/aleph-client), you should have access to the `aleph` command:

```shell
aleph --help
```

The `aleph program CODE_DIR ENTRYPOINT` command will package the `CODE_DIR` code directory and configure the program
to run the `ENTRYPOINT` command.
For our program, the code directory is the build directory and the entrypoint is the name of our executable.

```shell
aleph program ./target/release/example_http_rust example_http_rust
```

If your program takes arguments, pass them in the entrypoint by using quotes: `"example_http_rust --help"`.

> ℹ️ If you get the error `Invalid zip archive`, you are probably missing the Squashfs user tool `mksquashfs`. 
> In that case, first create the squashfs archive and then upload it using `aleph program ./target/release/example_http_rust.squashfs example_http_rust`.
