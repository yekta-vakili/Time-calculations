print("Please select the desired operation:")
print("1-Addition of two times\n2-Subtraction of two times\n3-Convert seconds to time\n4-Convert time to seconds")
select = int(input())


class Time_calculations:
    def __init__(self):
        print("**The first time**")
        self.hour1 = int(input("Please enter the desired time:\n"))
        self.minutes1 = int(input("Please enter the desired minute:\n"))
        self.second1 = int(input("Please enter the desired seconds:\n"))
        print("**The second time**")
        self.hour2 = int(input("Please enter the desired time:\n"))
        self.minutes2 = int(input("Please enter the desired minute:\n"))
        self.second2 = int(input("Please enter the desired seconds:\n"))

    def su_m(self):
        a = self.second1+self.second2
        b = self.minutes1+self.minutes2
        c = self.hour1+self.hour2
        if a >= 60:
            a1 = int(a/60)
            b2 = b+a1
            f1 = a % 60
            if b2 >= 60:
                b3 = int(b2/60)
                c2 = c+b3
                f2 = b2 % 60
                print(c2, ":", f2, ":", f1)
            else:
                print(c, ":", b2, ":", f1)
        elif b >= 60:
            r1 = int(b/60)
            r2 = c+r1
            r3 = b % 60
            print(r2, ":", r3, ":", a)
        else:
            print(c, ":", b, ":", a)

    def sub(self):
        if self.second1 < self.second2:
            q1 = self.minutes1-1
            q2 = self.second1+60
            w3 = q2-self.second2
            w2 = q1-self.minutes2
            w1 = self.hour1-self.hour2
            if q1 < self.minutes2:
                q3 = self.hour1-1
                q4 = q1+60
                w2 = q4-self.minutes2
                w1 = q3-self.hour2
                print(w1, ":", w2, ":", w3)
            else:
                print(w1, ":", w2, ":", w3)

        elif self.minutes1 < self.minutes2:
            q5 = self.hour1-1
            q6 = self.minutes1+60
            w2 = q6-self.minutes2
            w1 = q5-self.hour2
            w3 = self.second1-self.second2
            print(w1, ":", w2, ":", w3)
        else:
            w3 = self.second1-self.second2
            w2 = self.minutes1-self.minutes2
            w1 = self.hour1-self.hour2
            print(w1, ":", w2, ":", w3)


class Time_conversion:
    def __init__(self):
        self.second = int(input("Please enter the desired seconds:\n"))

    def se_ho(self):
        out = self.second / 3600
        print("**Convert seconds to hours:**\n", out)


class Time_conversion2:
    def __init__(self):
        self.hour = float(input("Please enter the desired time:\n"))

    def ho_se(self):
        out = self.hour * 3600
        print("**Convert hours to seconds:**\n", out)


if select == 1:
    summ = Time_calculations()
    summ.su_m()
if select == 2:
    subb = Time_calculations()
    subb.sub()
if select == 3:
    seho = Time_conversion()
    seho.se_ho()
if select == 4:
    hose = Time_conversion2()
    hose.ho_se()
