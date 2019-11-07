set2 = {1,3,5,7,9,11}
print("Before removing:",set2)

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("value", type = int)

args = parser.parse_args()

set2.remove(args.value)
print("After removing:",set2)

