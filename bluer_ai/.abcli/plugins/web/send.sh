#! /usr/bin/env bash

function bluer_ai_web_send() {
    local options=$1
    local do_download=$(bluer_ai_option_int "$options" download 0)
    local port=$(bluer_ai_option "$options" port $BLUER_AI_WEB_SEND_PORT)
    local use_path=$(bluer_ai_option_int "$options" path 0)

    local path
    if [[ "$use_path" == 1 ]]; then
        path=$2
    else
        local object_name=$(bluer_ai_clarify_object $2 .)

        [[ "$do_download" == 1 ]] &&
            bluer_objects_download - \
                $object_name

        path=$ABCLI_OBJECT_ROOT/$object_name
    fi

    bluer_ai_log "⬆️ $path -> http://$BLUER_AI_IP:$port/"

    bluer_ai_badge "⬆️"

    bluer_ai_eval path=$path \
        python3 -m http.server $port \
        "${@:3}"

    bluer_ai_badge "🌀"
}
