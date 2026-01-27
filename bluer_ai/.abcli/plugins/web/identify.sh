#! /usr/bin/env bash

function bluer_ai_web_identify() {
    local options=$1
    local do_log=$(bluer_ai_option_int "$options" log 1)
    local do_loop=$(bluer_ai_option_int "$options" loop 0)
    local add_timestamp=$(bluer_ai_option_int "$options" timestamp 0)

    if [[ "$do_loop" == 1 ]]; then
        local sleep_period=$(bluer_ai_option "$options" sleep 5)

        while true; do
            eval bluer_ai_web_identify \
                timestamp,$options,~loop \
                "${@:2}"

            sleep $sleep_period
        done

        return
    fi

    export BLUER_AI_INTERNET_INSIDE_IS_ACCESSIBLE=$(
        bluer_ai_web_is_accessible \
            $BLUER_AI_INTERNET_INSIDE_CHECK_URL \
            "${@:2}"
    )
    export BLUER_AI_INTERNET_OUTSIDE_IS_ACCESSIBLE=$(
        bluer_ai_web_is_accessible \
            $BLUER_AI_INTERNET_OUTSIDE_CHECK_URL \
            "${@:2}"
    )

    if [[ "$do_log" == 1 ]]; then
        local message="internet:"

        if [[ "$add_timestamp" == 1 ]]; then
            message="$message $(bluer_ai_string_timestamp)"
        fi

        message="$message 🇮🇷"
        if [[ "$BLUER_AI_INTERNET_INSIDE_IS_ACCESSIBLE" == 1 ]]; then
            message="$message ✅"
        else
            message="$message 🛑"
        fi

        message="$message | 🌍"
        if [[ "$BLUER_AI_INTERNET_OUTSIDE_IS_ACCESSIBLE" == 1 ]]; then
            message="$message ✅"
        else
            message="$message 🛑"
        fi

        bluer_ai_log "$message"
    fi

}
