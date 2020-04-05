#! python3

import argparse

my_parser=argparse.ArgumentParser(description='Create a short bio')

#add the arguments

my_parser.add_argument('Name',metavar='Name',type=str,help='Name for the bio')
my_parser.add_argument('Age',metavar='Age',type=int,help='Age for the bio')

args=my_parser.parse_args()

bioName=args.Name
bioAge=args.Age

print("Hello my name is "+bioName + ". I am "+ str(bioAge) + " years old.")
