#! /usr/bin/env bash

function test_abcli_README() {
    local options=$1

    abcli_eval ,$options \
        blue_ai build_README
}
