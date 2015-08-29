__author__ = 'benjamin_sanchez'

#flow control and formatting
def main():
    aCount = int(input())
    for x in range(aCount):
        bNums = [int(x) for x in input().split()]
        GCDh = GCD(bNums[0], bNums[1])
        print ("(" + str(GCDh), str(LCM(GCDh, bNums)) + ")", end=" ")
        print (LCM(bNums))

#GCD finder
def GCD(a, b):
    notComplete = True
    while notComplete:
        pass

def LCM(gcd, nums):
    #do stuff

main()