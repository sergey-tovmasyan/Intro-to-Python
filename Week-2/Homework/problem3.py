import argparse

parser = argparse.ArgumentParser()

parser.add_argument("text", type = str)

args = parser.parse_args()
print("The given text:", args.text)


parser = argparse.ArgumentParser()

parser.add_argument("first_word", type = str)

args = parser.parse_args()
print("First word:", args.first_word)


parser = argparse.ArgumentParser()

parser.add_argument("second_word", type = str)

args = parser.parse_args()
print("Second word:", args.second_word)




