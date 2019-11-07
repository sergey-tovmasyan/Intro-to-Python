import argparse
import datetime
today = datetime.date.today()

parser = argparse.ArgumentParser()
parser.add_argument("num_y", type=int)
args = parser.parse_args()

parser = argparse.ArgumentParser()
parser.add_argument("num_d", type=int)
args = parser.parse_args()

print("Current date:",today)
print(args.num_y)
print(args.num_d)
      
#I cannot find where I made a mistake.