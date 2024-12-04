#!/usr/bin/env python3
# azce::highlights.py - Arizona Edwards
# Created: 2024-11-29 17:29-EST

import re
import argparse
from collections import deque, namedtuple
from ellipsize import ellipsize
from OutputWrapper import OutputWrapper
from HighlightsHtml import HighlightsHtml

re_link       = re.compile(r'\[(.*?)\]\((.*?)\)')
re_job        = re.compile(r'^# \[(.*)\]$')
re_list       = re.compile(r'^## (.*):$')
re_highlight  = re.compile(r'^(\s*)- (.*)$')
re_line       = re.compile(r'^(\s*)(\S+.*)$')

Parent = namedtuple('Parent', ['column', 'collector'])

class Link:
    otype = 'link'

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __str__(self):
        return f'[{self.title}]({self.url})]'

    def __repr__(self):
        return f'{self.otype}(Title="{self.title}", Url="{self.url}")'
    
    def desc(self):
        return f'{self.otype}-[{ellipsize.left(self.title,30)}]({ellipsize.right(self.url,30)})'
        
class Span:
    otype = 'span'

    def __init__(self, line_number, column, text, link=None):
        self.line_number = line_number
        self.column = column
        if link:
            self.link = link
            self._text = text # stored as the underlying text
        else:
            self._text = text
            self.link = None

    def spantype(self):
        if self.link:
            return 'link'
        else:
            return 'text'

    def text(self):
        return self.link.title if self.link else self._text

    def desc(self):
        return f'{self.otype}-{self.spantype()}-{self.line_number}:{self.column}-{ellipsize.center(self.text(), 40)}'
        
    def __str__(self):
        if self.link:
            return str(self.link)
        else:
            return self._text
        
    def __repr__(self):
        if self.link:
            return f'{self.otype}({self.line_number}:{self.column},{repr(self.link)})'
        else:
            return f'{self.otype}({self.line_number}:{self.column},Text("{self.text()}"))'
        
class Line:
    otype = 'line'

    def __init__(self, line_number, parent, column, text):
        self.line_number = line_number
        self.parent = parent
        self.column = column
        self.children = []
        self.text = text
        if text:
            links = re_link.finditer(text)
            textpos=0
            for link in links:
                if link.start() > textpos:
                    self.children.append(Span(self.line_number, textpos, text=text[textpos:link.start()]))
                self.children.append(Span(self.line_number, link.start(), text=text[link.start():link.end()], link=Link(link[1], link[2])))
                textpos = link.end()
            if textpos < len(text): 
                self.children.append(Span(self.line_number, textpos, text=text[textpos:]))

    def __str__(self):
        return ''.join([str(sub) for sub in self.children])

    def __repr__(self):
        rsubs = [repr(sub) for sub in self.children]
        return f'{self.otype}({self.line_number}:{self.column},{",".join(rsubs)})'
    
    def desc(self):
        return f'{self.otype}-{self.line_number}:{self.column}-{ellipsize.mid(self.text,30,20)}'
       
class Highlight:
    otype = 'highlight'

    def __init__(self, line_number, parent, level, column, text):
        self.line_number = line_number
        self.parent = parent
        self.level = level
        self.column = column
        self.prefix = ' ' * level + '- '
        self.children = [Line(line_number, self, column+2, text)]

    def __str__(self):
        return '\n'.join([str(sub) for sub in self.children])

    def __repr__(self):
        rsubs = [repr(sub) for sub in self.children]
        return f'{self.otype}({self.line_number},{self.level},{self.column},[{",".join(rsubs)}])'
    
    def push(self, child, pusher):
        if child.otype in ['line', 'highlight']:
          self.children.append(child)
        else:
            pusher.print_error(f'Can only push lines or highlights to Highlight. Cannot push {child.desc()}.')

    def desc(self):
        return f'{self.otype}-{self.line_number}:{self.column}-{len(self.children)}xSubs-{ellipsize.left(self.children[0].text,30)}'
                
