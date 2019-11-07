import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type = str)

args = parser.parse_args()
print(args.text.count("USA")) 
print(args.text.count("usa"))

print(args.text.replace("USA","Armenia"))
print(args.text.replace("usa","Armenia"))
