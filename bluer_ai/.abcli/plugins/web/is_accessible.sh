#! /usr/bin/env bash

function bluer_ai_web_is_accessible() {
    local options=$1
    local do_force=$(bluer_ai_option_int "$options" force 0)
    if [[ "$BLUER_AI_FORCE_OFFLINE" == 1 ]] && [[ "$do_force" == 0 ]]; then
        echo 0
        return
    fi

    url=$2
    if [[ -z "$url" ]]; then
        bluer_ai_log_error "url not found."
        return 1
    fi

    python3 -m bluer_ai.plugins.web \
        is_accessible \
        --url $url \
        "${@:3}"
}

bluer_ai_web_identify
