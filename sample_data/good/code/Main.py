from Solution import Solution
import sys

if __name__ == "__main__":
    content = ""
    with open(sys.argv[1], 'r') as content_file:
        content = content_file.read()
    with open(sys.argv[2], 'w') as output:
        output.write(Solution().run(content))
