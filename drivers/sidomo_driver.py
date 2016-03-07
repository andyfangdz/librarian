from sidomo import Container
from constants import CODE_TARGET, INPUT_TARGET, OUTPUT_TARGET


class SidomoDriver(object):
    def __init__(self, container, code_dir, input_dir, output_dir, script):
        self.volumes = [
            '%s:%s' % (code_dir, CODE_TARGET),
            '%s:%s' % (output_dir, OUTPUT_TARGET)
        ]
        if input_dir:
            self.volumes.append('%s:%s' % (input_dir, INPUT_TARGET))
        self.container = Container(container, volumes=self.volumes)
        self.container.__enter__()
        for line in self.container.run('/bin/sh -c "%s"' % script):
            print line
