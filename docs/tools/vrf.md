# Aleph.im Verifiable Random Functions

From the official GitHub repository: [aleph-im/aleph-vrf](https://github.com/aleph-im/aleph-vrf)

## What is a Verifiable Random Function (VRF)?

Verifiable Random Functions (VRF) are cryptographic primitives that generate random numbers that are both unpredictable
and verifiable.
This allows to create "trustless randomness", i.e. generate (pseudo-) random numbers in decentralized systems and
provide the assurance that the number was indeed generated randomly.

## Aleph.im implementation

Aleph.im uses a combination of virtual machines (VMs) and aleph.im network messages to implement VRFs.

The implementation revolves around the following components:

* The VRF coordinator
* N executors.

The coordinator receives user requests to generate random numbers.
Upon receiving a request, it selects a set of compute resource nodes (CRNs) to act as executors.
Each of these executors generates a random number and computes its hash using SHA3–256.
These hashes are then posted to aleph.im using a POST message, which also includes a unique request identifier.
Once all the hashes are posted and confirmed, the coordinator requests the actual random numbers from each node.

Finally, the coordinator performs a verification process to ensure that all random numbers correspond to their
previously posted hashes. The random numbers are then combined using an XOR operation to generate the final random
number. This final number, along with a summary of operations performed, is published on aleph.im for public
verification.

## How to use aleph.im VRFs

The VRF executors and coordinator are meant to be deployed as VM functions on the aleph.im network.
The coordinator can also be deployed in library mode (see below).

We provide a script to deploy the VM functions.
Just run the following command to package the application and upload it to the aleph.im network.

```
python3 deployment/deploy_vrf_vms.py
```

If the deployment succeeds, the script will display links to the VMs on the aleph.im network. Example:

```
  Executor VM: https://api2.aleph.im/api/v0/messages/558b0eeea54d80d2504b0287d047e0b78458d08022d3600bcf8478700dd0aac2
  Coordinator VM: https://api2.aleph.im/api/v0/messages/d9eef54544338685a9b4034cc16e285520eb3cf0c199eeade1d6b290365c95d0
```


### Use the coordinator in library mode

The coordinator can also be used directly from Python code.
First, deploy the executors using the deployment script, without the coordinator VM:

```
python3 deployment/deploy_vrf_vms.py --no-coordinator
```

This will deploy an executor VM on the network and give you its ID.
Example:

> Executor VM: https://api2.aleph.im/api/v0/messages/558b0eeea54d80d2504b0287d047e0b78458d08022d3600bcf8478700dd0aac2

Then, install the `aleph-vrf` module and call it from your code:

```shell
pip install aleph-vrf
```

```python
from aleph_vrf.coordinator.vrf import generate_vrf
from aleph_message.models import ItemHash


async def main():
    aleph_account = ...  # Specify your aleph.im account
    vrf_response = await generate_vrf(
        account=aleph_account,
        vrf_function=ItemHash(
            # The hash of the executor VM deployed above
            "558b0eeea54d80d2504b0287d047e0b78458d08022d3600bcf8478700dd0aac2"
        ),
    )
    random_number = int(vrf_response.random_number)
```

## Contribute

### Set up the development environment

You can set up a development environment by configuring a Python virtual environment and installing the project in
development mode.

```shell
python -m virtualenv venv
source venv/bin/activate
pip install -e .[build,testing]
```

### Run tests

This project uses mypy for static type analysis and pytest for unit/integration tests.

```shell
# Static analysis with mypy
mypy src/ tests/
# Run unit/integration tests
pytest -v .
```

### Create a new release

1. Deploy the VMs: `python3 deployment/deploy_vrf_vms.py`
2. Update the executor VM hash in the settings (Settings.FUNCTION) and create a Pull Request
3. Merge the Pull Request and create a new release on Github
4. Build and upload the package on PyPI: `python3 -m build && twine upload dist/*`

## Other resources

* [Article on Medium](https://medium.com/aleph-im/aleph-im-verifiable-random-function-vrf-b03544a7e904)
