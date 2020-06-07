#!/bin/bash

import sys
import struct
import tensorflow as tf
from tensorflow.core.example import example_pb2


dm_single_close_quote = u'\u2019' # unicode
dm_double_close_quote = u'\u201d'
END_TOKENS = ['.', '!', '?', '...', "'", "`", '"', dm_single_close_quote, dm_double_close_quote, ")"] # acceptable ways to end a sentence
SENTENCE_START = '<s>'
SENTENCE_END = '</s>'


def fix_missing_period(line):
    """Adds a period to a line that is missing a period"""
    if not line or line[-1] in END_TOKENS:
        return line
    return f"{line}."


def write_to_bin(tokenized_file, outfile):
    lines = []
    with open(tokenized_file, 'r') as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            lines.append(fix_missing_period(line.lower()))
    tokenized = ' '.join(lines).encode()
    tf_example = example_pb2.Example()
    tf_example.features.feature['article'].bytes_list.value.extend([tokenized])
    tf_example.features.feature['abstract'].bytes_list.value.extend([b''])
    tf_example_str = tf_example.SerializeToString()
    str_len = len(tf_example_str)
    with open(outfile, 'wb') as fout:
        fout.write(struct.pack('q', str_len))
        fout.write(struct.pack('%ds' % str_len, tf_example_str))
    
if __name__ == "__main__":
    output = sys.argv[1]
    tokenized_file = sys.argv[2]
    write_to_bin(tokenized_file, output)
