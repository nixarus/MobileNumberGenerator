#!/usr/bin/env python

from random import randint, choice
from datetime import datetime
import sys
import argparse

country_code = 234 #Nigeria
max_characters = 13 #Maximum characters of GSM numbers you want

pad_number = randint(0,9)
number_range = { 

        "mtn": [ 703, 803, 806, 813, 814, 816, 903], 
        "airtel": [ 701, 802, 808, 812, 902], 
        "glo": [ 705, 805, 807, 811, 815, 905], 
        "etisalat": [ 809, 817, 818, 909]
}


def generate(operator, count):
        
    output_file = operator.upper()+"_"+str(datetime.now().strftime('%d%m%Y%M%S'))+".csv"
    if operator.lower() in number_range.keys():
        try:
            assert count > 0
        except AssertionError:
            print "Count must be greater than 0"
            sys.exit()
        while count > 1:
            with open(output_file, "a") as out_file:
                randval = randint(00000000, 99999999)
                mobile_number = str(country_code)+str(choice(number_range[operator]))+str(randval)
                if len(mobile_number) < max_characters:
                    count_difference = int(max_characters) - len(mobile_number)
                    full_mobile_number = (lambda x: x + count_difference*str(randint(0,9)) )(mobile_number)
                    out_file.write(full_mobile_number[:max_characters]+"\n")
                    count -= 1
    else:
        print "Telco Operator profile not found"
        sys.exit()


parser = argparse.ArgumentParser(description='Generates GSM Mobile Numbers')
parser.add_argument('operator', type=str, help="Short name for operator e.g MTN, Glo")
parser.add_argument('count', type=int, help="Quantity of MSISDN needed")
args = parser.parse_args()


if __name__=='__main__':
    generate(args.operator, args.count)

