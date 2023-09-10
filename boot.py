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
	get_disp1_file = open('boot.txt', 'r')
	with get_disp1_file:
		disp1 = get_disp1_file.readlines()
		return disp1[0]


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


print(save_boot(get_disp1(), get_disp2(), get_disp3()))