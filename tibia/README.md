# Calculadoras
## Neste topico temos os programas de calculos que podem ser uteis para jogadores do Tibia, podemos calcular os valores e converter para Reias, muito útil para jogadores, visto que a moeda TibiaCoins é negociavel, podendo converter para Reais 💸💲

##### segue abaixo a explicação de cada função feita e com os codigos para entender como funciona



## Funções do codigo

#### `format_tc`: recebe 1 parametro `int/float`, formata o valor inserido em formato tibiano (Gold/TCs)
    def format_tc(valor):
      """Função para converter os valores no formato das TCs do Tibia

      Returns:
          float: retorna o valor formatado para formatação tibiana em TCs/Gold
      """

      tc_format_ = f"{float(valor):_.0f}".replace("_",".")
      return tc_format_
    
<center> ![def_format_tc](https://user-images.githubusercontent.com/86204984/222589871-2ae9ea1f-75a8-4259-b08a-dd477e986060.jpg) </center>

-----------------------------------------------------------------------------------------------------

#### `format_real`: recebe 1 parametro `int/float`, formata o valor inserido em formato Real (BR)
    def format_real(valor):
      """Função para converter os valores no formato Real-BR (R$)

      Returns:
          float: retorna o valor formatado para formatação em Reais
      """

      real_format_ = f"{float(valor):,.2f}".replace(".",",").replace("_",".")
      return real_format_

![def_format_real](https://user-images.githubusercontent.com/86204984/222589882-4395febf-ff32-41ee-8c14-05f3b0554278.jpg)

-----------------------------------------------------------------------------------------------------

#### `values_`: recebe 1 parametro `int/float`, essa função serve como um tratamento de erro, é o que valida o valor inserido pelo usuario, se o mesmo inserir uma `str`por exemplo, essa função retorna com uam mensagem alertando e pede para que o usuário retorne com os tipos corretos, que no casso são tipos `int/float`
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
            print("Por favor, digite apenas valores númericos, para números Reais deve-se substituir a virgula(',') por pontos('.')")
    return num

![def_values_](https://user-images.githubusercontent.com/86204984/222589904-0e84ad7d-f85f-46d5-bc40-e94793557e41.jpg)

-----------------------------------------------------------------------------------------------------

#### `lines_`: Função serve apenas para pular linhas 
    def lines_():
        """comando para pular linha apenas, para deixar o codigo mais limpo
        """

        print("-=-"*20)

![def_lines_](https://user-images.githubusercontent.com/86204984/222589910-1047993d-209f-42d6-8367-90aa517167a7.jpg)

-----------------------------------------------------------------------------------------------------

## Resultado do programa acima:

![image](https://user-images.githubusercontent.com/86204984/222593706-76248b21-6713-4f7d-aa50-46418c239eac.png)

-----------------------------------------------------------------------------------------------------
### Calculadora de Shared




