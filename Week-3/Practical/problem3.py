import argparse

parser = argparse.ArgumentParser()

parser.add_argument("number", type=int)

args = parser.parse_args()

list2 = ["Hey",88,1,False,88,"python",2,1,"No"]
print("Number of 1s in list2:",list2.count(args.number))


