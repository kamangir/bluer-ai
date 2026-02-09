#! /usr/bin/env bash

function bluer_ai_web_access() {
    local task=${1:-log}

    local function_name=bluer_ai_web_access_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m bluer_options.web.access "$@"
}

bluer_ai_source_caller_suffix_path /access
