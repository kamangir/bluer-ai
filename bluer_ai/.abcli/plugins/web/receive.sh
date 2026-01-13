#! /usr/bin/env bash

function bluer_ai_web_receive() {
    local options=$1
    local do_open=$(bluer_ai_option_int "$options" open 0)
    local do_upload=$(bluer_ai_option_int "$options" upload 0)
    local port=$(bluer_ai_option "$options" port 8001)

    local object_name=$(bluer_ai_clarify_object $2 web-$(bluer_ai_string_timestamp))
    local object_path=$ABCLI_OBJECT_ROOT/$object_name

    [[ "$do_open" == 1 ]] &&
        open $object_path

    bluer_ai_log "⬇️ http://$BLUER_AI_IP:$port/ -> $object_name"

    bluer_ai_badge "⬇️"

    bluer_ai_eval - \
        python3 -m bluer_ai.web.receive.app \
        --path $object_path \
        --port $port \
        "${@:3}"

    bluer_ai_badge "🌀"

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - \
            $object_name
}
