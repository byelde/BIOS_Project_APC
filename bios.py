'''
Neste arquivo são definidas 
'''
# imports
import os
import sys
import platform
import psutil

from datetime import date
from pynput import keyboard
from colored import fore, back, Style

from advanced import get_usar_senha
from advanced import set_usar_senha

from boot import get_disp1
from boot import get_disp2
from boot import get_disp3
from boot import save_boot

# ====================================================
# variaveis globais (terão valores alterados)
# ====================================================
# elementos de tela
menu_ativo = 0
enter      = 0
item_tela  = 0

# dispositivos de boot
disp1 = get_disp1()
disp2 = get_disp2()
disp3 = get_disp3()

# ====================================================
# constantes globais (não serão alteradas)
# ====================================================
# representam as cores que serão utilizadas ao longo do projeto
color: str = f"{fore('black')}{back('cyan')}"
color_ativo: str = f"{fore('red')}{back('black')}"
color_inativo: str = f"{fore('light_gray')}{back('blue')}"
color_selecionado: str = f"{fore('blue')}{back('light_gray')}"
color_editavel: str = f"{fore('white')}{back('black')}"
color_movendo: str = f"{fore('blue')}{back('black')}"	
color_tela: str = f"{fore('black')}{back('light_gray')}"

# ====================================================
# funcoes
# ====================================================
def limpar_tela() :
	'''
	Deve limpar a tela
	'''
	os.system('cls')


def end():
	'''
	Deve resetar o estilo padrao do terminal, se essa funcção não for 
	executada o terminal permanecerá colorido após finalizar a aplicação
	'''
	print(f'{Style.reset}')


def atualizar() :
	'''
	A tela será redesenhada constantemente, essa função deve executar 
	um conjunto de ações
	'''
	limpar_tela()
	tela()
	end()


def titulo() :
	'''
	Exibe uma barra de titulo incial
	'''
	print(f'{color}{"Projeto Bios":^80}{Style.reset}')


def menu() :
	'''
	Exibe uma barra de menu
	'''
	print(f'{color_inativo}{"":^80}{Style.reset}')
	main_menu()
	advanced_menu()
	boot_menu()
	exit_menu()


def main_menu() :
	'''
	Exibe o menu main selecionado ou inativo
	'''
	# pass
	sys.stdout.write(f'\x1b[{2};{2}H')
	if menu_ativo == 0:
		print(f'{color_selecionado}{"Main":^12}{Style.reset}')
	else:
		print(f'{color_inativo}{"Main":^12}{Style.reset}')


def advanced_menu() :
	'''
	Exibe o menu advanced selecionado ou inativo
	'''
	sys.stdout.write(f'\x1b[{2};{12}H')
	if menu_ativo == 1:
		print(f'{color_selecionado}{"Advanced":^12}{Style.reset}')
	else:
		print(f'{color_inativo}{"Advanced":^12}{Style.reset}')


def boot_menu():
	'''
	Exibe o menu boot selecionado ou inativo
	'''
	sys.stdout.write(f'\x1b[{2};{22}H')
	if menu_ativo == 2:
		print(f'{color_selecionado}{"Boot":^12}{Style.reset}')
	else:
		print(f'{color_inativo}{"Boot":^12}{Style.reset}')


def exit_menu() :
	'''
	Exibe o menu exit selecionado ou inativo
	'''
	sys.stdout.write(f'\x1b[{2};{32}H')
	if menu_ativo == 3:
		print(f'{color_selecionado}{"Exit":^12}{Style.reset}')
	else:
		print(f'{color_inativo}{"Exit":^12}{Style.reset}')


def rodape() :
	'''
	Exibe o conteúdo do rodape, exibindo a lista de comandos
	'''
	sys.stdout.write(f'\x1b[{22};{0}H')
	print(f'{color_inativo}', end='')
	print('{0:80}'.format('Enter: Selecionar menu   \u2191 \u2193: Alterar valores   \u2190\u2192: Navegar menus'))
	print(f'{"+ -: Alterar valores   q: Sair":80}{Style.reset}')


