#! /usr/bin/env bash

function bluer_ai_web_get_ip() {
    ifconfig | grep inet | grep -v inet6 | grep -v 127.0.0.1 | awk '{print $2}'
}

export BLUER_AI_IP=$(bluer_ai_web_get_ip)
bluer_ai_log "IP: $BLUER_AI_IP"
