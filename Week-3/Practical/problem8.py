set1 = {1,2,3,4,5,6,7,8,9}
print("Initial set:",set1)

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("value", type = int)

args = parser.parse_args()

set1.add(args.value)
print("After adding:",set1)

