import sys

x = 0
while x <= 999999:
    # print("\b "*6, end="", flush=True)
    sys.stdout.write('\010'*6)
    print(('0'*(6-len(str(x)))) + str(x), end="")
    x += 1
