#! /usr/bin/env bash

function bluer_ai_web_is_accessible() {
    what=${1:-online}

    url=$2
    if [[ -z "$url" ]]; then
        bluer_ai_log_error "url not found."
        return 1
    fi

    python3 -m bluer_ai.web \
        is \
        --what $what \
        --url $url \
        "${@:3}"
}
