"""
This script processes a CSV file for string escaping and writes the output to a new file.
It reads from 'allCountries.txt', applies necessary string escaping to each row, and
writes the processed rows to 'outputallCountries.txt'. It also counts the total number of
rows processed and the number of changes made.
"""

import csv

input_file = r'D:\source\repos\Ancestral_Insights\Ancestral Insights\Ancestral Insights MVP\allCountries\allCountries.txt'
output_file = r'D:\source\repos\Ancestral_Insights\Ancestral Insights\Ancestral Insights MVP\allCountries\outputallCountries.txt'

row_count = 0
changes_count = 0

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, quoting=csv.QUOTE_ALL)

    for row in reader:
        original_row = row[:]  # Make a copy of the original row

        # Here, implement the logic for any changes needed for string escaping
        # For example:
        # row = [s.replace('"', '""') for s in row]  # Escape double quotes
        # if row != original_row:
        #     changes_count += 1

        writer.writerow(row)
        row_count += 1

print(f"Total rows processed: {row_count}")
print(f"Total changes made: {changes_count}")
