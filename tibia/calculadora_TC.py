
    
    
from modulos.format_valores import format_tc, format_real, lines_, values_

gold_hor = values_("Gold por Hora: ")
hor_in_day = values_("Horas farmando por dia: ")
work_days = values_("Por quantos dias: ")
value_tc = values_("Valor da TC no Server: ")

total_in_day = gold_hor * hor_in_day
total_gold = total_in_day * work_days
total_tc = total_gold / value_tc

lines_()
print(f"Farmando {format_tc(total_in_day)} por dia!")
print(f"Seu ouro total será {format_tc(total_gold)}_Gold")
print(f"O valor de tc que vai conseguir com esse valor é {format_tc(total_tc)}_TCs")
lines_()

b_tc = input("Vai transformar essa grana em dinheiro na RL? [S]im or [N]ão: ").upper()[0]
if b_tc == "S":
    value_tc_real = values_("Vai vender por quanto cada 25TC? ")
    real_real = format_real(value_tc_real)

    total_tc_real = (total_tc / 25) * value_tc_real

    lines_()
    print(f"Vai conseguir pegar R${format_real(total_tc_real)} vendendo as {format_tc(total_tc)}_TCs")
