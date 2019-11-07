set3 = {2,3,5,7,11,13,17,19}

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("value", type = int)

args = parser.parse_args()

print((min(set3)<args.value) and (args.value<max(set3)))
