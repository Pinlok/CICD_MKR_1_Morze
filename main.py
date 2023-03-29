def compare_files(file1, file2):

    with open(file1, 'r') as f1:
        lines1 = set(f1.readlines())
    with open(file2, 'r') as f2:
        lines2 = set(f2.readlines())