def tela() :
	'''
	Desenha a tela realizando uma chamada para todas as outras funcoes
	'''
	titulo()
	menu()

	if menu_ativo == 0:
		main_tela()
	elif menu_ativo == 1:
		advanced_tela()
	elif menu_ativo == 2:
		boot_tela()
	elif menu_ativo == 3:
		mexit_tela()
	
	rodape()

def main_tela() :
	'''
	Exibe o conteúdo da tela main, quando selecionada
	'''
	for c in range(20):
		print(f'{color_tela}{"":^80}{Style.reset}')
	
	sys.stdout.write(f'\x1b[{5};{5}H')
	today = date.today()
	today = today.strftime("%d/%m/%Y")
	print(f'{color_tela}{today}{Style.reset}')
	
	sys.stdout.write(f'\x1b[{8};{0}H')
	print(f"{color_tela}{'Computer network name: '}{platform.node()}{Style.reset}")
	print(f"{color_tela}{'Machine type: '}{platform.machine()}{Style.reset}")
	print(f"{color_tela}{'Processor type: '}{platform.processor()}{Style.reset}")
	print(f"{color_tela}{'Operating System: '}{platform.system()}{Style.reset}")
	print(f"{color_tela}{'Operating system release: '}{platform.release()}{Style.reset}")
	print(f"{color_tela}{'Operating system version: '}{platform.version()}{Style.reset}")
	print(f"{color_tela}{'Memória RAM instalada: '}{round((psutil.virtual_memory().total)/(1000000000),1)}{'GB'}{Style.reset}")


def advanced_tela() :
	'''
	Exibe o conteúdo da tela advanced, quando selecionada
	Obs.: O valor da senha não é verdadeiramente editável, está com
	um valor padrão 1234
	'''
	password_on = get_usar_senha()
	
	for c in range(20):
		print(f'{color_tela}{"":^80}{Style.reset}')
	
	sys.stdout.write(f'\x1b[{8};{0}H')

	if menu_ativo != 1:
		if password_on == False:
			print(f'{color_tela}{"Usar senha "}{color_ativo}{"Off"}{Style.reset}')
			print(f'{color_tela}{"Senha "}{color_editavel}{"    "}{Style.reset}')
		elif password_on == True:
			print(f'{color_tela}{"Usar senha "}{color_ativo}{"On"}{Style.reset}')
			print(f'{color_tela}{"Senha "}{color_editavel}{"    "}{Style.reset}')

	elif menu_ativo == 1:
		if item_tela == 0:
			if password_on == False:
				print(f'{color_tela}{"Usar senha "}{color_ativo}{"Off"}{Style.reset}')
				print(f'{color_tela}{"Senha "}{color_editavel}{"    "}{Style.reset}')
			elif password_on == True:
				print(f'{color_tela}{"Usar senha "}{color_ativo}{"On"}{Style.reset}')
				print(f'{color_tela}{"Senha "}{color_editavel}{"1234"}{Style.reset}')
		elif item_tela == 1:
			if password_on == False:
				print(f'{color_tela}{"Usar senha "}{color_ativo}{"Off"}{Style.reset}')
				print(f'{color_tela}{"Senha "}{color_movendo}{"    "}{Style.reset}')
			elif password_on == True:
				print(f'{color_tela}{"Usar senha "}{color_ativo}{"On"}{Style.reset}')
				print(f'{color_tela}{"Senha "}{color_movendo}{"1234"}{Style.reset}')

