###### Question No. 1 

import sys

# Load patterns into a set for quick lookup
with open('to_select.tsv', 'r') as f:
    patterns = set(line.strip() for line in f)

# Read from stdin
for line in sys.stdin:
    columns = line.strip().split('\t')
    for column in columns:
        if column in patterns:
            print(line.strip())
            break
'''            
#bash
zcat data/q1_data.tsv.gz | python3 select_lines.py
'''

