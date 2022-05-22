#!/usr/bin/env python3

import argparse
from googletrans import Translator

def translate(text, src_lng=None, dest_lng=None):
    translator = Translator()
    if src_lng and dest_lng:
        return translator.translate(text, src=src_lng, dest=dest_lng)
    elif src_lng:
        return translator.translate(text, src=src_lng)
    elif dest_lng:
        return translator.translate(text, dest=dest_lng)
    else:
        return translator.translate(text)

parser = argparse.ArgumentParser()
parser.add_argument('text', type=str, help='text to translate')
parser.add_argument('-s', '--src', default=None, help='origin language of the text')
parser.add_argument('-d', '--dest', default=None, help='destiny language of the translation')
parser.add_argument('-v', '--verbose', help='show more information', action='store_true')

args = parser.parse_args()

tr = translate(args.text, args.src, args.dest)

if args.verbose:
    print(f'original text: {tr.origin}')
    print(f'translated text: {tr.text}')
    print(f'origin language: {tr.src}')
    print(f'destiny language: {tr.dest}')
else:
    print(tr.text)