class HighlightList:
    otype = 'highlightlist'

    def __init__(self, line, parent, caption, highlights=None):
        self.line = line
        self.parent = parent
        self.caption = caption
        self.level = 0
        self.column = 0
        self.highlights = highlights or []
        if caption:
            self.caption_type = 'highlights' if caption == "Highlights" else "challenges" if caption.startswith("Challenges") else caption.split()[0].lower()
        else:
            self.caption_type = 'none'
        
    def __str__(self):
        return '\n'.join([str(sub) for sub in self.highlights])
    
    def push(self, child, pusher):
        if child.otype == 'highlight':
            self.highlights.append(child)
        else:
            pusher.print_error(f'Can only push highlights to HighlightList. Cannot push {child.desc()}.') 
    
    def __repr__(self):
        rsubs = [repr(sub) for sub in self.highlights]
        return f'{self.otype}({self.line},{self.caption_type}[{",".join(rsubs)}])'
    
    def desc(self):
        return f'{self.otype}-{self.line}-{len(self.highlights)} {self.caption_type}'
    
class Job:
    otype = 'job'

    def __init__(self, line_number, jobid, highlights=None):
        self.line_number = line_number
        self.jobid = jobid
        self.highlights = highlights
        self.column = 0

    def __str__(self):
        return f'Job: {self.jobid}; Highlights: {str(self.highlights)}'

    def __repr__(self):
        return f'{self.otype}("{self.line_number},{self.jobid}",{repr(self.highlights)})'
    
    def push(self, child, pusher):
        if child.otype != 'highlightlist':
            pusher.print_error(f'Can only push highlight lists to Job. Cannot push {child.desc()}.') 
        if self.highlights:
            pusher.print_error(f'Job already has highlights {self.highlights.desc()}.') 
            pusher.continue_error(f' Cannot push {child.desc()}.')
        self.highlights = child

    def desc(self): 
        return f'{self.otype}-{self.line_number}-{self.jobid}'
    

class CV_Highlights:
    otype = 'cv_highlights'

    def __init__(self, jobs=None):
        self.jobs = jobs or []
        self.column = 0

    def __str__(self):
        return '\n'.join([str(sub) for sub in self.jobs])
    
    def __repr__(self):
        return f'{self.otype}([{",".join([repr(sub) for sub in self.jobs])}]'
    
    def desc(self):
        return f'{self.otype}-{len(self.jobs)}xJobs'
    
    def push(self, job, pusher):
        if job.otype != 'job':
            pusher.print_error(f'Can only push jobs to CV_Highlights. Cannot push {job.desc()}.')
        self.jobs.append(job)

