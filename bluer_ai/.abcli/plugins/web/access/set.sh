#! /usr/bin/env bash

function bluer_ai_web_access_set() {
    local keyword=${1:-void}

    local var_name=$(python3 -m bluer_options.web.access \
        get_var_name \
        --keyword "$keyword")

    if [[ -z "$var_name" ]]; then
        bluer_ai_log_error "$keyword: var not found."
        return 1
    fi

    local value=${2:-1}

    bluer_ai_log "$var_name=$value"
    export $var_name=$value

    if [[ "$keyword" == "forced_offline" ]]; then
        bluer_ai_eval path=$abcli_path_git/bluer-ai \
            dotenv set \
            $var_name \
            "$value"
    fi
}
