## Enable PAYG (Pay-As-You-Go)

Pay-As-You-Go allows user to pay for resources as you use them on the Aleph.im network, eliminating the need to hold or
stake large amounts of $ALEPH.

The feature is currently available on BASE and Avalanche c-chain.

This guide outlines how to enable [Confidential Computing](../../../computing/confidential/index.md) on a CRN.

#### Configure the stream reward address

1. Create an Avalanche (AVAX) or BASE wallet.
2. Open the information of your CRN on the [aleph.im account page](https://account.aleph.im/) and enter the address in
   the section named STREAM REWARD ADDRESS.

3. Add the reward address inside the CRN configuration `/etc/aleph-vm/supervisor.env` in the form of:
   ```
   ALEPH_VM_PAYMENT_RECEIVER_ADDRESS="0x0000000000000000000000000000000000000000"
   ```
   Where `0x0000000000000000000000000000000000000000` is the address of your wallet.
4. Restart the node with `systemctl restart aleph-vm-supervisor.service`
5. Confirm that the address appears on the path `/status/config` on the CRN's URL/config
