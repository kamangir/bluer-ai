#! /usr/bin/env bash

function bluer_ai_web_access_log() {
    bluer_ai_log $(
        python3 -m bluer_options.web.access \
            as_str \
            "$@"
    )
}

bluer_ai_web_access_check all
