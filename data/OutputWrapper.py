# azce::OutputWrapper.py - Arizona Edwards
# Created: 2024-11-24 18:39-EST

import sys
class OutputWrapper:
    def __init__(self, filename=None, encoding="utf-8"):
        if filename:
            self.output = open(filename, mode='w', encoding=encoding)
        else:
            self.output = sys.stdout

    def write(self, message):
        self.output.write(message)

    def writelines(self, lines):
        self.output.writelines(lines)

    def close(self):
        if self.output is not sys.stdout:
            self.output.close()
            
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
