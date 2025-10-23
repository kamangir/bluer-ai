# aliases: plugins

```bash
@plugins \
	get_module_name \
	<repo-name>
 . get module name for <repo-name>.
@plugins \
	install \
	[all | <plugin-name>]
 . install plugin(s).
@plugins \
	list_of_external \
	[--delim space | <delim>] \
	[--log 1] \
	[--repo_names 1]
 . show list of external plugins.
@plugins \
	list_of_installed \
	[--delim space | <delim>] \
	[--log 1] \
	[--repo_names 1]
 . show list of installed plugins.
@plugins \
	transform \
	<repo-name>
 . transform a bluer-plugin git clone to <repo-name>.
```