class HighlightsReader:
    otype = 'reader'

    def __init__(self, options):
        self.cv_highlights = CV_Highlights()
        self.stack = deque()
        self.stack.append(Parent(0, self.cv_highlights))
        self.line_count = 0
        self.read_errors = 0
        self.read_warnings = 0
        self.stop = False
        self.parse_options(options)

    def parse_options(self, options):
        self.verbose = options.verbose or options.log
        self.log = OutputWrapper(ofile=options.log, noCloseIfFile=True, stderr=True)

    def __str__(self):
        return f'HighlightsReader of {str(self.cv_highlights)}'
    
    def __repr__(self):
        return f'{self.otype}-({self.line_count}xLines-{self.read_errors}xErrors-{self.read_warnings}xWarnings'\
                f'-stop={self.stop}-verbose={self.verbose}-{len(self.cv_highlights.jobs)}xJobs'\
                f'-[{"-".join([sub.collector.otype for sub in self.stack])}]'
    
    def desc(self): 
        return f'{self.otype}-{self.line_count}xLines-{self.read_errors}xErrors-{self.read_warnings}xWarnings'\
               f'-{len(self.cv_highlights.jobs)}xJobs-[{"-".join([sub.otype for sub in self.stack])}]'
    
    def print_message(self, message_level, message):
        if message_level == 'Error':
            self.print_error(message)
        elif message_level == 'Warning':
            self.print_warning(message)
        else:
            print(f'{message_level}: At line {self.line_count}: {message}', file=self.log)

    def print_warning(self, message):
        print(f'Warning: At line {self.line_count}: {message}', file=self.log)
        self.read_warnings += 1

    def print_error(self, message, fatal=False):
        print(f'Error: At line {self.line_count}: {message}', file=self.log)
        self.read_errors += 1
        if fatal:
            self.stop = True

    def continue_error(self, message):
        print(f'     - {message}', file=self.log)

    def is_stack_type(self, expected_types, actual_type):
        if not isinstance(expected_types, list):
            return expected_types == actual_type
        else:
            return actual_type in expected_types  
        
    def expected_type_names(self, expected_types):
        if not isinstance(expected_types, list):
            return expected_types
        elif len(expected_types) == 1:
            return expected_types[0]
        else:
            return f'one of {expected_types}'
  
    def stack_top_type(self):
        return self.stack[-1].collector.otype if self.stack else 'Empty'
    
    def stack_top_collector(self):
        return self.stack[-1].collector
    
    def stack_top_collector_desc(self):
        return self.stack[-1].collector.desc() if self.stack else 'Empty'
    
    def ensure_stack(self, expected_types, for_type, old_top_type=None):
        self.no_stack(expected_types, for_type, old_top_type) if not self.stack else None

    def no_stack(self, expected_types, for_type, old_top_type=None, constraint=None):
        expected = self.expected_type_names(expected_types)
        if constraint:
            expected += f' ({constraint})'
        for_name = ' for new ' + for_type if for_type else ''
        self.print_error(f'Stack is empty. Expected {expected} to be on stack{for_name}.', fatal=True)
        if old_top_type and old_top_type != 'Empty':
            self.continue_error(f'Found {old_top_type} on top without {expected} underneath.')

    def pop_stack_till(self, till_types, for_type):
        old_top_type = self.stack_top_type()
        while self.stack and not self.is_stack_type(till_types, self.stack_top_type()):
            if self.verbose:
                self.print_message('Info', f'"pop_stack_till()" Popping {self.stack_top_type()} from stack {self.stack_top_collector_desc()}.')
            self.stack.pop()
        self.ensure_stack(till_types, for_type, old_top_type)

    def expect_stack_top(self, expected_types, for_type, required=False, constraint=None):
        self.ensure_stack(expected_types, for_type)
        stack_top_type = self.stack_top_type()
        if not self.is_stack_type(expected_types, stack_top_type):
            expected = self.expected_type_names(expected_types)
            if constraint:
                expected += f' ({constraint})'
            for_name = ' for new ' + for_type if for_type else ''
            message_level = 'Error' if required else 'Warning'
            self.print_message(message_level, f'Expected {expected} on stack top{for_name}, found {stack_top_type}')
            if required:
                self.stop = True
            self.pop_stack_till(expected_types, for_type)
        else:
            if self.verbose:
                self.print_message('Info', f'"expect_stack_top()" Found {self.stack_top_type()} on stack top as {self.stack_top_collector_desc()}.')

    def push(self, child):
        if self.verbose:
            self.print_message('Info', f'Pushing {child.desc()} onto {self.stack_top_collector_desc()}.')
        self.stack[-1].collector.push(child, self)
        self.stack.append(Parent(child.column, child))

    def append(self, child):
        if self.verbose:
            self.print_message('Info', f'Appending {child.desc()} onto {self.stack_top_collector_desc()}.')
        self.stack[-1].collector.push(child, self)

    def push_highlight(self, for_level, for_column, for_type, text):
        if for_column == 0:
           self.pop_stack_till('highlightlist', 'highlight')
           self.push(Highlight(self.line_count, self.stack[-1].collector, for_level, for_column, text))
        else:
            target_column = for_column - 2;
            constraint=f'column=={target_column}'
            self.expect_stack_top('highlight', for_type, required=True, constraint=constraint)
            while self.stack and self.stack[-1].collector.column > target_column:
                if self.verbose:
                    self.print_message('Info', f'Popping {self.stack_top_collector_desc()} from stack, looking for column {target_column}.') 
                self.stack.pop()
            self.expect_stack_top('highlight', for_type, required=True, constraint=constraint)
            if not self.stack[-1].collector.column == target_column:
                self.print_error(f'Parent not found for {for_type} at column {for_column}.')
            elif for_type == 'highlight':
                self.push(Highlight(self.line_count, self.stack[-1].collector, for_level, for_column, text))
            else:
                self.append(Line(self.line_count, self.stack[-1].collector, for_column, text))                            

    def get_line_type(self, line):
        if (m := re_job.match(line)):
            return 'job', m
        elif (m := re_list.match(line)):
            return 'highlightlist', m
        elif (m := re_highlight.match(line)):
            return 'highlight', m
        elif (m := re_line.match(line)):
            return 'line', m
        else:
            return 'empty', None    

    def spacestrip(self, line):
        line_stripped = line.strip()
        if line_stripped:
            line_r_stripped = line.rstrip()
            if line_r_stripped != line.rstrip('\n'):
                self.print_warning('Trailing whitespace.')
            if '\t' in line_r_stripped:
                self.print_warning('Tabs.')
            if "  " in line_stripped:
                self.print_warning('Consecutive spaces.')
            return line_r_stripped
        else:
            return line_stripped

    def process_line(self, line):
        self.line_count += 1
        line = self.spacestrip(line)
        line_type, line_match = self.get_line_type(line)

        if line_type == 'empty':
            self.pop_stack_till('cv_highlights', 'empty')
        elif line_type == 'job':
            self.expect_stack_top('cv_highlights', 'job')
            self.push(Job(self.line_count, line_match.group(1)))
        elif line_type == 'highlightlist':
            self.expect_stack_top('job', 'highlightlist', required=True)
            self.push(HighlightList(self.line_count, self.stack_top_collector(), line_match.group(1)))
        elif line_type == 'highlight' or line_type == 'line':
            column = len(line_match.group(1))
            level = column // 2
            self.push_highlight(level, column, line_type, line_match.group(2))
        else:
            self.print_error(f'Line {self.line_count} does not match any pattern:')
            print(f' >>> {line}', file=self.log)

    def read(self, lines):
        for line in lines:
            if self.stop:
                print(f'Fatal: Halting after {self.read_errors} errors and {self.read_warnings} warnings.', file=self.log)
                print(repr(self.cv_highlights), file=self.log)
                break
            self.process_line(line)
        if self.read_errors:
            print(f'Error: {self.read_errors} errors found in input.', file=self.log)
        if self.read_warnings:  
            print(f'Warning: {self.read_warnings} warnings found in input.', file=self.log)
        return self.cv_highlights    
    
