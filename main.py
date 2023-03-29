with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2, open('same.txt', 'w') as same_file, open('diff.txt', 'w') as diff_file:
    # Read the contents of the two files into lists
    file1_lines = file1.readlines()
    file2_lines = file2.readlines()