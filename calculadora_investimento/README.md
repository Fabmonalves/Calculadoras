# [calculadora Investimento](https://github.com/Fabmonalves/Calculadoras/tree/main/tibia)
## 🙋‍♂️ Olá, Neste topico temos os programas de calculos que podem ser uteis para jogadores do Tibia, podemos calcular os valores e converter para Reias, muito útil para jogadores, visto que a moeda TibiaCoins é negociavel, podendo converter para Reais 💸💲

##### segue abaixo a explicação de cada função feita e com os codigos para entender como funciona



## [Funções do codigo](https://github.com/Fabmonalves/Calculadoras/blob/main/tibia/modulos/format_valores/__init__.py) (Atalho direto para o documento)


-----------------------------------------------------------------------------------------------------

#### `format_real`: recebe 1 parametro `int/float`, formata o valor inserido em formato Real (BR)
    def format_real(valor):
      """Função para converter os valores no formato Real-BR (R$)

      Returns:
          float: retorna o valor formatado para formatação em Reais
      """

      real_format_ = f"{float(valor):_.2f}".replace(".",",").replace("_",".")
      return real_format_

![image](https://user-images.githubusercontent.com/86204984/222605789-fe3ea730-8f20-4615-864d-61b21d1540f4.png)

-----------------------------------------------------------------------------------------------------

#### `tratamento_value`: recebe 1 parametro `int/float`, essa função serve como um tratamento de erro, é o que valida o valor inserido pelo usuario, se o mesmo inserir uma `str`por exemplo, essa função retorna com uam mensagem alertando e pede para que o usuário retorne com os tipos corretos, que no casso são tipos `int/float`
    def values_(msg):
    """Tratamento de erro, usado para input, para garantir que o usuário nos passe os dados corretos, nesse caso deve ser usar um valor do tipo int/float

    Args:
        msg (int/float): usar apenas valores int/float, substituindo a ',' por '.'

    Returns:
        float: valor será retornado um float, caso o usuario use outro tipo de dados dara um erro e voltara para inserir os dados novamente
    """
    
     
    while True:
        try:
            num = float(input(msg))
            break
        except:
            print('por favor, me informe um valor valido, valor tipo "int | float", substitua a ","(virgula) por "."(porntos)')
    return num

![image](https://user-images.githubusercontent.com/86204984/222605755-95105676-d549-4d8a-bfd4-999fdc8f1012.png)

-----------------------------------------------------------------------------------------------------

#### `lines_`: Função serve apenas para pular linhas 
    def lines_():
        """comando para pular linha apenas, para deixar o codigo mais limpo
        """

        print("-=-"*20)

![def_lines_](https://user-images.githubusercontent.com/86204984/222589910-1047993d-209f-42d6-8367-90aa517167a7.jpg)

-----------------------------------------------------------------------------------------------------

### [O Codigo](https://github.com/Fabmonalves/Calculadoras/blob/main/calculadora_investimento/investimento.py) (Atalho direto para o codigo) 

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

![image](https://user-images.githubusercontent.com/86204984/222606184-a2da3809-1ee3-4f04-b8c2-eea290dcc770.png)


## Resultado do programa acima:

![image](https://user-images.githubusercontent.com/86204984/222606274-7cfd6d27-ba7f-482e-8e3b-1c6cd1a0a1f9.png)
