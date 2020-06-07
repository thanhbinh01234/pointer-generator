#!/bin/bash

DIR="$(readlink -f "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )/..")"

python pointer-generator/run_summarization.py \
    --mode=decode \
    --data_path="$DIR"/data/chunked/test_000.bin \
    --vocab_path="$DIR"/data/vocab \
    --log_root="$DIR"/models \
    --exp_name=pretrained_model_tf1.2.1 \
    --coverage=true \
    --once
