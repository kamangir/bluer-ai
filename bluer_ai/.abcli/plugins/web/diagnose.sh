#! /usr/bin/env bash

function bluer_ai_web_diagnose() {
    local connection=$(bluer_ai_option "$options" Zagros,Sion $BLUER_AI_WIFI_SSID)

    bluer_ai_log "connection: $connection through $BLUER_AI_WIFI_SSID"

    if [[ "$connection" == "Sion" ]]; then
        bluer_ai_log http://192.168.0.1
        bluer_ai_log http://192.168.0.1/settings.html#Advanced/Wireless/OnlineClients
        bluer_ai_log https://my.mci.ir/panel
    elif [[ "$connection" == "Zagros" ]]; then
        bluer_ai_log http://router.miwifi.com/cgi-bin/luci/diagnosis
    fi

    bluer_ai_log https://radar.arvancloud.ir/
}
