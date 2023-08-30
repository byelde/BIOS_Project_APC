'''
Neste arquivo devem ser implementadas funcoes para facilitar a execução
de ações necessarias no bios.py
'''
def get_disp1() :
	'''
	Essa função deve ler o arquivo boot.txt e retornar o dispositivo 
	indicado na primeira linha, sem o caractere especial \n
	Exemplo de retorno 'SSD/HDD'
	'''
	# pass
	get_disp1_file = open('boot.txt', 'r')
	# abra o arquivo "boot.txt" para leitura
	with get_disp1_file:
		disp1 = get_disp1_file.readlines()
		return disp1[0]

	# dica: utilize a instrução with
		# dentro do bloco with leia UMA linha do arquivo
		# e substitua o caractere especial '\n' por vazio ''
		# esse conteúdo deve ser salvo em uma variável ex. disp1
	# fora da instrução with, retorne o conteúdo da variável 'disp1'


def get_disp2() :
	'''
	Essa função deve ler o arquivo boot.txt e retornar o dispositivo 
	indicado na segunda linha, sem o caractere especial \n
	Exemplo de retorno 'DVD-ROM'
	'''
	get_disp2_file = open('boot.txt', 'r')
	with get_disp2_file:
		disp2 = get_disp2_file.readlines()
		return disp2[1]
	# abra o arquivo "boot.txt" para leitura
	# dica: utilize a instrução with
		# dentro do bloco with leia UMA linha do arquivo
		# essa linha será ignorada
		# leia a segunda linha do arquivo
		# e substitua o caractere especial '\n' por vazio ''
		# esse conteúdo deve ser salvo em uma variável ex. disp2
	# fora da instrução with, retorne o conteúdo da variável 'disp2'


def get_disp3() :
	'''
	Essa função deve ler o arquivo boot.txt e retornar o dispositivo 
	indicado na terceira linha, sem o caractere especial \n
	Exemplo de retorno 'LAN'
	'''
	get_disp3_file = open('boot.txt', 'r')
	with get_disp3_file:
		disp3 = get_disp3_file.readlines()
		return disp3[2]
	# abra o arquivo "boot.txt" para leitura
	# dica: utilize a instrução with
		# dentro do bloco with leia UMA linha do arquivo
		# essa linha será ignorada
		# leia a segunda linha do arquivo
		# essa linha será ignorada
		# leia a terceira linha do arquivo
		# e substitua o caractere especial '\n' por vazio ''
		# esse conteúdo deve ser salvo em uma variável ex. disp2
	# fora da instrução with, retorne o conteúdo da variável 'disp2'


def save_boot(disp1, disp2, disp3) :
	'''
	Essa função deve abrir o arquivo boot.txt e criar a lista de 
	dispositivos de boot, um por linha
	Exemplo de conteúdo do arquivos após a execução

	SSD/HDD
	DVD-ROM
	LAN
	'''
	lines = [disp1, disp2, disp3]
	sv_return = ''
	for line in lines:
		sv_return += line
	return sv_return
	# abra o arquivo "boot.txt" para escrita
	# dica: utilize a instrução with
		# dentro do bloco with escreva uma linha com disp1 e \n
		# escreva uma linha com disp2 e \n
		# escreva uma linha com disp3 e \n

print(save_boot(get_disp1(), get_disp2(), get_disp3()))