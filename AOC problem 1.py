import math

def calc(mass):
        module = math.floor(int(mass)//3) -2
        return module

def recurCalc(mass):
        if calc(mass) <= 0:
                return 0
        elif calc(mass) == 2:
                return 2
        else:
                return calc(mass)+ recurCalc(calc(mass))
p= """95065
129298
145573
95743
59139
78323
124445
69015
81990
83254
139274
92101
74245
104038
61955
80642
110376
89992
84392
117830
140144
80076
111285
107135
98741
103753
141922
130503
60409
73891
84781
118319
93610
143228
99616
65353
102388
123813
88335
95459
133635
108771
101999
73850
106490
53396
110330
140258
73958
60273
101401
128995
61495
114674
71955
107049
79374
52359
107925
91789
69174
133966
85063
62856
96965
97100
81638
104488
131368
59015
149357
65193
61489
126089
141224
100596
93144
109421
121988
135890
70141
53531
59900
98981
66796
113700
109535
100721
87240
99883
81637
80064
143154
75778
64835
59235
103907
121637
118525
125730"""

o = p.split()

val=0
for i in o:
    val += recurCalc(i)


print(val)
    
