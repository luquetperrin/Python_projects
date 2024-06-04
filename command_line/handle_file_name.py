# Handle script name

import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
    print(f"Opening file: {filename}")
else:
    print("Please provide a filename as an argument.")
