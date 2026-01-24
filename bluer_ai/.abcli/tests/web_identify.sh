#! /usr/bin/env bash

function test_bluer_ai_web_identify() {
    bluer_ai_web_identify
    [[ "$output" -ne 0 ]] &&
        return 1

    bluer_ai_hr

    local object_name=test_bluer_ai_web_identify-$(bluer_ai_string_timestamp)

    bluer_ai_web_identify \
        loop,~upload \
        $object_name \
        --count 3 \
        --sleep 2
}
