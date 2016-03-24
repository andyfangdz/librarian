from Solution import Solution
import sys

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as content_file:
        a = int(content_file.readline())
        b = int(content_file.readline())

        with open(sys.argv[2], 'w') as output:
            out = str(Solution().aplusb(a, b)) + "\n"
            output.write(out)
