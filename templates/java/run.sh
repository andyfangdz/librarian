#!/bin/bash
set -e

CODE_DIR=/var/code
INPUT_DIR=/var/input
OUTPUT_DIR=/var/output
java -cp ${CODE_DIR} Main ${INPUT_DIR}/{{ data_id }}.in ${OUTPUT_DIR}/output.log 1>${OUTPUT_DIR}/stdout.log 2>${OUTPUT_DIR}/stderr.log
