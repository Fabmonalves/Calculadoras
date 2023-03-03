

from modulos.format_valores import lines_

my_level = int(input("Seu level: "))
shared_min = (my_level / 3) * 2
shared_max = (my_level / 2) * 3



print(f"Level minimo para sharear: \n{shared_min:.0f}" )
lines_()
print(f"Level maximo para sharear: \n{shared_max:.0f}" )