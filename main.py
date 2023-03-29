with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2, open('same.txt', 'w') as same_file, open('diff.txt', 'w') as diff_file:
    # Read the contents of the two files into lists
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()
    # Write the lines that are in both files to same.txt
    same_lines = set(file1_lines) & set(file2_lines)
    for line in same_lines:
        same_file.write(line)
        diff_lines = set(file1_lines) ^ set(file2_lines)
        for line in diff_lines:
            diff_file.write(line)