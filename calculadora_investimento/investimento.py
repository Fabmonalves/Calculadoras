from modulos import tratamento_value, format_real, lines_
    
tx_selic = tratamento_value('Digite o valor da TX Selic ao ano: ')
valor_investido = tratamento_value("Digite o valor que deseja investir: ")

vai_reenvestir = input("Vai reenvestir todo mes com um valor? [S]im/[N]ão: ").upper()[0]

if vai_reenvestir == "S":
    valor_reenvestido = tratamento_value("Digite o valor investido todo o mês: ")
    valor_investido += valor_reenvestido

prazo_ano = int(tratamento_value("Quantos anos deseja deixar esse dinheiro investido? "))
dia_investimento = int(prazo_ano * 365)
tx_selic_dia = (tx_selic / 365)
valor_dia_investido_total = 0
valor_dia_lucro = 0
valor_juros = 0
valor_control = 0
valor_reenvestido_mes = 0
valor_mes = 0
for valor in range(dia_investimento):
    valor_dia_lucro += (((valor_investido + valor_reenvestido_mes) * (tx_selic_dia)) / 100) 
    valor_juros += (valor_investido * tx_selic_dia) / 100    
    valor_control += 1
    if vai_reenvestir == "S" and valor_control >= (365 / 12):
        valor_reenvestido_mes += valor_reenvestido
        valor_mes += valor_reenvestido
        valor_control = 0
        
valor_dia_investido_total = valor_dia_lucro + valor_investido + valor_mes

lines_()
print(f"O valor acumulado em Juros é R$ {format_real(valor_dia_lucro)}")
lines_()
print(f"Investido todo mês R$ {format_real(valor_mes)}")
lines_()
print(f"Valor acumulado total é R$ {format_real(valor_dia_investido_total)} em {prazo_ano} anos")
lines_()
print('Simulação feira sem considerar o IR ********')
lines_()
    
    
