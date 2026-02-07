# aliases: git

```bash
@git \
	<repo_name> \
	<command-line>
 . run '@git <command-line>' in <repo_name>.
@git \
	browse \
	[ . | - | <repo-name> ] \
	[actions,code|web]
 . browse <repo-name>.
@git \
	checkout \
	<branch-name> \
	[~fetch,~pull,rebuild]
 . git checkout <branch-name>.
@git \
	clone \
	<repo-name> \
	[cd,~from_template,if_cloned,install,object,pull,source=<username/repo_name>]
 . clone <repo-name>.
@git \
	create_branch \
	[<branch-name>] \
	[~increment_version,offline,~push,~timestamp]
 . create a branch in the repo.
@git \
	create_pull_request
 . create a pull request in the repo.
@git \
	get_branch
 . get git branch name.
@git \
	get_remote
 . get repo remote.
@git \
	get_repo_name
 . get repo name.
@git \
	++ | increment | increment_version \
	[diff] \
	[--verbose 1]
 . increment repo version.
@git \
	pull \
	[all,init,scp]
 . pull.
@git \
	push \
	[<message>] \
	[~action,browse,~create_pull_request,first,~increment_version,offline,test,~status,~workflow] \
	[build,browse,install,~rm_dist,~upload]
 . push repo.
@git \
	recreate_ssh
 . recreate github ssh key.
@git \
	reset
 . reset to the latest commit of the current branch.
@git \
	review \
	[<branch-name>]
 . review the repo.
@git \
	rm \
	<repo_name>
 . rm <repo-name>.
@git \
	seed \
	[screen]
 . seed 🌱  git.
@git \
	set_remote \
	[dryrun,https|ssh,private,~pull]
 . set repo remote.
@git \
	status \
	[~all]
 . show git status.
@git \
	sync_fork \
	<branch-name>
 . sync fork w/ upstream.
```
