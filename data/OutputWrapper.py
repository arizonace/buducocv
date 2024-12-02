# azce::OutputWrapper.py - Arizona Edwards
# Created: 2024-11-24 18:39-EST

import sys
class OutputWrapper:
    def __init__(self, filename=None, encoding="utf-8", ofile=None, noCloseIfFile=False, stderr=False):
        if filename:
            self.output = open(filename, mode='w', encoding=encoding)
            self.noClose = False
        elif ofile:
            self.output = ofile
            self.noClose = noCloseIfFile
        else:
            self.output = sys.stderr if stderr else sys.stdout
            self.noClose = True

    def write(self, message):
        self.output.write(message)

    def writelines(self, lines):
        self.output.writelines(lines)

    def close(self):
        if self.output not in [sys.stdout, sys.stderr]:
            if not self.noClose:
                self.output.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
