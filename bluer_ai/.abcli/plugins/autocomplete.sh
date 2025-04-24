#! /usr/bin/env bash

function _autocomplete_bluer_ai() {
    local cur="${COMP_WORDS[COMP_CWORD]}"
    local cword=$COMP_CWORD
    local words="${COMP_WORDS[*]}"
    local command_name="${COMP_WORDS[0]}"

    COMPREPLY=($(python3 -m bluer_ai.plugins.autocomplete \
        --command "$command_name" \
        --cword "$cword" \
        --words "$words" \
        --alias_filename ../../.abcli/plugins/alias.sh))
}

function _set_bluer_ai_autocomplete() {
    local callable
    for callable in bluer_ai @ @ai @build_README @conda @docker @error @git @git++ @gpu @init \
        @latex @log @perform_action @plugins @pypi @screen @seed @session @ssh @ssm @terraform \
        @version @warn @wifi; do
        complete -F _autocomplete_bluer_ai "$callable"
    done
}

_set_bluer_ai_autocomplete
