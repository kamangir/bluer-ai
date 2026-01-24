#! /usr/bin/env bash

function bluer_ai_pypi() {
    local task=$1

    local options=$2
    local plugin_name=$(bluer_ai_option "$options" plugin bluer_ai)

    local function_name=bluer_ai_pypi_$task
    if [[ $(type -t $function_name) == "function" ]]; then
        $function_name "${@:2}"
        return
    fi

    bluer_ai_log_error "$plugin_name: pypi: $task: command not found."
    return 1
}

bluer_ai_source_caller_suffix_path /pypi

export BLUER_AI_PYPI_IS_ACCESSIBLE=$(python3 -m bluer_ai.web \
    is_accessible \
    --url https://pypi.org/)
if [[ "$BLUER_AI_PYPI_IS_ACCESSIBLE" == 1 ]]; then
    bluer_ai_log "✅ pypi is accessible."
else
    bluer_ai_log_warning "pypi is not accessible."
fi
