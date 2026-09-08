# Calculadora de consumo elétrico

aparelho = input("Digite o nome do aparelho: ")

potencia = float(input("Digite a potência do aparelho em Watts: "))

horas_de_uso = float(input("Digite o tempo de uso diário em horas: "))

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_de_uso * 30) / 1000

# Cálculo do custo
valor_kwh = 0.75
custo_mensal = consumo_mensal * valor_kwh

# Exibição dos resultados
print(f"\nAparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_mensal:.2f}/mês")