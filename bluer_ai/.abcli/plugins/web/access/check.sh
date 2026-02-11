#! /usr/bin/env bash

function bluer_ai_web_access_check() {
    local url=${1:-all}

    local options=$2
    local show_prep=$(bluer_ai_option_int "$options" prep 1)

    if [[ "$url" == "all" ]]; then
        local do_loop=$(bluer_ai_option_int "$options" loop 0)

        [[ "$show_prep" == 1 ]] &&
            bluer_ai_log "🔍 checking access..."

        if [[ "$do_loop" == 1 ]]; then
            bluer_ai_badge - "🔍"

            bluer_ai_watch \
                ~clear,~hr,~log,seconds=5,$options \
                bluer_ai_web_access_check \
                all \
                ~prep \
                --timestamp 1 \
                "${@:3}"

            bluer_ai_badge reset

            return
        fi

        export BLUER_AI_CLOUD_IS_ACCESSIBLE=$(
            bluer_ai_web_access_check \
                $BLUER_AI_CLOUD_CHECK_URL
        )

        export BLUER_AI_WEB_IS_ACCESSIBLE=$(
            bluer_ai_web_access_check \
                $BLUER_AI_WEB_CHECK_URL
        )

        export BLUER_AI_PYPI_IS_ACCESSIBLE=$(
            bluer_ai_web_access_check \
                https://pypi.org/
        )

        bluer_ai_web_access_log \
            "${@:3}"

        return

    fi

    python3 -m bluer_options.web.access \
        check \
        --url $url \
        "${@:3}"
}
