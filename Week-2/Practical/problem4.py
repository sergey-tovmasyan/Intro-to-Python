import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--age", type=int)

args = parser.parse_args()
print ("Happy Birthday, you are already", args.age, "years old!")