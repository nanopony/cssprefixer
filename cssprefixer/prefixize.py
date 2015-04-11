#!/usr/bin/env python

# CSSPrefixer
# Copyright 2015 Nanopony, 2010-2012 Greg V. <floatboth@me.com>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from cssprefixer.engine import process
import sys
import argparse
import logging
import os

def _prepare_argparser():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Input CSS file")
    parser.add_argument("-m", "--mute", help="Don't check for errors")
   
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-o", "--output", help="Specity output filename", type=str)
    group.add_argument("-i", "--inplace", help="Convert CSS in-place", action="store_true")
    group.add_argument("-s", "--suffix", help="Add suffix")
    
    return parser

def clean_css(filename, mute = True):
    with open(filename) as f:
        raw = f.read()
        css = process(raw, minify=False, silent = mute)
    return css

def main():
    args = _prepare_argparser().parse_args()
    cleaned = clean_css(args.filename, mute = args.mute)  
    if (args.inplace is False and args.output is None and args.suffix is None):
        print(cleaned)
    else:
        if (args.suffix is not None):
            path, ext = os.path.splitext(args.filename)
            path = path + '.%s'%args.suffix + ext
        elif (args.output is not None):
            path = args.output
        else:
            path = args.filename

        with open(path, 'w') as w:
            w.write(cleaned)
        print('Cleaned CSS saved to %s'%path)

if __name__ == '__main__':
    main()