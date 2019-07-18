#!/bin/env python
import MaximumCombination
import json, csv, os, sys
from pprint import pprint


values = {
    "A": ["1", "2"],
    "B": ["X", "Y"],
    "C": ["Yes", "No"]
}

kys = [
    "A.B.C",
    "B",
    "A.C"
]

m = MaximumCombination.MaximumCombination(kys, values)
ky = m.getHash()
js = m.getValueHash()

pprint(ky)
#sys.exit(1)


def pushValues(stairCase, hs ,currentKey , jsBundlle ):
    #print currentKey
    jsBundlle[currentKey]["total"] += 1
    jsBundlle[currentKey][hs[currentKey]]["total"] += 1

    for x in stairCase[currentKey]:
        pushValues(stairCase[currentKey] , hs , x , jsBundlle[currentKey][hs[currentKey]])

    #return jsBundlle

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        #None
        #here row us a dict containing all values
        js["total"] += 1
        for k in ky:
            pushValues(ky,row ,k , js)


pprint(js)

with open("base.json", "w") as f:
    f.write(json.dumps(js))