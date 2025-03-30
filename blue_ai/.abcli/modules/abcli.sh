#! /usr/bin/env bash

function blue_ai() {
    local task=$1

    local function_name=abcli_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
    else
        abcli_log_error "blue_ai: $task: command not found."
        return 1
    fi
}

function abcli_version() {
    echo $abcli_fullname
}

abcli_env_dot_load \
    caller,filename=config.env,suffix=/../..
