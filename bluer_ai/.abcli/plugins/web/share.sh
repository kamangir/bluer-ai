#! /usr/bin/env bash

function bluer_ai_web_share() {
    local options=$1
    local do_download=$(bluer_ai_option_int "$options" download 0)
    local do_upload=$(bluer_ai_option_int "$options" upload 0)
    local port_send=$(bluer_ai_option "$options" port.send $BLUER_AI_WEB_SEND_PORT)
    local port_receive=$(bluer_ai_option "$options" port.receive $BLUER_AI_WEB_RECEIVE_PORT)
    local use_path=$(bluer_ai_option_int "$options" path 0)

    local path
    if [[ "$use_path" == 1 ]]; then
        path=$2
    else
        local object_name=$(bluer_ai_clarify_object $2 web-$(bluer_ai_string_timestamp))

        [[ "$do_download" == 1 ]] &&
            bluer_objects_download - \
                $object_name

        path=$ABCLI_OBJECT_ROOT/$object_name
    fi

    bluer_ai_log "sharing $path ..."

    bluer_ai_badge "⬆️⬇️"

    bluer_ai_log "⬆️ -> http://$BLUER_AI_IP:$port_send/"
    pushd $path >/dev/null
    python3 -m http.server $port_send &
    local pid=$!
    popd >/dev/null

    bluer_ai_log "⬇️ <- http://$BLUER_AI_IP:$port_receive/"
    bluer_ai_eval - \
        python3 -m bluer_ai.web.receive.app \
        --path $path \
        --port $port_receive \
        "${@:3}"

    kill $pid

    bluer_ai_badge "🌀"

    if [[ "$use_path" == 0 ]]; then
        [[ "$do_upload" == 1 ]] &&
            bluer_objects_upload - \
                $object_name
    fi
}
