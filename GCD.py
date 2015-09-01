__author__ = 'benjamin_sanchez'

#flow control and formatting
def main():
    aCount = int(input())
    for x in range(aCount):
        bNums = [int(x) for x in input().split()]
        GCDh = GCD(bNums[0], bNums[1])
        print ("(" + str(GCDh), str(int(LCM(GCDh, bNums))) + ")", end=" ")

#GCD finder
def GCD(a, b):
    notComplete = True
    answer = 0
    t = 0
    while notComplete:
        if a == b:
            answer = a
            notComplete = False
        else:
            if a>b:
                a -= b
            elif b>a:
                b -= a
    return answer

#lowest common multiplier
def LCM(gcd, nums):
    return (nums[0] * nums[1]) / gcd

main()