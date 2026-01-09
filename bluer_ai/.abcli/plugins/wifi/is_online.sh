#! /usr/bin/env bash

function bluer_ai_wifi_is_online() {
    local output=1

    local filename=~/$abcli_path_temp/is_online-$(bluer_ai_string_timestamp)

    curl -L https://github.com/kamangir \
        --output $filename \
        --connect-timeout 3
    [[ $? -ne 0 ]] &&
        output=0

    [[ -f "$filename" ]] &&
        rm -v $filename

    echo $output
}

export BLUER_AI_IS_ONLINE=$(bluer_ai_wifi_is_online)

if [[ "$BLUER_AI_IS_ONLINE" == true ]]; then
    bluer_ai_log "🛜 online."
else
    bluer_ai_log "⛓️‍💥 offline."
fi
