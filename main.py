# 2024.10.22
# Evaluate the probability of victory
def EPV(B, G):
    #probability
    S = ((1/B+1)*(1/G)+(1/G+1)*(1/B)) / 2 #"/ 2" to get average value
    return S


def Assess(a):
    assess = ""
    a = a*100
    if a >= 25:
        assess = f"[1] : (VERY GOOD: {a}%), (S)he is highly likely."
    elif a >= 20:
        assess = f"[2] : GOOD: {a}%"
    elif a >= 10:
        assess = f"[3] : CENTER: {a}%"
    elif a >= 5:
        assess = f"[4] : BAD: {a}%"
    elif a >= 3:
        assess = f"[5] : VERY BAD: {a}%"
    elif a >= 1:
        assess = f"[6] : EHH... : {a}%"
    elif a >= 0.5:
        assess = f"[2] : MAYBE THE NUMBER OF PEOPLE IS SO MUCH: {a}%"
    elif a >= 0.1:
        assess = f"[2] : MAYBE THE NUMBER OF PEOPLE IS SO MUCH AND DONT SAD: {a}%"
    return assess


# start
def start():
    try:
        BoyNumber = int(input("Number of boys: "))
        GirlNumber = int(input("Number of girls: "))
    except Exception as e:
        print(f"Error: {e}")
    epv = EPV(BoyNumber,GirlNumber)
    print(Assess(epv))
    input("[Enter] to exit.")
