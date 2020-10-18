#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on October 2020
# This program states all integers from 1000 to 2000

def main():
    # This function states all integers from 1000 to 2000

    # Input
    counter = 0

    # Process & Output
    print("Here are all the valid RGB values:")
    print("")

    for counter in range(1000, 2001):
        if counter % 5 == 0:
            if counter == 2000:
                print("2000")
            else:
                print("{0} {1} {2} {3} {4}"
                      .format(counter, counter + 1, counter + 2, counter + 3,
                              counter + 4))


if __name__ == "__main__":
    main()
