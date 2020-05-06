#/usr/bin/#!/usr/bin/env python
#"""CracklePop.py, by Daniele Tenga, Jan 13, 2020
#This program prints out numbers from 1 to 100. If the number is divisible by 3,
#print Crackle instead of the number. If its divisible by 5, print Pop.
#if it's divisble by both 3 and 5, print CracklePop.
#"""


def main():
    for i in range (100):
        print ("i")

        if (i/3 == 0):
            print("Crackle")
        if (i/5 == 0):
            print("Pop")
        if (i/3 == 0 and 1/5 ==0):
            print("CracklePop!")
        else:
            print ("i")


if __name__ == '__main__':
    main()
