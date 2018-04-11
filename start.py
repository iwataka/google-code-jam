#!/usr/bin/env python

import os
import shutil
import sys

years = [int(p) for p in os.listdir('.') if p.isdigit()]
default_year = max(years)
year = input('Year (Default: %d): ' % default_year)
if year == '':
    year = str(default_year)

round_name = input('Round Name: ')
if round_name == '':
    print('Round name must not be empty')
    sys.exit(0)
round_path = os.path.join(year, round_name)

template_path = 'template'

while True:
    pbl_name = input('Problem Name (Empty means no more problem): ')
    if pbl_name == '':
        break

    if not os.path.exists(year):
        os.makedirs(year)
    if not os.path.exists(round_path):
        os.makedirs(round_path)

    pbl_path = os.path.join(round_path, pbl_name)
    if not os.path.exists(pbl_path):
        shutil.copytree(template_path, pbl_path, ignore=shutil.ignore_patterns('__pycache__'))
    else:
        print('%s already exists' % pbl_path)
        sys.exit(0)

print('> Now you are ready to go through fantastic time!')
print('> Enjoy and good luck!')
