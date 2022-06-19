#!/usr/bin/env python3

from sys import argv
from random import choice


def interactive_compare(tier1, tier2):
    while True:
        print("Which of these items is greater?")
        # select random element from each tier to avoid repetitive-sounding questions
        selection = input(
            f"[1] {choice(tier1)} or [2] {choice(tier2)} or [0] equal: ")
        print()  # newline for readability
        if selection == "1":
            return 1
        elif selection == "2":
            return -1
        elif selection == "0":
            return 0
        else:
            print("Please enter either '0' or '1' or '2'")


# quicksort since we try to minimize comparisons
# tier: list of elements, initially each list has one element
# tiers: list of tiers
def tier_sort(tiers, cmp):
    if len(tiers) <= 1:
        return tiers
    pivot = tiers[0]
    lesser = []
    greater = []
    for el in tiers[1:]:
        c = cmp(el, pivot)
        if c < 0:
            lesser.append(el)
        elif c == 0:
            # el == pivot -> merge el and pivot
            pivot += el
        else:
            greater.append(el)
    return tier_sort(lesser, cmp) + [pivot] + tier_sort(greater, cmp)


def print_tiers(tiers):
    for i, tier in enumerate(reversed(tiers)):
        print(f"{i+1}. {' - '.join(tier)}")


if __name__ == "__main__":
    tiers = [[el] for el in argv[1:]]
    sorted_tiers = tier_sort(tiers, cmp=interactive_compare)
    print_tiers(sorted_tiers)
