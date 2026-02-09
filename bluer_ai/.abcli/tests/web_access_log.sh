#! /usr/bin/env bash

function test_bluer_ai_web_access_log() {
    bluer_ai_web_access_log
    [[ $? -ne 0 ]] && return 1

    bluer_ai_hr

    bluer_ai_web_access_log \
        --timestamp 1
}
