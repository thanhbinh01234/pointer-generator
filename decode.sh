#/bin/bash

PDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
DIR="$(readlink -f "$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )/..")"

bin_file="$(mktemp --suffix=.bin)"
infile="$1"

python "$PDIR"/gen_bin.py "$bin_file" "$infile" && \
python "$PDIR"/run_summarization.py \
    --mode=decode \
    --data_path="$bin_file" \
    --vocab_path="$DIR"/data/vocab \
    --log_root="$DIR"/models \
    --exp_name=pretrained_model_tf1.2.1 \
    --coverage=true \
    --once
