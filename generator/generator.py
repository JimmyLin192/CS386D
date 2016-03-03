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
    print "    python generator.py [-v1/v2] [num_rows] [out_file]"

def generate_random_integer(lower=INT_MIN, upper=INT_MAX):
    return randint(lower, upper)

def generate_random_text(length=LEN_TEXT):
    result = [ chr(randint(1,255)) for i in range(length) ]
    return "".join(result)

def random_generate(fout, num_rows, mode):
    theKeys = range(num_rows)
    if mode == '-v2': shuffle(theKeys)
    for key in theKeys:
        columnA = generate_random_integer()
        columnB = generate_random_integer()
        filler = generate_random_text()
        instance = "("+str(key)+","+str(columnA)+","+str(columnB)+''',"'''+filler+'''")'''
        fout.write(instance)
        fout.write("\n")

# main entrance
if __name__ == "__main__":
    # examine arguments
    nargs = len(sys.argv)
    if nargs != 4:
        usage()
        sys.exit(-1)
    # parse arguments
    mode = sys.argv[1]
    num_rows = int(sys.argv[2])
    ofname = sys.argv[3]
    # generate data of random values and write to <ofname>
    fout = open(ofname, "w+")
    seed(1)
    data = random_generate(fout, num_rows, mode)
    fout.close()
