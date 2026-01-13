#! /usr/bin/env bash

function bluer_ai_web_send() {
    local options=$1
    local do_download=$(bluer_ai_option_int "$options" download 0)
    local port=$(bluer_ai_option "$options" port 8000)

    local object_name=$(bluer_ai_clarify_object $2 .)

    [[ "$do_download" == 1 ]] &&
        bluer_objects_download - \
            $object_name

    bluer_ai_log "🔗 http://$BLUER_AI_IP:$port/"

    bluer_ai_eval path=$ABCLI_OBJECT_ROOT/$object_name \
        python3 -m http.server $port
}
