import argparse

parser = argparse.ArgumentParser()

parser.add_argument('text', type=str)
args = parser.parse_args()
print('uppercase', args.text.upper())
print('lowercase', args.text.lower())
