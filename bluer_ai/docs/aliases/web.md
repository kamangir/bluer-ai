# aliases: web

```bash
@web \
	access \
	check \
	[<url> | all] \
	[count=<count>,loop,seconds=<seconds>] \
	[--timeout 3]
 . check web access.
@web \
	access \
	log
 . log web access.
@web \
	access \
	set \
	cloud | pypi | web \
	0 | 1
 . set web access.
   cloud: BLUER_AI_CLOUD_IS_ACCESSIBLE (currently: 1)
   web: BLUER_AI_WEB_IS_ACCESSIBLE (currently: 1)
   pypi: BLUER_AI_PYPI_IS_ACCESSIBLE (currently: 0)
@web \
	diagnose \
	[Sion,Zagros]
 . diagnose web connection.
@web \
	get_ip
 . get IP.
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
