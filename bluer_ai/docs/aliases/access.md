# aliases: access

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
   cloud: BLUER_AI_CLOUD_IS_ACCESSIBLE (currently: 0)
   web: BLUER_AI_WEB_IS_ACCESSIBLE (currently: 1)
   pypi: BLUER_AI_PYPI_IS_ACCESSIBLE (currently: 1)
   forced_offline: BLUER_AI_FORCE_OFFLINE (currently: 0)
```
