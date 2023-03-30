#! /usr/bin/env python3
# Name:         messier.py
# Author:       Earl John Gallarde
# Version:      1.0
# Description:  

"""
    DocString:
"""

import sys

for line in open('messier.txt'):
    if not line:
        break
    else:
        if line.startswith('M'):
            m_num = line[:6].rstrip()
            cmn_name = line[6:40].strip()
            if cmn_name == '-':
                cmn_name = 'no name'
            obj_type = line[40:64].strip()
            constellation = line[64:].strip()
            print(f"|{m_num} | {cmn_name} | {obj_type} |{constellation}|")

sys.exit(0)