from colored import fore, back, Style
import sys
import psutil

color: str = f"{fore('black')}{back('cyan')}"
color_ativo: str = f"{fore('red')}{back('black')}"
color_inativo: str = f"{fore('light_gray')}{back('blue')}"
color_selecionado: str = f"{fore('blue')}{back('light_gray')}"
color_editavel: str = f"{fore('white')}{back('black')}"
color_movendo: str = f"{fore('blue')}{back('black')}"	
color_tela: str = f"{fore('black')}{back('light_gray')}"

# titulo = '{0:^80}'.format('Projeto Bios')
# print(f'{color}{titulo}{Style.reset}')
# # print(f'{"PROJETO BIOS"}'.center)
menu_ativo = 2

# sys.stdout.write(f'\x1b[{2};{2}H')
# if menu_ativo == 0:
# 	print(f'{color_selecionado}{"Main":^12}{Style.reset}')
# else:
#     print(f'{color_inativo}{"Main":^12}{Style.reset}')
# print(f'{color_inativo}{"":^80}{Style.reset}')

# sys.stdout.write(f'\x1b[{22};{0}H')
# print(f'{color_inativo}', end='')
# print('{0:80}'.format('Enter: Selecionar menu   \u2191 \u2193: Alterar valores   \u2190\u2192: Navegar menus'))
# print(f'{"+ -: Alterar valores   q: Sair":80}{Style.reset}')

# from datetime import date
# today = date.today()
# # dd/mm/YY
# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)

print(f"{color_tela}{'Memória RAM instalada: '}{round((psutil.virtual_memory().total)/(1000000000),1)}{'GB'}{Style.reset}")