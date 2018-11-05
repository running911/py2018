#!/usr/bin/env python
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("echo",help='echo the string you use here')
parser.add_argument('hello',help='just say hello to you')
args=parser.parse_args()
print(args.echo,args.hello)
