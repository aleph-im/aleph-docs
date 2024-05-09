# Release process

The _aleph-vm_ software orchestrates the execution of virtual machines on
[aleph.im compute resource nodes](./index.md) using two hypervisors: 
_QEMU_ and _Firecracker_. 
This software is collaboratively developed by _aleph.im_ and the open-source community, 
with the main repository located at [aleph-im/aleph-vm on GitHub](https://github.com/aleph-im/aleph-vm).

## Versioning

The versioning of _aleph-vm_ follows the [Semantic Versioning](https://semver.org/) specification.

The version number is composed of three numbers: `MAJOR.MINOR.PATCH`.

- `MAJOR` version is incremented when incompatible changes are made.
- `MINOR` version is incremented when new features are added in a backwards-compatible manner.
- `PATCH` version is incremented when backwards-compatible bug fixes are made. 

Additional labels for pre-release follow [Python's PEP-0440](https://www.python.org/dev/peps/pep-0440/#pre-releases).

## Development process

Development is primarily conducted through Pull Requests (PRs) and code reviews targeting the `main` branch.

Commits must follow the commit style [defined on the community forum](https://community.aleph.im/t/git-commit-style/110).

Significant updates trigger preparation for a new release.

## Releases

_aleph-vm_ is published in two formats:

1. Debian packages for supported distributions.
2. Source code for manual installation.

### Preparation of a new release:

1. Packages built by GitHub Actions are tested on staging servers.
2. A new git tag is assigned to the release.
3. The new release is listed in the table used by the [node scoring](../reliability/scores.md).
4. Draft release notes are prepared on the GitHub releases page.
5. Packages are downloaded, unpacked, and attached to the release.
6. Release notes are reviewed and published.
7. The release is announced on [Twitter](https://twitter.com/aleph_im), [Telegram](https://t.me/alephim), and other channels.

All releases are documented on the [_aleph-vm_ GitHub releases page](https://github.com/aleph-im/aleph-vm/releases).
