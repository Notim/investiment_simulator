
# Calculadora de Investimento com Juros Compostos e Inflação

Este script calcula a evolução de um investimento ao longo do tempo, considerando juros compostos e inflação. Ele também exibe um gráfico de barras que mostra os aportes mensais e o valor total acumulado.

## Requisitos

- Python 3.x
- Bibliotecas:
  - `matplotlib`
  - `numpy`

Você pode instalar as bibliotecas necessárias usando o pip:

```sh
pip install matplotlib numpy
```

## Como Usar

### Passo 1: Defina os Parâmetros do Investimento

Ao executar o script, você será solicitado a inserir os seguintes parâmetros:

- `periodo_meses`: Período do investimento em meses.
- `rendimento_anual`: Taxa de rendimento anual em decimal (por exemplo, 0.10 para 10%).
- `valor_inicial`: Valor inicial do investimento.
- `aporte_mensal`: Valor do aporte mensal.
- `inflacao_media_ano`: Taxa média de inflação anual em decimal (por exemplo, 0.08 para 8%).

### Passo 2: Execute o Script

Para executar o script, use o comando:

```sh
python nome_do_script.py
```

### Passo 3: Interprete os Resultados

O script irá:

1. Calcular e imprimir uma tabela mostrando a evolução do investimento mês a mês.
2. Exibir um gráfico de barras que mostra:
   - Aportes mensais inflacionados.
   - Valor total acumulado ao longo do tempo.

## Exemplo de Uso

### Defina os Parâmetros no Script

Edite o script conforme necessário para definir os parâmetros de entrada. Exemplo:

```python
# Inputs do usuário
periodo_meses = int(input("Digite o período em meses: "))
rendimento_anual = float(input("Digite o rendimento anual em decimal (0.10 -> 10%): "))
valor_inicial = float(input("Digite o valor inicial: "))
aporte_mensal = float(input("Digite o valor de aporte mensal: "))
inflacao_media_ano = float(input("Digite o valor da media de inflação ano em %: "))
```

### Execute o Script

Execute o script com:

```sh
python nome_do_script.py
```

### Saída Esperada

O script imprimirá uma tabela como esta (apenas alguns meses mostrados para exemplo):

```
mes1     0.67%      1.08%     R$271000.00     R$2920.00     R$2000.00
mes2     0.67%      1.08%     R$274000.00     R$2940.00     R$2030.00
...
```

E exibirá um gráfico de barras mostrando a evolução dos aportes mensais e do valor total acumulado ao longo dos meses.

## Licença

Este projeto não possui uma licença específica e pode ser utilizado livremente.
