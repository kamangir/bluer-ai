#! /usr/bin/env bash

function test_bluer_ai_git_encrypt() {
    local options=$1

    bluer_ai_git_clone bluer-plugin
    [[ $? -ne 0 ]] && return 1

    bluer_ai_git_encrypt
}
