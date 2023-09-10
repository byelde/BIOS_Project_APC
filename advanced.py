'''
Neste arquivo devem ser implementadas funcoes para facilitar a execução
de ações necessarias no bios.py
'''

def get_usar_senha() :
	'''
	Essa função deve ler o arquivo advanced.txt e retornar 
	'True' se a primeira linha do arquivo contiver 'True'
	'False' se a primeira linha do arquivo contiver 'False'
	'''
	# pass
	with open('advanced.txt', 'r') as arquivo:
		linha = arquivo.readline()
		if linha == 'True\n':
			return True
		else:
			return False


def set_usar_senha(senha="") :
	'''
	Essa função deve escrever no arquivo advanced.txt
	'True\n' se a senha recebida como parametro não for vazia
	'False\n' se a senha recebida como parametro for vazia
	
	Exemplo de conteúdo do arquivo advanced.txt
	
	--------------------
	False
	      (vazio, estará em branco)
	--------------------
	ou
	--------------------
	True
	1234
	--------------------
	'''
	# pass
	with open('advanced.txt', 'w') as arquivo:
		if senha == '':
			arquivo.write('False\n')
			arquivo.write(senha)
		else:
			arquivo.write('True\n')
			arquivo.write(senha) 