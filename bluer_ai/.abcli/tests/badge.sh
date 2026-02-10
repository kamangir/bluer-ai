#! /usr/bin/env bash

function test_bluer_ai_badge() {
    bluer_ai_badge save
    [[ $? -ne 0 ]] && return 1

    bluer_ai_badge - "🚀"
    [[ $? -ne 0 ]] && return 1

    bluer_ai_badge clear
    [[ $? -ne 0 ]] && return 1

    bluer_ai_badge reset
}
