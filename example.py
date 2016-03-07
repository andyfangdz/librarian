from drivers.sidomo_driver import SidomoDriver as sandbox
import os
import tempfile
import filecmp

EXAMPLE_PYTHON = """\
#!/bin/bash
set -e

CODE_DIR=/var/code
INPUT_DIR=/var/input
OUTPUT_DIR=/var/output
python ${CODE_DIR}/Main.py ${INPUT_DIR}/%d.in ${OUTPUT_DIR}/output.log 1>${OUTPUT_DIR}/stdout.log 2>${OUTPUT_DIR}/stderr.log
"""

EXAMPLE_DATA_RANGE = range(1, 3)

if __name__ == "__main__":
    temp_dir = tempfile.mkdtemp()
    sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample_data/good')
    for i in EXAMPLE_DATA_RANGE:
        sandbox('python:alpine',
                os.path.join(sample_dir, 'code'),
                os.path.join(sample_dir, 'input'),
                temp_dir,
                EXAMPLE_PYTHON % i)
        print filecmp.cmp(os.path.join(sample_dir, 'output/%d.out' % i),
                          os.path.join(temp_dir, 'output.log'))
    print "Temp folder: %s" % temp_dir
