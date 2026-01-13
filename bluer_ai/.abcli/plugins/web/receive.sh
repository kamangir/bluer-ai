#! /usr/bin/env bash

function bluer_ai_web_receive() {
    local options=$1
    local do_upload=$(bluer_ai_option_int "$options" upload 0)
    local port=$(bluer_ai_option "$options" port 8001)

    local object_name=$(bluer_ai_clarify_object $2 web-$(bluer_ai_string_timestamp))

    bluer_ai_log "🔗 http://$BLUER_AI_IP:$port/ -> $object_name"

    bluer_ai_eval - \
        python3 -m bluer_ai.web.receive.app \
        --path $ABCLI_OBJECT_ROOT/$object_name \
        --port $port \
        "${@:3}"

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - \
            $object_name
}
