#! /usr/bin/env bash

function test_blue_ai_version() {
    local options=$1

    abcli_eval ,$options \
        "blue_ai version ${@:2}"

    return 0
}
