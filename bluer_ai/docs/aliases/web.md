# aliases: web

```bash
@web \
	diagnose \
	[Sion,Zagros]
 . diagnose web connection.
@web \
	get_ip
 . get IP.
@web \
	identify \
	[count=3,~log,loop,sleep=5,timestamp] \
	[--timeout 3]
 . identify web connection.
@web \
	is_accessible \
	<url> \
	[--timeout 3]
 . is <url> accessible?
@web \
	open
 . open the web object (kulej).
@web \
	share \
	[download,~open,~receive,~send,upload] \
	[kulej|<object-name>] \
	[port.receive.=<8001>,port.send=<8000>]
 . share <object-name>.
@web \
	where_am_i
 . where am I?
```
