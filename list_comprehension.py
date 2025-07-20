# podowjenie = [wyrazenie for elementu in typydanych]
# d = [x*2 for x in range(1,11)]
# t = [y*3 for y in range(1,11)]
# s = [z*z for z in range(1,11)]
# print(d)
# print(t)
# print(s)

owoce = ["Banan","Borówka","Truskawki","Mango"]
f = [owoc[0] for owoc in owoce]
o = [(owoce[index]) for index in range(len(owoce))if index == 1]


nums = [1,0,-1,-2,-3,-4]


p = [num for num in nums if num >= 0]
n = [num for num in nums if num < 0]
e = [num for num in nums if num % 2 == 0]


liczby = [1, 2, 3, 4, 5, 6]
filtracja = [num * 2 for num in liczby if num % 2 == 0]

nums = [1, 2, 3, 4, 5]
p = [num**2 for num in nums if not num % 2 == 0 ]
p_sum = sum(p)
print(p_sum)