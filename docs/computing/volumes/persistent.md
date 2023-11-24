## Persistent Volumes

Persistent volumes are logical block disks that are attached to virtual machines running programs
in [on-demand](../index.md#on-demand-execution) or [persistent](../index.md#persistent-execution) execution modes. They are typically used to store
mutable data such as databases and persist data. Currently, persistent volumes are only stored on
the [Compute Resource Node](../../nodes/compute/index.md) (CRN) that is executing the program. Automatic backups and restoration
in case of failure of the CRN is a feature that is planned to be added in the future, and is currently left to the user.

A persistent volume has the following properties:

- `comment`: A custom comment from the user about the purpose of the volume.
- `mount`: The path on the filesystem of the virtual machine where the volume will be mounted.
- `name`: A unique name to reference the volume. This allows the user to change the _mount_ path while keeping the data
  present in the volume.
- `persistence`: `host` or `store`. Only `host` is currently supported.
- `size_mib`: The size of the volume, in [Mebibytes (MiB)](https://simple.wikipedia.org/wiki/Mebibyte). Only used when
  the volume is created and cannot be changed.

The content of a persistent volume is only available to the virtual machine using it and not accessible from other
virtual machines or from the network. Only the system administrator of the CRN is technically capable of directly
accessing the content of persistent volumes. The creator of a program can send an update of the program that exfiltrates
the content of the persistent volume.
