#!/bin/bash

CODE_DIR=/var/code
INPUT_DIR=/var/input
OUTPUT_DIR=/var/output
python ${CODE_DIR}/Main.py ${INPUT_DIR}/{{ data_id }}.in ${OUTPUT_DIR}/output.log 1>${OUTPUT_DIR}/stdout.log 2>${OUTPUT_DIR}/stderr.log
