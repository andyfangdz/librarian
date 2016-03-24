from drivers.sidomo_driver import SidomoDriver as sandbox
import os
import tempfile
import filecmp
import pyprind
import sys
import shutil
from templates import templates
import difflib

EXAMPLE_DATA_RANGE = range(1, 3) * 5
CLEANUP = True
sample_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample_data/good')

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def should_compile(lang_conf):
    return "compile" in lang_conf and lang_conf["compile"]


if __name__ == "__main__":
    JUDGE_LANG = sys.argv[1]
    code_path = os.path.join(sample_dir, 'code')
    input_path = os.path.join(sample_dir, 'input')
    temp_code_path = tempfile.mkdtemp()
    temp_input_path = tempfile.mkdtemp()
    compile_output = tempfile.mkdtemp()

    copytree(input_path, temp_input_path)
    copytree(code_path, temp_code_path)
    
    lang_conf = templates[JUDGE_LANG]
    
    if should_compile(lang_conf):
        sandbox(lang_conf["image"], temp_code_path, None, compile_output, lang_conf["compile"].render())
        if os.path.exists(os.path.join(compile_output, 'compile_failure')):
            print "Compile Failed. Error message:"
            with open(os.path.join(compile_output, 'stderr.log'), 'r') as stderr:
                print stderr.read()
            if CLEANUP:
                shutil.rmtree(compile_output)
                shutil.rmtree(temp_code_path)
                shutil.rmtree(temp_input_path)
            exit(-1)

    results = []
    bar = pyprind.ProgBar(len(EXAMPLE_DATA_RANGE))
    for i in EXAMPLE_DATA_RANGE:
        output_tmp = tempfile.mkdtemp()
        sandbox(lang_conf["image"], temp_code_path, temp_input_path, output_tmp, lang_conf["run"].render(data_id=i))
        # sandbox('frolvlad/alpine-oraclejdk8:cleaned',
        
        original_output = os.path.join(sample_dir, 'output/%d.out' % i)
        user_output = os.path.join(output_tmp, 'output.log')

        results.append(filecmp.cmp(original_output, user_output))
        bar.update()
        if not results[-1]:
            original_lines = list(open(original_output, 'r'))
            user_lines = list(open(user_output, 'r'))
            differ = difflib.Differ()
            print '\n'.join(differ.compare(original_lines, user_lines))
            if CLEANUP:
                shutil.rmtree(output_tmp)
                
            break
        if CLEANUP:
            shutil.rmtree(output_tmp)
        

    if CLEANUP:
        shutil.rmtree(compile_output)
        shutil.rmtree(temp_code_path)
        shutil.rmtree(temp_input_path)
    print "Temp folder: %s" % output_tmp
    print results
