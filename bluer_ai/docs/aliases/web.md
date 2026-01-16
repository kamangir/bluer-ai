# aliases: web

```bash
@web \
	get_ip
 . get IP.
@web \
	identify \
	[~upload,loop] \
	[-|<object-name>] \
	[--sleep <30>] \
	[--timeout 3]
 . identify web connection.
@web \
	is_accessible \
	<url> \
	[--timeout 3]
 . is <url> accessible?
@web \
	share \
	[download,open,~receive,~send,upload] \
	[-|<object-name>] \
	[port.receive.=<8001>,port.send=<8000>]
 . share <object-name>.
@web \
	share \
	[open,path,~receive,~send] \
	<path> \
	[port.receive.=<8001>,port.send=<8000>]
 . share <path>.
@web \
	where_am_i
 . where am I?
```
