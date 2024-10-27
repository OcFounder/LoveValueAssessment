# 2024.10.22
from EPV import *


def Assess(a, b, epv):
    small, big = epv.C(b)
    assess = ""
    a = a*100
    txt = {
    1:f"[1] : (VERY GOOD: {a:.32f}%), (S)he is highly likely. \n[（非常好：概率{a:.32f}%），他（她）很有可能喜欢你。]",
    2:f"[2] : GOOD: {a:.32f}% \n[ 好：概率{a:.32f}% ]",
    3:f"[3] : CENTER: {a:.32f}% \n[还行：{a:.32f}%]",
    4:f"[4] : BAD: {a:.32f}% \n[ 不好：{a:.32f}%]",
    5:f"[5] : VERY BAD: {a:.32f}% \n[ 非常不好：{a:.32f}%]",
    6:f"[6] : EHH... : {a:.32f}% \n[一言难尽：{a:.32f}%]",
    7:f"[7] : MAYBE THE NUMBER OF PEOPLE IS SO MUCH: {a:.32f}% \n[ 可能输入的人数有点多：{a:.32f}% ]",
    8:f"[8] : MAYBE THE NUMBER OF PEOPLE IS SO MUCH AND DONT SAD: {a:.32f}% \n[ 不要灰心，也许你输入的人数太多了：{a:.32f}%]",
    9:f"[9] : MAYBE THE NUMBER OF PEOPLE IS VERY MUCH AND DONT SAD: {a:.32f}% \n[ 不要灰心，也许你的范围太大了：{a:.32f}%]"
    }
    if a >= 25:
        assess = 1
    elif a >= 20:
        assess = 2
    elif a >= 10:
        assess = 3
    elif a >= 5:
        assess = 4
    elif a >= 3:
        assess = 5
    elif a >= 1:
        assess = 6
    elif a >= 0.5:
        assess = 7
    elif a >= 0.1:
        assess = 8
    else:
        assess = 9

    if a < small and assess != 9:
        assess += 1
    if a > big and assess != 1:
        assess -= 1

    return txt[assess]


# start
def start():
    try:
        BoyNumber = int(input("Number of boys [输入男生人数]: "))
        GirlNumber = int(input("Number of girls [输入女生人数]: "))
    except Exception as e:
        print(f"Error: {e}")
    print("\n\t*************CALCULAT 计算*************")

    #EPV
    epv = EPV(BoyNumber,GirlNumber)
    epvA = epv.A()
    epvB = epv.B()

    print("\n\t*************RESULT 结果***************")
    print(Assess(epvA, epvB, epv))
    input("\n\n[Enter] to exit. \n{ 按下[Enter]退出。}")
