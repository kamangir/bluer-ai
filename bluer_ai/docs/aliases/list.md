# aliases: list

```bash
@list \
	filter \
	<item-1>,<item-2>,... \
	[--contains <this>] \
	[--doesnt_contain <that>] \
	[--delim space | <delim>]
 . filter list.
@list \
	in \
	<item> \
	<item-1>,<item-2>,... \
	[--delim space | <delim>]
 . True | False.
@list \
	intersect \
	<item-1>,<item-2>,... \
	<item-1>,<item-2>,... \
	[--delim space | <delim>]
 . intersect the two lists.
@list \
	item \
	<item-1>,<item-2>,... \
	<index> \
	[--delim space | <delim>]
 . list[<index>].
@list \
	len \
	<item-1>,<item-2>,... \
	[--delim space | <delim>]
 . len(list).
@list \
	log \
	<item-1>,<item-2>,... \
	[--before <loading>] \
	[--after <thing(s)>] \
	[--delim space | <delim>]
 . log list.
@list \
	next \
	<item> \
	<item-1>,<item-2>,... \
	[--delim space | <delim>]
 . item after <item> in list.
@list \
	nonempty \
	<item-1>,<item-2>,... \
	[--delim space | <delim>]
 . non-empty items in list.
@list \
	prev \
	<item> \
	<item-1>,<item-2>,... \
	[--delim space | <delim>]
 . item before <item> in list.
@list \
	resize \
	<item-1>,<item-2>,... \
	-1 | <length> \
	[--delim space | <delim>]
 . resize list.
@list \
	reverse \
	<item-1>,<item-2>,... \
	[--delim space | <delim>]
 . reverse list.
@list \
	sort \
	<item-1>,<item-2>,... \
	[--delim space | <delim>] \
	[--unique 0|1]
 . sort list.
```
