# Confidential computing

Aleph.im allow to launch confidential VM, securised with AMD SEV. This is also known as TEE, Trusted Execution Environment.

The disk and the memory are fully encrypted so no one can see what happen inside your VM.

At the moment they can only be launched via the aleph client cli tool.


# Requirements:
 * The sevctl command tool
 * The aleph cli client, properly set up with an Ethereum account
 * A ssh key

# Guide
1. Create a confidential disk image
You must create a virtual machine disk image,  encrypted with a password of your choice.

Follow the instruction and scripts provided here: https://github.com/aleph-im/aleph-vm/blob/main/examples/example_confidential_image/README.md

Make it your own:  add your user, ssh key, other program that you might need.
Don't forget your encryption password! The aleph team can't help you if you lose it

2. Upload the disk file you just created to ipfs

3. Pin the ipfs file in aleph via
```
aleph file pin <ipfs hash>
```

4. Check that it is present 

... and get it's ItemHash that is to be passed at the rootfs item hash:
```shell
aleph file list
```

5. Create your confidential Instance in Aleph.

This will ask you how much CPU, RAM and Disk you want to use and on which node (CRN) to deploy it

`aleph instance create  --confidential`

Be sure to write down the url of the CRN running the node and the hash of your VM 


6.  Establish a secure channel to communicate with your VM

Using the command:
```sh
aleph instance confidential-init-session <vmhash> <node url>
``` 

7. Validate the authenticity of you VM and start it
Using the command:

```sh
aleph  instance confidential-start <vmhash> <node url>
``` 


8. Your VM is now ready to use
You can check the log of your VM or ssh to it 
