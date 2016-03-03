import sys, os
from random import shuffle
from random import seed
from random import randint

INT_MIN = 1
INT_MAX = 50000
LEN_TEXT = 247

# helper function
def usage(): 
    print "This program aims at generating a dataset of random value for CS386D Lab 01 and 02." 
    print "Usage: "
    print "    python generator.py [num_rows] [out_file]"

def generate_random_integer(lower=INT_MIN, upper=INT_MAX):
    return randint(lower, upper)

def generate_random_text(length=LEN_TEXT):
    chars = [ chr(randint(1,255)) for i in range(length) ]
    result = "".join(chars)
    result = result.replace("\n", "\r")
    result = result.replace('''"''', "'")
    return result

def quote(word):
    return '''"''' + str(word) + '''"'''

def random_generate(v1fout, v2fout, num_rows):
    theKeys = range(num_rows)
    # use shuffle to simulate sampling without replacement
    shuffle(theKeys)
    v1key = 0
    for v2key in theKeys:
        # generate random values for each columns
        columnA = generate_random_integer()
        columnB = generate_random_integer()
        filler = generate_random_text()
        # generate strings for output
        v1instance = (v1key, columnA, columnB, filler)
        v2instance = (v2key, columnA, columnB, filler)
        v1string = ",".join(quote(val) for val in v1instance)
        v2string = ",".join(quote(val) for val in v2instance)
        # write to out file
        v1fout.write(v1string) 
        v1fout.write("\n")
        v2fout.write(v2string)
        v2fout.write("\n")
        # update v1key
        v1key += 1

# main entrance
if __name__ == "__main__":
    # examine arguments
    nargs = len(sys.argv)
    if nargs != 3:
        usage()
        sys.exit(-1)
    # parse arguments
    num_rows = int(sys.argv[1])
    v1ofname = sys.argv[2] + "v1"
    v2ofname = sys.argv[2] + "v2"
    # generate data of random values and write to <ofname>
    v1fout = open(v1ofname, "w+")
    v2fout = open(v2ofname, "w+")
    seed(1)
    data = random_generate(v1fout, v2fout, num_rows)
    v2fout.close()
    v1fout.close()
