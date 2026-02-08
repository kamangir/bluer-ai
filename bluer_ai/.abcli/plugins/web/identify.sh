#! /usr/bin/env bash

function bluer_ai_web_identify() {
    local options=$1
    local do_loop=$(bluer_ai_option_int "$options" loop 0)

    local identification_options=$2

    if [[ "$do_loop" == 1 ]]; then
        bluer_ai_badge save "🔍"

        bluer_ai_watch \
            ~clear,~log,~hr,seconds=5,$options \
            bluer_ai_web_identify \
            timestamp,$identification_options \
            "${@:3}"

        bluer_ai_badge reset

        return
    fi

    local add_timestamp=$(bluer_ai_option_int "$options" timestamp 0)
    local do_log=$(bluer_ai_option_int "$options" log 1)
    local do_update=$(bluer_ai_option_int "$options" update 1)

    if [[ "$do_update" == 1 ]]; then
        export BLUER_AI_PYPI_IS_ACCESSIBLE=$(
            bluer_ai_web_is_accessible \
                ,$options \
                https://pypi.org/ \
                "${@:2}"
        )
        export BLUER_AI_CLOUD_IS_ACCESSIBLE=$(
            bluer_ai_web_is_accessible \
                ,$options \
                $BLUER_AI_CLOUD_CHECK_URL \
                "${@:2}"
        )
        export BLUER_AI_WEB_IS_ACCESSIBLE=$(
            bluer_ai_web_is_accessible \
                ,$options \
                $BLUER_AI_WEB_CHECK_URL \
                "${@:2}"
        )
    fi

    if [[ "$do_log" == 1 ]]; then
        bluer_ai_log $(
            python3 -m bluer_options.web \
                access_as_str \
                --timestamp $add_timestamp
        )
    fi
}