def main():
    parser = argparse.ArgumentParser(description='Reads a markdown file and extracts highlights.')
    parser.add_argument('input', type=argparse.FileType('r'), help='Input file')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('-l', '--log', type=argparse.FileType('w'), help='Log file')
    parser.add_argument('--str', type=argparse.FileType('w'), help='str() output file')
    parser.add_argument('--str-out', action='store_true', help='print str() to stdout')
    parser.add_argument('--repr', type=argparse.FileType('w'), help='repr() output file')
    parser.add_argument('--repr-out', action='store_true', help='print repr() to stdout')
    parser.add_argument('--html', type=argparse.FileType('w'), help='HTML output file')
    parser.add_argument('--html-out', action='store_true', help='print HTML to stdout')
    parser.add_argument('--csv', type=argparse.FileType('w'), help='Format output as CSV and output to file.')
    parser.add_argument('--csv-out', action='store_true', help='Format highlights as CSV and print to stdout')

    args = parser.parse_args()
    reader = HighlightsReader(args)
    cv_highlights = reader.read(args.input)

    if args.str:
        print(str(cv_highlights), file=args.str)
    if args.str_out:
        print("\n---===--- str(cv_highlights):")
        print(cv_highlights)

    if args.repr:
        print(repr(cv_highlights), file=args.repr)
    if args.repr_out:
        print("\n---===--- repr(cv_highlights):")
        print(repr(cv_highlights))

    if args.html:
        print(HighlightsHtml.make_cv_highlights(cv_highlights), file=args.html)
    if args.html_out:
        print("\n---===--- HTML output:")
        print(HighlightsHtml.make_cv_highlights(cv_highlights))

    if args.csv:
        print(HighlightsHtml.make_csv(cv_highlights), file=args.csv)
    if args.csv_out:
        print("\n---===--- CSV output:")
        print(HighlightsHtml.make_csv(cv_highlights))

if __name__ == '__main__':
    main()
