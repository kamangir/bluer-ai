# ssh

```bash
@ssh \
	add \
	<filename>
 . ssh add <filename>.
@ssh \
	copy_id \
	<filename> \
	jetson_nano | rpi \
	<machine-name>
 . ssh copy-id <filename> to <machine-name>.
@ssh \
	ec2 \
	<ip-address> \
	[region=<region_1>,user=<ec2-user|ubuntu>,vnc]
 . ssh to <ip-address>.
@ssh \
	jetson_nano | rpi \
	<machine-name>
 . ssh to <machine-name>.
@ssh \
	keygen \
	[<filename>]
 . keygen <filename>.
```
