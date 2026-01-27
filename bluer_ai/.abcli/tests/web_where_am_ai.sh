#! /usr/bin/env bash

function test_bluer_ai_web_where_am_i() {
    if [[ "$BLUER_AI_INTERNET_OUTSIDE_IS_ACCESSIBLE" == 0 ]]; then
        bluer_ai_log_warning "outside is not accessible, test is disabled."
        return
    fi

    bluer_ai_web_where_am_i
}
