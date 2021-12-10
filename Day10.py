data = """151
94
14
118
25
143
33
23
80
95
87
44
150
39
148
51
138
121
70
69
90
155
144
40
77
8
97
45
152
58
65
63
128
101
31
112
140
86
30
55
104
135
115
16
26
60
96
85
84
48
4
131
54
52
139
76
91
46
15
17
37
156
134
98
83
111
72
34
7
108
149
116
32
110
47
157
75
13
10
145
1
127
41
53
2
3
117
71
109
105
64
27
38
59
24
20
124
9
66"""

test = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""


# Part 1
data = test.split("\n")

data = list(map(int, data))
data = sorted(data)

onediffs = 1
threediffs = 1

for adapter in data:

    if data.index(adapter) == 0:
        continue

    elif adapter - data[data.index(adapter) - 1] == 1:
        onediffs += 1
    
    elif adapter - data[data.index(adapter) - 1] == 3:
        threediffs += 1

answer = onediffs * threediffs

# print(answer)

answer = 1

# Part 2
for adapter0 in data:

    if data.index(adapter0) >= 28:
        continue

    possibles = 0
    adapter1 = data[data.index(adapter0) + 1]
    adapter2 = data[data.index(adapter0) + 2]
    adapter3 = data[data.index(adapter0) + 3]

    if adapter0 - adapter1 <= -1 and adapter0 - adapter1 >= -3:
        possibles += 1

    if adapter0 - adapter2 <= -1 and adapter0 - adapter2 >= -3:
        possibles += 1

    if adapter0 - adapter3 <= -1 and adapter0 - adapter3 >= -3:
        possibles += 1

    answer *= possibles

print(answer)