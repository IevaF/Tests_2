i =  [1, -2, 10]
new_i = [i*2 for i in i if i>0]
print(new_i)


i =  [1, -2, 10]
new_i = [i*2 for i in i]
print(new_i)

i =  [1, -2, 10]
new_i = [i*2 if i > 0 else 0 for i in i]
print(new_i)

x = 5
x = complex(x)
print(x)

txt = "Hello World"
x = (txt[0])
print(x)

    
temps = [221, 334, 556, 842]
new_temps = []
for temp in temps:
    new_temps.append(temp / 10)
        
print(new_temps)

temps = [221, 334, 556, 842]
new_temps = [temp / 10 for temp in temps]

print(new_temps)

