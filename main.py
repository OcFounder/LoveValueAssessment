# 2024.10.22
# Evaluate the probability of victory
def EPV(B, G):
    #probability
    S = ((1/(B+1))*(1/G)+(1/(G+1))*(1/B)) / 2 #"/ 2" to get average value
    return S


def Assess(a):
    assess = ""
    a = a*100
    if a >= 25:
        assess = f"[1] : (VERY GOOD: {a}%), (S)he is highly likely. \n[（非常好：概率{a}%），他（她）很有可能喜欢你。]"
    elif a >= 20:
        assess = f"[2] : GOOD: {a}% \n[ 好：概率{a}% ]"
    elif a >= 10:
        assess = f"[3] : CENTER: {a}% \n[还行：{a}%]"
    elif a >= 5:
        assess = f"[4] : BAD: {a}% \n[ 不好：{a}%]"
    elif a >= 3:
        assess = f"[5] : VERY BAD: {a}% \n[ 非常不好：{a}%]"
    elif a >= 1:
        assess = f"[6] : EHH... : {a}% \n[一言难尽：{a}%]"
    elif a >= 0.5:
        assess = f"[7] : MAYBE THE NUMBER OF PEOPLE IS SO MUCH: {a}% \n[ 可能输入的人数有点多：{a}% ]"
    elif a >= 0.1:
        assess = f"[8] : MAYBE THE NUMBER OF PEOPLE IS SO MUCH AND DONT SAD: {a}% \n[ 不要灰心，也许你输入的人数太多了：{a}%]"
    return assess


# start
def start():
    try:
        BoyNumber = int(input("Number of boys [输入男生人数]: "))
        GirlNumber = int(input("Number of girls [输入女生人数]: "))
    except Exception as e:
        print(f"Error: {e}")
    print()
    epv = EPV(BoyNumber,GirlNumber)
    print(Assess(epv))
    input("\n[Enter] to exit. \n{ 按下[Enter]退出。}")
