import jinja2
import os

TEMPLATE_DIR = os.path.dirname(__file__)
loader = jinja2.FileSystemLoader([TEMPLATE_DIR], followlinks=True)
env = jinja2.Environment(loader=loader)

templates = {
    'cpp': {
        'compile': env.get_template('cpp/compile.sh'),
        'run': env.get_template('cpp/run.sh'),
        'image': 'gcc'
    },
    'java': {
        'compile': env.get_template('java/compile.sh'),
        'run': env.get_template('java/run.sh'),
        'image': 'vixns/java8'
    },
    'python': {
        'compile': None,
        'run': env.get_template('python/run.sh'),
        'image': 'python:alpine'
    }
}