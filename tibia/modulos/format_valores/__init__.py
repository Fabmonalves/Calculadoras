def format_tc(valor):
    """Função para converter os valores no formato das TCs do Tibia

    Returns:
        float: retorna o valor formatado para formatação tibiana em TCs/Gold
    """
    
    tc_format_ = f"{float(valor):_.0f}".replace("_",".")
    return tc_format_


def format_real(valor):
    """Função para converter os valores no formato Real-BR (R$)

    Returns:
        float: retorna o valor formatado para formatação em Reais
    """
    
    real_format_ = f"{float(valor):,.2f}".replace(".",",").replace("_",".")
    return real_format_
     
     
     
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



def lines_():
    """comando para pular linha apenas, para deixar o codigo mais limpo
    """
    
    print("-=-"*20)
    