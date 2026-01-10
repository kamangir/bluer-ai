#! /usr/bin/env bash

function bluer_ai_web() {
    local task=$1

    local function_name=bluer_ai_web_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    python3 -m bluer_ai.web "$@"
}

bluer_ai_source_caller_suffix_path /web
