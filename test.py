from main import *

wr = open("test_data_2.txt","a")
txt = ""

for i in range(1,50):
    for o in range(1,50):
        txt += f"[{i}, \t{o}, \t{EPV(i,o)*100}%]\n"
        print(i,o)

wr.write(txt)
wr.close()
input()
