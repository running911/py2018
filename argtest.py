#!/usr/bin/env python3
#encoding:utf-8

import argparse

parser=argparse.ArgumentParser(description="This is an example program")
parser.add_argument('echo',help='echo the string')
parser.add_argument('-v',type=int,choices=[0,1,2],help='you can chose 0,1 or 2')
args=parser.parse_args()
print('The man is {} and your choice is:{}'.format(args.echo,args.v))
