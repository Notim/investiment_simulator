import matplotlib.pyplot as plt
import numpy as np

def calcular_investimento(periodo_meses, rendimento_anual, valor_inicial, aporte_mensal, inflacao_anual):
    rendimento_mensal = rendimento_anual / 12
    inflacao_mensal = inflacao_anual / 12

    valores_totais = []
    valores_aportes = []
    
    valor_total = valor_inicial
    aporte_mensal_inflacionado = aporte_mensal

    for mes in range(1, periodo_meses + 1):
        juros_mes = valor_total * rendimento_mensal
        
        valores_totais.append(valor_total)
        valores_aportes.append(aporte_mensal_inflacionado)
        
        printar_valores(mes, inflacao_mensal, rendimento_mensal, valor_total, juros_mes, aporte_mensal_inflacionado)
    
        valor_total += juros_mes + aporte_mensal_inflacionado
        aporte_mensal_inflacionado += (aporte_mensal_inflacionado * inflacao_mensal)
        

    return valores_totais, valores_aportes


def printar_valores(mes, inflacao_mensal, rendimento_mensal, valor_total, juros_mes, aporte_mensal_inflacionado):
    print("mes"+ str(mes) + "\t" + format((inflacao_mensal*100), ".2f") + "%" + "\t" + format((rendimento_mensal*100), ".2f") + "%" + "\t" + "R$" + format(valor_total, ".2f") + "\t" + "R$" + format(juros_mes, ".2f") + "\t" + "R$" + format(aporte_mensal_inflacionado, ".2f"))

# Inputs do usuário
periodo_meses = int(input("Digite o período em meses: "))
rendimento_anual = float(input("Digite o rendimento anual em decimal (0.10 -> 10%): "))
valor_inicial = float(input("Digite o valor inicial: "))
aporte_mensal = float(input("Digite o valor de aporte mensal: "))
inflacao_media_ano = float(input("Digite o valor da media de inflação ano em %: "))

# Calculando o investimento
valores_totais, valores_aportes = calcular_investimento(periodo_meses, rendimento_anual, valor_inicial, aporte_mensal, inflacao_media_ano)

# Plotando o gráfico de barras
meses = np.arange(1, periodo_meses + 1)
largura_barra = 0.35  # Largura das barras

fig, ax = plt.subplots(figsize=(12, 6))
barras_aportes = ax.bar(meses - largura_barra/2, valores_aportes, largura_barra, label='Aportes Mensais')
barras_totais = ax.bar(meses + largura_barra/2, valores_totais, largura_barra, label='Total Acumulado')

ax.set_xlabel('Meses')
ax.set_ylabel('Valor (R$)')
ax.set_title('Evolução do Investimento com Juros Compostos e Inflação')
ax.set_xticks(np.arange(0, periodo_meses + 1, 12))
ax.legend()

plt.grid(True)
plt.show()
