# How to update a program

Whether it is to add new features to your application, upgrade to the latest version of a dependency or migrate to
a new runtime, there are numerous reasons why you will update your program.

In this tutorial, we will see how you can, and sometimes cannot, update programs deployed on the aleph.im network.

There are two main solutions to update a program:\
1. Update the program directly\
2. Update one or more volumes of the program.

## Update a program

The first way to update a program is to emit a new PROGRAM message that replaces the original one.
This is as simple as setting the `replaces` field of the PROGRAM message to the hash of the program
you want to modify.

For example, let's say you wrote a program and configured it to use 1 core.
It turns out that this was a little short-sighted, and you actually need 4 cores
to serve more requests.
You can update your program with the `aleph` CLI.
There are two options, whether you need to update your code or not.

If you want to update your code:

```bash
aleph program update $PROGRAM_HASH $CODE_DIR
```

Otherwise:

```bash
aleph message amend $PROGRAM_HASH
```

This will open your favorite command-line editor and let you update the message.
For our example, we will just update the `resource.vcpus` property from 1 to 4.
Once saved, the new message is emitted as a replacement for the original program.
Your program will be updated as soon as the message reaches the Compute Resource Node(s) executing it.

### Immutable programs

Some programs cannot be updated with the method described above.
We call these __immutable__ programs.
These programs are configured with the `allow_amend` field set to false.
Even the owner of an immutable program cannot update it.

The only way to update an immutable program is to delete it and create a new one.

## Update a volume

While updating a program will work in most cases, you can also update a program by updating one or more
of its volumes.
There are numerous cases where this is the best option:

* You detected a security vulnerability in one of your dependencies and want to migrate to a fixed version
* You want your program to migrate to the latest official aleph.im runtime automatically
* You just want to upgrade your code
* etc.

The operation is similar to updating a program, except that we will update the STORE message
that created the file instead of the PROGRAM message.
Let's use the `aleph` CLI to update one of our volumes.

```
aleph message amend $VOLUME_REF
```

Where `VOLUME_REF` is the `item_hash` of the STORE message that stores the file on aleph.im.
You must either own this file or have the permission to update this file 
(see [Permissions](../protocol/permissions.md)).

### Immutable volumes

Similarly to programs, aleph.im also has the concept of immutable volumes.
They are volumes configured with the `use_latest` field set to false.
These volumes will always use the version of the file configured when the program was created.

The only way to update an immutable volume is to first update the program to make the volume
mutable.
If the program itself is immutable, you will have to delete the program and start over.
