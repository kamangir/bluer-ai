#! /usr/bin/env bash

function bluer_ai_plugins_transform() {
    local repo_name=$1
    if [[ -z "$repo_name" ]]; then
        abcli_log_error "@plugins: transform: $repo_name: repo not found."
        return 1
    fi
    local plugin_name=$(abcli_plugin_name_from_repo $repo_name)

    abcli_log "bluer-plugin -> $repo_name ($plugin_name)"

    pushd $abcli_path_git/$repo_name >/dev/null

    git mv bluer_plugin $plugin_name

    git mv \
        $plugin_name/.abcli/bluer_plugin.sh \
        $plugin_name/.abcli/$plugin_name.sh

    rm -v $plugin_name/.abcli/session.sh

    python3 -m bluer_ai.plugins \
        transform \
        --repo_name $repo_name \
        --plugin_name $plugin_name \
        "${@:2}"
}
