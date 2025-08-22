#! /usr/bin/env bash

function bluer_ai_git_encrypt() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)
    local do_install=$(bluer_ai_option_int "$options" install 0)

    if [[ "$do_install" == 1 ]]; then
        if [[ "$abcli_is_mac" == true ]]; then
            bluer_ai_eval dryrun=$do_dryrun \
                brew install git-crypt gnupg
            [[ $? -ne 0 ]] && return 1
        fi
    fi

    bluer_ai_eval dryrun=$do_dryrun \
        echo "🪄"
    [[ $? -ne 0 ]] && return 1

    echo "🪄"
}
