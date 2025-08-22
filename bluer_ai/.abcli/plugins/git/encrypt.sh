#! /usr/bin/env bash

function bluer_ai_git_encrypt() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)

    bluer_ai_eval dryrun=$do_dryrun \
        echo "🪄"
    [[ $? -ne 0 ]] && return 1

    echo "🪄"
}
