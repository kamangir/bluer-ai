#! /usr/bin/env bash

function test_bluer_ai_web_access_set() {
    local BLUER_AI_CLOUD_IS_ACCESSIBLE_saved=$BLUER_AI_CLOUD_IS_ACCESSIBLE
    export BLUER_AI_CLOUD_IS_ACCESSIBLE=0

    bluer_ai_web_access_set \
        cloud \
        1
    [[ $? -ne 0 ]] && return 1

    bluer_ai_assert $BLUER_AI_CLOUD_IS_ACCESSIBLE 1
    [[ $? -ne 0 ]] && return 1

    export BLUER_AI_CLOUD_IS_ACCESSIBLE=$BLUER_AI_CLOUD_IS_ACCESSIBLE_saved
}
