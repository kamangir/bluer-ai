#! /usr/bin/env bash

function test_bluer_ai_web_access_check() {
    local output=$(bluer_ai_web_access_check void)
    [[ "$output" -ne 0 ]] &&
        return 1

    bluer_ai_hr

    local url="https://iribnews.ir"
    [[ "$abcli_is_github_workflow" == true ]] &&
        url="https://cnn.com"

    output=$(bluer_ai_web_access_check $url)
    [[ "$output" -ne 1 ]] &&
        return 1

    bluer_ai_hr

    output=$(
        bluer_ai_web_access_check $url - \
            --timeout 3
    )
    [[ "$output" -ne 1 ]] &&
        return 1

    bluer_ai_hr

    local BLUER_AI_FORCE_OFFLINE_saved=$BLUER_AI_FORCE_OFFLINE
    export BLUER_AI_FORCE_OFFLINE=1

    output=$(bluer_ai_web_access_check $url)
    [[ "$output" -ne 0 ]] &&
        return 1

    export BLUER_AI_FORCE_OFFLINE=$BLUER_AI_FORCE_OFFLINE_saved

    return
}