def boot_tela() :
	'''
	Exibe o conteúdo da tela boot, quando selecionada
	'''
	for c in range(20):
		print(f'{color_tela}{"":^80}{Style.reset}')
	
	sys.stdout.write(f'\x1b[{8};{0}H')

	if menu_ativo != 2:
		print(f'{color_tela}{"1° dispositivo de boot: "}{color_editavel}{disp1}{Style.reset}')
		print(f'{color_tela}{"2° dispositivo de boot: "}{color_editavel}{disp2}{Style.reset}')
		print(f'{color_tela}{"3° dispositivo de boot: "}{color_editavel}{disp3}{Style.reset}')
	elif menu_ativo == 2:
		if item_tela == 0:
			print(f'{color_tela}{"1° dispositivo de boot: "}{color_movendo}{disp1}{Style.reset}')
		if item_tela != 0:
			print(f'{color_tela}{"1° dispositivo de boot: "}{color_editavel}{disp1}{Style.reset}')

		if item_tela == 1:
			print(f'{color_tela}{"2° dispositivo de boot: "}{color_movendo}{disp2}{Style.reset}')
		if item_tela != 1:
			print(f'{color_tela}{"2° dispositivo de boot: "}{color_editavel}{disp2}{Style.reset}')

		if item_tela == 2:
			print(f'{color_tela}{"3° dispositivo de boot: "}{color_movendo}{disp3}{Style.reset}')
		if item_tela != 2:
			print(f'{color_tela}{"3° dispositivo de boot: "}{color_editavel}{disp3}{Style.reset}')

def mexit_tela() :
	'''
	Exibe o conteúdo da tela mexit_tela, quando selecionada
	'''	
	for c in range(20):
		print(f'{color_tela}{"":^80}{Style.reset}')
	
	sys.stdout.write(f'\x1b[{8};{0}H')
	print(f'{color_tela}{"Pressione ENTER para sair!"}  {Style.reset}')


# ====================================================
# eventos	
# ====================================================
def on_press(key):
	'''
	Trata todos os eventos de teclado no programa
	'''
	global menu_ativo
	global enter
	global item_tela
	global disp1
	global disp2
	global disp3

	try:
		'''
		Quando o caractere q é presionado, sai do programa
		'''
		if (key.char == 'q') :
			sys.exit()

		if (key.char == '+'):
			if menu_ativo == 1:
				set_usar_senha('1234')
			if menu_ativo == 2:
				if item_tela == 0:
					disp1, disp2 = disp2, disp1
				elif item_tela == 1:
					disp2, disp3 = disp3, disp2
				elif item_tela == 2:
					disp1, disp3 = disp3, disp1
				save_boot(disp1, disp2, disp3)

		elif (key.char == '-'):
			if menu_ativo == 1:
				set_usar_senha('')
			if menu_ativo == 2:
				if item_tela == 0:
					disp1, disp3 = disp3, disp1
					
				elif item_tela == 1:
					disp1, disp2 = disp2, disp1

				elif item_tela == 2:

					disp2, disp3 = disp3, disp2
					
				save_boot(disp1, disp2, disp3)
			
		else :
			pass
	except AttributeError:
		# para indicar quantos itens são editáveis em cada tela
		###########################################
		# não precisa alterar as linhas a seguir
		mod = 1
		if (enter == 0) :
			mod = 1	
		elif (enter == 1) :
			mod = 2
		elif (enter == 2) :
			mod = 3	
		# não precisa alterar as linhas anteriores
		###########################################
		
		if (key == keyboard.Key.up): 
			if menu_ativo == 1:
				item_tela = (item_tela - 1)%2
			elif menu_ativo == 2:
				item_tela = (item_tela - 1)%4

		elif (key == keyboard.Key.down): 
			if menu_ativo == 1:
				item_tela = (item_tela + 1)%2
			elif menu_ativo == 2:
				item_tela = (item_tela +
				 1)%4

		elif (key == keyboard.Key.left):
			menu_ativo = (menu_ativo - 1)%4
			item_tela = 0

		elif (key == keyboard.Key.right):
			menu_ativo = (menu_ativo + 1)%4
			item_tela = 0

		elif (menu_ativo == 3) and (key == keyboard.Key.enter):
			sys.exit()
		elif (key == keyboard.Key.enter):
			enter     = menu_ativo
			item_tela = 0

			if (menu_ativo == 2) :
				save_boot(disp1, disp2, disp3)
	atualizar()

def on_release(key):
	'''
	Finaliza o programa ao pressionar ESC
	Obs.: Não é necesário modificar
	'''
	if key == keyboard.Key.esc:
		return False


# main
####################################################
# Chegou aqui, retire os comentários e execute
####################################################

try:
	limpar_tela()
	tela()
	input()
	end()

	# Collect events until released
	with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
		listener.join()

except :
	limpar_tela()
	print("BIOS finalizada!")
