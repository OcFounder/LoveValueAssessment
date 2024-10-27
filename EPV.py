

def BdefRange(a, b):
    c = []
    for i in range(a+b):
        c.append(0)
    return c

class EPV:
    def __init__(self, B, G):
        self.boy = B
        self.girl = G
        self.S = 0
        self.Bdef = BdefRange(B, G)

    # Evaluate the probability of victory
    def A(self):
        self.S = ((1/(self.boy+1))*(1/self.girl)*(1/(self.girl+1))*(1/self.boy))
        return self.S


    def B(self):
        for i in range(len(self.Bdef)):
            if i <= self.boy-1:
                self.Bdef[i] = 1/self.girl*100
            else:
                self.Bdef[i] = 1/self.boy*100


        print(self.Bdef)
        for i in range(len(self.Bdef)):
            for o in range(len(self.Bdef)):
                self.Bdef[i] = self.Bdef[o] = (self.Bdef[i] + self.Bdef[o]) / 2
            print(f'A: {(i/len(self.Bdef)):.2f}%')

        print("[")
        for i in range(len(self.Bdef)):
            print(self.Bdef[i])
        print("]")
        print()
        return self.Bdef
    def C(self, a):
        self.a = a

        small = self.a[0]
        big = small
        for i in range(len(self.a)):
            if self.a[i] < small:
                small = self.a[i]
            if self.a[i] > big:
                big > self.a[i]
        return small, big
