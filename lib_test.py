import sys

import own_lib as ol

if len(sys.argv) != 2:
    sys.exit("Enter argument")

ol.hello(sys.argv[1])

ol.goodbye(sys.argv[1])