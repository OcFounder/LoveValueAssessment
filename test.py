from main import *
from EPV import *

wr = open("test_data.txt","a")
txt = ""

for i in range(1,500):
    for o in range(1,500):
        epv = EPV(i,o)
        epvA = epv.A()
        txt += f"[{i}, \t{o}, \t{(100*epvA):.16f}%]\n"

wr.write(txt)
wr.close()
input("OK")
