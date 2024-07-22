# How to backup a CCN

The data stored by aleph.im Core Channel Nodes (CCN) is redundant and can be retrieved from the network in case of
emergencies. However, there are a few important factors to consider in order to minimize node downtime, safeguard
reputation, and maximize rewards.

## What to back up

### Secret Keys

The first essential step is to backup the keys used in the P2P protocol by the Core Channel Node.

These keys are located
in the `pyaleph/keys/*` directory. It is sufficient to perform this backup only once, as these keys will not change.

> ⚠️ Reinstalling a node with the same IPv4 will fail if these keys change, as other nodes will only trust the same key
> for a duration of many hours or days.

### File Storage

The second aspect you may consider backing up is the file storage. If you are using the provided `docker-compose.yml`
file, the file storage is located in the Docker volume named `pyaleph-ipfs`. It is acceptable to have an incomplete
backup, as it enables faster resynchronization from the network by eliminating the need to download those files again.

### PostgreSQL Database

Additionally, it is recommended to backup the PostgreSQL database stored in the Docker volume `pyaleph-postgres`. When
restoring your node, ensure that the file storage mentioned above is not older than this database volume.

## Full resynchronisation

Performing backups of the file storage and the PostgreSQL database will enable faster node recovery compared to
downloading and processing all messages from the network. However, keep in mind that there is always a possibility of
relying solely on network synchronization.

## Tooling

The choice of backup solution depends on your specific installation.

### Filesystem snapshots

A popular approach is to install run the Docker volumes on
the [BTRFS](https://www.kernel.org/doc/html/latest/filesystems/btrfs.html)
or [ZFS](https://openzfs.org/) filesystem and utilizing the snapshots provided by those file systems.
Others prefer running Core Channel Nodes in virtual machines and utilizing the snapshot features of
the [QCOW image format](https://wiki.qemu.org/Features/Qcow3).

### Backup tools

An alternative using regular tools is to use the following commands:

#### Database

Backup:

```shell
docker exec -t pyaleph_postgres_1 pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
```

Restore:

```shell
cat your_dump.sql | docker exec -i pyaleph_postgres_1 psql -U postgres
```

#### File storage

Backup:

```shell
rsync -av /var/lib/docker/volumes/pyaleph_pyaleph-local-storage/ user@your-backup-server:/path/to/directory
```

Restore (untested):

```shell
rsync -av user@your-backup-server:/path/to/directory /var/lib/docker/volumes/pyaleph_pyaleph-local-storage/
```
