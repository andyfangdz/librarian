from drivers.sidomo_driver import SidomoDriver as sandbox
import os
import tempfile
import filecmp
import pyprind

EXAMPLE_PYTHON = """\
#!/bin/bash
set -e

CODE_DIR=/var/code
INPUT_DIR=/var/input
OUTPUT_DIR=/var/output
python ${CODE_DIR}/Main.py ${INPUT_DIR}/%d.in ${OUTPUT_DIR}/output.log 1>${OUTPUT_DIR}/stdout.log 2>${OUTPUT_DIR}/stderr.log
"""

EXAMPLE_JAVAC = """\
#!/bin/bash
set -e

CODE_DIR=/var/code
INPUT_DIR=/var/input
OUTPUT_DIR=/var/output
javac ${CODE_DIR}/Main.java -d ${OUTPUT_DIR} -cp ${CODE_DIR}
"""

EXAMPLE_JAVA = """\
#!/bin/bash
set -e

CODE_DIR=/var/code
INPUT_DIR=/var/input
OUTPUT_DIR=/var/output
java -cp ${CODE_DIR} Main
"""



EXAMPLE_DATA_RANGE = range(1, 3)

JAVA_IMAGE = 'vixns/java8'
CPP_IMAGE = 'gcc'
PYTHON_IMAGE = 'python:alpine'

if __name__ == "__main__":
    sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample_data/good')
    bar = pyprind.ProgBar(len(EXAMPLE_DATA_RANGE))
    code_path = os.path.join(sample_dir, 'code')
    tmp_path = tempfile.mkdtemp()
    input_path = os.path.join(sample_dir, 'input')
    sandbox(JAVA_IMAGE, code_path, None, tmp_path, EXAMPLE_JAVAC)
    for i in EXAMPLE_DATA_RANGE:
        output_tmp = tempfile.mkdtemp()
        sandbox(JAVA_IMAGE, tmp_path, input_path, output_tmp, EXAMPLE_JAVA)
        # sandbox('frolvlad/alpine-oraclejdk8:cleaned',
        bar.update()
        # print filecmp.cmp(os.path.join(sample_dir, 'output/%d.out' % i),
                          # os.path.join(temp_dir, 'output.log'))
    print "Temp folder: %s" % temp_dir
