# aliases: env

```bash
@env \
	[keyword]
 . show environment variables.
@env \
	backup
 . backup env -> $abcli_path_env_backup.
@env \
	backup \
	list
 . list $abcli_path_env_backup.
@env \
	dot \
	cat \
	[ | <env-name> | config | sample ]
 . cat env.
@env \
	dot \
	cat \
	jetson_nano | rpi \
	<machine-name>
 . cat .env from machine.
@env \
	dot \
	cp | copy \
	<env-name> \
	local | jetson_nano | rpi \
	[<machine-name>]
 . cp <env-name> to machine.
@env \
	dot \
	edit \
	jetson_nano | rpi \
	<machine-name>
 . edit .env on machine.
@env \
	dot \
	get \
	<variable>
 . <variable>.
@env \
	dot \
	list
 . list env repo.
@env \
	dot \
	load \
	[caller,filename=<.env>,plugin=<plugin-name>,ssm,suffix=/tests,verbose]
 . load .env.
@env \
	dot \
	set \
	<variable> \
	<value>
 . <variable> = <value>.
```
