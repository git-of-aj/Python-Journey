# challenge: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true

# check weird
def check_weird(n):
    if (n % 2 != 0) or (6<= n <= 20):
        print("Weird")
    else:
        print("Not Weird")


if __name__ == '__main__':
  # strip() removes spaces from left + right side
    n = int(input().strip())
    check_weird(n)
