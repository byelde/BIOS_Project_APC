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
	advanced = open('advanced.txt', "r")
	line = advanced.readline()
	return line
	if line == 'True\n':
		return True
	elif line == 'False\n':
		return False
	# dica: utilize a instrução with
		# dentro do bloco with leia UMA linha do arquivo
		# salve o conteúdo desta linha em uma variável
		# SE o valor da variável corresponder a 'False\n'
			# retorne False
		# SE o valor da variável corresponder a 'True\n'
			# retorne True


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
	advanced_file = open('advanced.txt',"w")
	if senha == '':
		advanced_file.write('False\n')
	else:
		advanced_file.write(f'True\n{senha}')

	# abra o arquivo "advanced.txt" para escrita
	# dica: utilize a instrução with
		# SE o valor da variável senha for vazio
			# escreva "False\n"
			# escreva o conteúdo da variável senha
		# SE o valor da variável senha NÃO for vazio
			# escreva "True\n"
			# escreva o conteúdo da variável senha

# print(get_usar_senha())
set_usar_senha('1234')