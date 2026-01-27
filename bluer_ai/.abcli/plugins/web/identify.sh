#! /usr/bin/env bash

function bluer_ai_web_identify() {
    local options=$1
    local do_loop=$(bluer_ai_option_int "$options" loop 0)

    if [[ "$do_loop" == 1 ]]; then
        local do_upload=$(bluer_ai_option_int "$options" upload 0)

        local object_name=$(bluer_ai_clarify_object $2 web-status-$(bluer_ai_string_timestamp))

        python3 -m bluer_ai.web \
            identify \
            --object_name $object_name \
            --loop 1 \
            --timestamp 1 \
            "${@:3}"
        [[ $? -ne 0 ]] && return 1

        if [[ "$do_upload" == 1 ]]; then
            bluer_objects_upload \
                - \
                $object_name
        fi

        return
    fi

    export BLUER_AI_WEB_STATUS=$(python3 -m bluer_ai.web \
        identify \
        --log 1)
}

bluer_ai_web_identify
