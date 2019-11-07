import argparse

parser = argparse.ArgumentParser()

parser.add_argument("number", type=int)

args = parser.parse_args()

list4 = [32,15,3,"world",74,"bye"]
print("Before removing:",list4)
list4.remove(args.number)
print("After removing:",list4)