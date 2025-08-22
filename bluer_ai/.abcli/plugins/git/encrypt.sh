#! /usr/bin/env bash

function bluer_ai_git_encrypt() {
    local options=$1
    local do_dryrun=$(bluer_ai_option_int "$options" dryrun 0)
    local do_create_key=$(bluer_ai_option_int "$options" create_key 0)
    local do_install=$(bluer_ai_option_int "$options" install 0)

    if [[ "$do_install" == 1 ]]; then
        if [[ "$abcli_is_mac" == true ]]; then
            bluer_ai_eval dryrun=$do_dryrun \
                brew install git-crypt gnupg
            [[ $? -ne 0 ]] && return 1
        fi
    fi

    if [[ "$do_create_key" == 1 ]]; then
        bluer_ai_eval dryrun=$do_dryrun \
            gpg --full-generate-key
        [[ $? -ne 0 ]] && return 1
    fi

    bluer_ai_eval dryrun=$do_dryrun \
        echo "🪄"
    [[ $? -ne 0 ]] && return 1

    echo "🪄"
}
