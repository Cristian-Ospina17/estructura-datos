temperatura =[]
for n in range (0,4):
    t = int(input("ingrese la temperatura:"))
    temperatura .append(t)
    print(temperatura)

promedio = sum(temperatura)/ len(temperatura)
print(f"El promedio de todas las temperaturas es:{promedio:.2f}")

if t < 20:
    print("tiene que arreglar el aire, temperatura muy baja ")
elif 20 <= t <= 30:
    print("el aire esta bien")
else:
    print("tiene que arreglar el aire, temperatura muy alta")  
