# storage

```bash
@storage \
	clear \
	[cloud,~dryrun]
 . clear storage.
@storage \
	download_file \
	<object-name> \
	[filename]
 . download filename -> <object-name>.
@storage \
	exists \
	<object-name>
 . True/False.
@storage \
	list \
	<prefix> \
	[<args>]
 . list prefix in storage.
@storage \
	rm \
	[~dryrun] \
	<object-name>
 . rm <object-name>.
@storage \
	status \
	[count=<10>,depth=<2>]
 . show storage status.
```
