#!/usr/bin/env python3
"""
PreToolUse hook for Edit/Write: blocks edits that touch CLAUDE:PROTECT regions in g1.tex.

Protected regions are marked in g1.tex with:
  % CLAUDE:PROTECT
  ...content...
  % CLAUDE:END-PROTECT

The hook receives JSON on stdin and exits 2 (block) if the proposed edit
overlaps a protected region, or 0 (allow) otherwise.
"""

import json
import sys
import os
import re

TEX_FILE = os.path.join(os.path.dirname(__file__), '..', 'g1.tex')

def load_protected_ranges(path):
    """Return list of (start_line, end_line) 1-based inclusive ranges."""
    ranges = []
    try:
        with open(path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return ranges

    start = None
    for i, line in enumerate(lines, 1):
        if re.search(r'%\s*CLAUDE:PROTECT\b', line):
            start = i
        elif re.search(r'%\s*CLAUDE:END-PROTECT\b', line):
            if start is not None:
                ranges.append((start, i))
                start = None
    return ranges


def find_in_file(content, old_string):
    """Return (start_line, end_line) 1-based of first occurrence of old_string in content."""
    pos = content.find(old_string)
    if pos == -1:
        return None, None
    start_line = content[:pos].count('\n') + 1
    end_line = start_line + old_string.count('\n')
    return start_line, end_line


def overlaps(a_start, a_end, b_start, b_end):
    return a_start <= b_end and b_start <= a_end


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # malformed input: let it through

    tool = data.get('tool_name', '')
    inp = data.get('tool_input', {})

    file_path = inp.get('file_path', '')
    if not file_path.endswith('g1.tex'):
        sys.exit(0)

    protected = load_protected_ranges(TEX_FILE)
    if not protected:
        sys.exit(0)

    if tool == 'Edit':
        old_string = inp.get('old_string', '')
        if not old_string:
            sys.exit(0)
        try:
            with open(file_path, 'r') as f:
                content = f.read()
        except Exception:
            sys.exit(0)
        edit_start, edit_end = find_in_file(content, old_string)
        if edit_start is None:
            sys.exit(0)
        for p_start, p_end in protected:
            if overlaps(edit_start, edit_end, p_start, p_end):
                result = {
                    "decision": "block",
                    "reason": f"Edit overlaps a CLAUDE:PROTECT region (lines {p_start}–{p_end} of g1.tex). Remove the % CLAUDE:PROTECT marker to allow edits here.",
                }
                print(json.dumps(result))
                sys.exit(0)

    elif tool == 'Write':
        # Write replaces the whole file — block if any protected regions exist
        # (they'd be overwritten by the new content unless they appear there too)
        old_content_path = file_path
        new_content = inp.get('content', '')
        # Check that every protected region still appears verbatim in new content
        try:
            with open(old_content_path, 'r') as f:
                old_content = f.read()
        except Exception:
            sys.exit(0)
        old_lines = old_content.splitlines()
        for p_start, p_end in protected:
            region = '\n'.join(old_lines[p_start - 1 : p_end])
            if region not in new_content:
                result = {
                    "decision": "block",
                    "reason": f"Write to g1.tex would modify or remove a CLAUDE:PROTECT region (lines {p_start}–{p_end}). Remove the % CLAUDE:PROTECT marker to allow changes there.",
                }
                print(json.dumps(result))
                sys.exit(0)

    sys.exit(0)


if __name__ == '__main__':
    main()
