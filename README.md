# Selecting-lines-from-stdin-Python-Code-Linux-Command:

1. Use the "cd" command to navigate to the folder where your data(q1_data.tsv.gz) and python script (line_selection.py) are stored.

2. To generalize python script(line_selection.py), I have used any() function to check if any column matches a pattern given in  query. any() checks all columns in a single line without needing an explicit loop.
  
3. Use the zless command to decompress q1_data.tsv.gz and pipe the output to your Python script:
   zless q1_data.tsv.gz | python3 line_selection.py
   
