# Confidential instance creation

This section explain how to allocate your VM on the Aleph Network and start it on a chosen CRN.

## Ensure you have uploaded your VM in the aleph network.
See previous section: [Encrypted Virtual Machine image](./encrypted-disk.md)

## Create your confidential Instance in Aleph.

This will ask you how much CPU, RAM and Disk you want to use and on which node (CRN) to deploy it.

```shell
aleph instance create --confidential
```

Be sure to write down the url of the CRN running the node and the hash of your VM

## Establish a secure channel to communicate with your VM

Using the command:
```shell
aleph instance confidential-init-session <vmhash>
``` 

> ℹ️ If this step fails, the instance must be rebooted using `aleph instance reboot <vmhash> <node url>` before
> a new attempt.

## Validate the authenticity of you VM and start it

Using the command:

```shell
aleph  instance confidential-start <vmhash>
``` 

> ℹ️ If this step fails, the instance must be rebooted using `aleph instance reboot <vmhash> <node url>` before
> a new attempt.

## Your VM is now ready to use

You can check the log of your VM or ssh into it.

### Retrieve the logs of your VM

Using the command:

```shell
aleph instance logs <vmhash>
```

### SSH into your VM

The list of instances can be obtained, with their IP addresses, using:

```shell
aleph instance list
```

Alternatively, the IPv6 address of an instance can be obtained from API of the compute node:
```
https://<node url>/about/executions/list
```

It is then possible to connect to the virtual machine using SSH:
```shell
ssh <user>@<ip>
```

The default user `<user>` is by default `root` for Debian systems and `ubuntu` for Ubuntu.
