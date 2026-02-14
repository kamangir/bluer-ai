# aliases: web

```bash
@access \
	check \
	[<url> | all] \
	[count=<count>,loop,seconds=<seconds>] \
	[--timeout 3]
 . check access.
@access \
	log
 . log access.
@access \
	set \
	cloud | forced_offline | pypi | web \
	0 | 1
 . set access.
   cloud: BLUER_AI_CLOUD_IS_ACCESSIBLE (currently: 1)
   web: BLUER_AI_WEB_IS_ACCESSIBLE (currently: 1)
   pypi: BLUER_AI_PYPI_IS_ACCESSIBLE (currently: 0)
   forced_offline: BLUER_AI_FORCE_OFFLINE (currently: 0)
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
