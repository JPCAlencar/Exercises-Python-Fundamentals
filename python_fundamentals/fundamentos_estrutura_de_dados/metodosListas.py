lista = []

lista.append(1)
lista.append("python")
lista.append([40,30,20])
print(lista)

lista= [1, "Python", [40,30,20]]
print(lista)
lista.clear()
print(lista)

lista= [1, "Python", [40,30,20]]
l2 = lista.copy()
print(lista)

cores = ["vermelho", "azul", "verde", "azul"]

contagem_cores = {
    "vermelho": cores.count("vermelho"),
    "azul": cores.count("azul"),
    "verde": cores.count("verde")
}

print(contagem_cores)

linguagens = ['python', 'js', 'c']
print(linguagens)
linguagens.extend(["java", "csharp"])
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'csharp']


print(linguagens.index("java"))
print(linguagens.index("python"))


linguagens = ['python', 'js', 'c', 'java', 'csharp']

linguagens.pop()
linguagens.pop()
linguagens.pop()
linguagens.pop(0)

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.remove("c")
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.reverse()
print(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort()

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(reverse =True)

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(key=lambda x: len(x))

linguagens = ['python', 'js', 'c', 'java', 'csharp']
linguagens.sort(key=lambda x: len(x), reverse=True)

linguagens = ['python', 'js', 'c', 'java', 'csharp']

len(linguagens)

linguagens = ['python', 'js', 'c', 'java', 'csharp']

sorted(linguagens, key=lambda x: len(x))
sorted(linguagens, key=lambda x: len(x), reverse=True)



