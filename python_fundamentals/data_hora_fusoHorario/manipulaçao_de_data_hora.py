from datetime import timedelta, datetime, date, time


tipo_carro = "P"
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada =  data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimada}")
elif tipo_carro == "M":
    data_estimada =  data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimada}")
else:
    data_estimada =  data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto ás {data_estimada}")

print(date.today() - timedelta(days=1))
#Para manipular data ou hora é sempre necessario usar datetime, se quiser tirar um dos dois, tem q chamar na hora de exibir somente um
resultado = datetime(2024, 11, 15, 10,19,20) - timedelta(hours=1)
#Chama para exibição soemnte a hora
print(resultado.time())

print(resultado.date())
print(datetime.now().date())
