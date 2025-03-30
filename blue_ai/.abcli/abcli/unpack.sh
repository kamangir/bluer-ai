#! /usr/bin/env bash

function abcli_unpack_repo_name() {
    local repo_name=${$1:-blue-ai}

    repo_name=$(echo "$repo_name" | tr _ -)

    [[ "$repo_name" == "." ]] &&
        repo_name=$(abcli_git_get_repo_name)

    echo $repo_name
}
