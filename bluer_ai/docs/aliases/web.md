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
	receive \
	[open,upload,port=<8001>] \
	[-|<object-name>]
 . receive files.
@web \
	send \
	[download,port=<8000>] \
	[.|<object-name>]
 . send files.
@web \
	send \
	[path,port=<8000>] \
	<path>
 . send files.
@web \
	share \
	[download,port.receive.=<8001>,port.send=<8000>,upload] \
	[-|<object-name>]
 . share files.
@web \
	share \
	[path,port.receive.=<8001>,port.send=<8000>] \
	<path>
 . share files.
@web \
	where_am_i
 . where am I?
```
