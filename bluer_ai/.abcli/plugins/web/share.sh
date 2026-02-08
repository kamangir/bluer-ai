#! /usr/bin/env bash

function bluer_ai_web_share() {
    local options=$1
    local do_open=$(bluer_ai_option_int "$options" open 1)
    local do_download=$(bluer_ai_option_int "$options" download 0)
    local do_receive=$(bluer_ai_option_int "$options" receive 1)
    local do_send=$(bluer_ai_option_int "$options" send 1)
    local do_upload=$(bluer_ai_option_int "$options" upload 0)

    bluer_ai_web_get_ip

    local object_name=$(bluer_ai_clarify_object $2 $BLUER_AI_WEB_OBJECT)
    local object_path=$ABCLI_OBJECT_ROOT/$object_name

    [[ "$do_download" == 1 ]] &&
        bluer_objects_download - \
            $object_name

    bluer_ai_log "@web: sharing object $object_name ..."

    local port_options=$3
    local port_send=$(bluer_ai_option "$port_options" port.send $BLUER_AI_WEB_SEND_PORT)
    local port_receive=$(bluer_ai_option "$port_options" port.receive $BLUER_AI_WEB_RECEIVE_PORT)

    [[ "$do_open" == 1 ]] &&
        open $object_path

    bluer_ai_badge - "⬆️⬇️"

    local url=""
    if [[ "$do_send" == 1 ]]; then
        url="http://$BLUER_AI_IP:$port_send/"
        bluer_ai_log "⬆️: $url"

        pushd $object_path >/dev/null

        bluer_ai_log "if there was a failure, \"lsof -i :$port_send\" and \"kill -9 <PID>\"".

        python3 -m http.server $port_send &
        local pid=$!

        popd >/dev/null
    fi

    if [[ "$do_receive" == 1 ]]; then
        url="http://$BLUER_AI_IP:$port_receive/"

        python3 -m bluer_objects.graphics \
            generate_qrcode \
            --url "$url" \
            --object_name $object_name
        [[ $? -ne 0 ]] && return 1

        bluer_ai_log "⬇️: $url"

        [[ "$do_open" == 1 ]] &&
            bluer_ai_browse $url

        bluer_ai_eval - \
            python3 -m bluer_ai.plugins.web.receive.app \
            --object_name $object_name \
            --port_receive $port_receive \
            "${@:4}"
    fi

    kill $pid

    bluer_ai_badge reset

    [[ "$do_upload" == 1 ]] &&
        bluer_objects_upload - \
            $object_name
}
