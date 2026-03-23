#What is the length of following set s :

s = set()
s.add(20)
s.add(20.0)  #20 == 20.0  Python treats them as same value
s.add('20')
print(len(s))   # 2