#! /usr/bin/env bash

function test_bluer_ai_git_encrypt() {
    local options=$1

    local object_name=test_bluer_ai_git_encrypt-$(bluer_ai_string_timestamp_short)

    bluer_ai_select $object_name

    bluer_ai_git_clone \
        bluer-plugin \
        cd,object
    [[ $? -ne 0 ]] && return 1

    bluer_ai_git_encrypt
}
