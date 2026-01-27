#! /usr/bin/env bash

function bluer_ai_web_identify() {
    local options=$1
    local do_log=$(bluer_ai_option_int "$options" log 1)
    local do_loop=$(bluer_ai_option_int "$options" loop 0)
    local add_timestamp=$(bluer_ai_option_int "$options" timestamp 0)
    local max_count=$(bluer_ai_option "$options" count -1)

    if [[ "$do_loop" == 1 ]]; then
        local sleep_period=$(bluer_ai_option "$options" sleep 5)

        local loop_count=0
        while true; do
            bluer_ai_web_identify \
                timestamp,$options,~loop \
                "${@:2}"

            loop_count=$((loop_count + 1))
            if [[ "$max_count" != -1 ]] &&
                [[ "$loop_count" -ge "$max_count" ]]; then
                break
            fi

            sleep $sleep_period
        done

        return
    fi

    export BLUER_AI_PYPI_IS_ACCESSIBLE=$(
        bluer_ai_web_is_accessible \
            https://pypi.org/ \
            "${@:2}"
    )
    export BLUER_AI_STORAGE_IS_ACCESSIBLE=$(
        bluer_ai_web_is_accessible \
            $BLUER_AI_STORAGE_CHECK_URL \
            "${@:2}"
    )
    export BLUER_AI_WEB_IS_ACCESSIBLE=$(
        bluer_ai_web_is_accessible \
            $BLUER_AI_WEB_CHECK_URL \
            "${@:2}"
    )

    if [[ "$do_log" == 1 ]]; then
        bluer_ai_log $(
            python3 -m bluer_options.web \
                access_as_str \
                --timestamp $add_timestamp
        )
    fi
}
