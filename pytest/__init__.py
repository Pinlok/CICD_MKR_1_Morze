import os

def test_file_comparison():
    # Create two files with test data
    file1_name = 'file1.txt'
    file2_name = 'file2.txt'
    with open(file1_name, 'w') as file1:
        file1.write('Line 1\nLine 2\nLine 3\n')
    with open(file2_name, 'w') as file2:
        file2.write('Line 1\nLine 3\nLine 4\n')

    # Run the script to compare the files
    exec(open('compare_files.py').read())

    # Check that same.txt contains the expected lines
    with open('same.txt', 'r') as same_file:
        same_lines = same_file.readlines()
    assert same_lines == ['Line 1\n', 'Line 3\n']

    # Check that diff.txt contains the expected lines
    with open('diff.txt', 'r') as diff_file:
        diff_lines = diff_file.readlines()
    assert diff_lines == ['Line 2\n', 'Line 4\n']

    # Clean up the test files and output files
    os.remove(file1_name)
    os.remove(file2_name)
    os.remove('same.txt')
    os.remove('diff.txt')
