
data_file = "data/ten_line_file.log"
#data_file = "data/less_than_ten_line_file.log"
#data_file = "data/bigfile_450_mb.log"
#data_file = "data/bigfile_11_gb.log"
with open(data_file) as read_file: 
    for line in (read_file.readlines() [-10:]):
        print(line)

# 1. This solution is fine for small to medium sized files.  See comments below on
# how to make this solution more efficient. 

# 2. Edge cases:
#     - What if the file was less than ten lines? We'd want a test to make sure the above snippet worked.
#     - What if one line was 8gb long. This code would more than likey not worked
#     - Not an edge case, but we'd want to add some try/except check to make sure our log file exists.

# 3. Large files:  
# This implementation would not work on large files on most machines ( 4GB+ ). It wouldn't work well 
# for a tail of large files, but would be okay for parsing < 1GB txt and CSV files.

# 4. If we were writing a tail for large files we'd want to do open the file in binary formart. Then 
# locate the end of the file.  Set a positional marker and then have a conditional testing if we're 
# past that marker.  I've added some pseudocode in tail_large_files.py.  I think this probably could be
# done in native python ( no external libs). Though I wouldn't be surpised if there is a nice package out there
# that does this for you.