# option

```bash
@option \
	"$options" \
	<keyword> \
	[<default>]
 . get $options[<keyword>].
@option::choice \
	"$options" \
	<keyword-1,keyword-2,keyword-3> \
	[<default>]
 . return <keyword-*> that is in $options.
@option::int \
	"$options" \
	<keyword> \
	[<default>]
 . get int($options[<keyword>]).
```
