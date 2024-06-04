import sys


def count_lines(filename):
    """Counts the number of lines in a file.

    Args:
        filename (str): The path to the file.

    Returns:
        The number of lines in the file (integer).
    """

    try:
        with open(filename, 'r') as file:
            num_lines = sum(1 for _ in file)
        return num_lines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return 0

if len(sys.argv) > 1:
    filename = sys.argv[1]
    line_count = count_lines(filename)
    if line_count > 0:
        print(f"File '{filename}' has {line_count} lines.")
    else:
        print("Usage: script_name.py filename")
