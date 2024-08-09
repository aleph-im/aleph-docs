# Confidential instance creation

## 1. Create your confidential Instance in Aleph.

This will ask you how much CPU, RAM and Disk you want to use and on which node (CRN) to deploy it.

```shell
aleph instance create --confidential --crn-url https://aleph8.agot.be/
```

Be sure to write down the url of the CRN running the node and the hash of your VM 


## 2. Establish a secure channel to communicate with your VM

Using the command:
```shell
aleph instance confidential-init-session <vmhash> <node url>
``` 

## 3. Validate the authenticity of you VM and start it

Using the command:

```shell
aleph  instance confidential-start <vmhash> <node url>
``` 

## 4. Your VM is now ready to use

You can check the log of your VM or ssh to it 

TODO: How, where ?
