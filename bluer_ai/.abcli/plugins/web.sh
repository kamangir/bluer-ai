#! /usr/bin/env bash

function bluer_ai_web() {
    local task=${1:-share}

    local function_name=bluer_ai_web_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    bluer_ai_log_error "@web: $task: command not found."
    return 1
}

bluer_ai_source_caller_suffix_path /web
