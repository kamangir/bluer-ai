#! /usr/bin/env bash

function test_bluer_ai_web_access_check_all() {
    bluer_ai_web_access_check all
    [[ $? -ne 0 ]] && return 1

    bluer_ai_hr

    bluer_ai_web_access_check \
        all \
        loop,count=3 \
        --timeout 2
}
