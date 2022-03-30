AGENDA = {
    "Leo": {
        "email": "leo@gmail.com",
        "telefone": "12345-6789",
        "endereco": "Rua dos Bobos, 0"
    },  
}

# -------------------------------------

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            print('------------------------')
            buscar_contato(contato)
    else:
        print('')
        print('Agenda vazia!')

# -------------------------------------

def adicionar_contato(nome, email, telefone, endereco):

    AGENDA[nome] = {
    'email': email,
    'telefone': telefone,
    'endereco': endereco
    }
    salvar()

# -------------------------------------

def buscar_contato(contato):
    try:
        print('Nome: '+ contato)
        print('Telefone: ' + AGENDA[contato]['telefone'])
        print('Email: ' + AGENDA[contato]['email'])
        print('Endereço: ' + AGENDA[contato]['endereco'])
    except KeyError:
        print('')
        print('Contato não encontrado!')
    except:
        print('[ERROR] Um erro inesperado ocorreu!')

# -------------------------------------

def remover_contato():
    contato_remover = input('Nome do contato que dejesa excluir: ')
    if contato_remover in AGENDA:
        del AGENDA[contato_remover]
        print("O contato " + contato_remover + " foi excluido com sucesso!")
        salvar()
    else:
        print("")
        print("Contato não encontrado!")

# -------------------------------------

def editar_contato():
    contato_editar = input("Nome do contato que gostaria de editar: ")

    if (contato_editar in AGENDA):
        item_editar = input("Digite [1] Editar nome, [2] Editar telefone, [3] Editar email, [4] Editar endereço: ")

        if (item_editar == "1"):
            print("Esse é o nome que sera alterado - " + AGENDA[contato_editar])
            nome_alterar = input("Qual o novo nome: ")
            AGENDA[contato_editar] = nome_alterar
            print("Nome alterado com sucesso!")
            print("-----------------")
        elif (item_editar == "2"):
            print("Esse é o numero que sera alterado - " + AGENDA[contato_editar]["telefone"])
            telefone_alterar = input("Qual o novo telefone: ")
            AGENDA[contato_editar]["telefone"] = telefone_alterar
            print("Numero alterado com sucesso!")
            print("-----------------")
        elif (item_editar == "3"):
            print("Esse é o email que sera alterado - " + AGENDA[contato_editar]["email"])
            email_alterar = input("Qual o novo email: ")
            AGENDA[contato_editar]["email"] = email_alterar
            print("Email alterado com sucesso!")
            print("-----------------")
        elif (item_editar == "4"):
            print("Esse é o endereço que sera alterado - " + AGENDA[contato_editar]["endereco"])
            endereco_alterar = input("Qual o novo endereco: ")
            AGENDA[contato_editar]["endereco"] = endereco_alterar
            print("Endereço alterado com sucesso!")
            print("-----------------")
        salvar()
    else:
        print("Contato não encontrado!")
        print("-----------------")
    
# -------------------------------------

def exportar_contato(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write("{},{},{},{}\n".format(contato,telefone,email,endereco))
    except Exception as error:
        print("Ocorreu um erro de exportação!")

# -------------------------------------

def salvar():
    exportar_contato('database.csv')

# -------------------------------------

def carregar():
    importar_contatos('database.csv')

# -------------------------------------

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                adicionar_contato(nome,telefone,email,endereco)
    except:
        print("Erro para importar arquivo!")

# -------------------------------------

def exibir_menu():
    print("")
    print("[1] Mostrar todos os contatos.")
    print("[2] Buscar contatos.")
    print("[3] Adicionar contato.")
    print("[4] Excluir contato.")
    print("[5] Editar contato.")
    print("[6] Exportar contatos.")
    print("[7] Importar contatos.")
    print("[0] Sair.")

# -------------------------------------
    
def principal():

    carregar()

    while True:
        exibir_menu()  
        opcao_usuario = input("Digite o numero referente a sua escolha: ")
        
        if (opcao_usuario == "1"):
            print("")
            mostrar_contatos()
        elif (opcao_usuario == "2"):
            print("")
            contato_busca =input("Qual contato deseja buscar: ")
            buscar_contato(contato_busca )
        elif (opcao_usuario == "3"):
            print("")
            nome = input('Nome: ')
            email = input('Email: ')
            telefone = input('Telefone: ')
            endereco = input('Endereço: ')
            adicionar_contato(nome, email, telefone, endereco)
        elif (opcao_usuario == "4"):
            print("")
            remover_contato()
        elif (opcao_usuario == "5"):
            print("")
            editar_contato()
        elif (opcao_usuario == "6"):
            print("")
            nome_do_arquivo = input("Digite o nome do arquivo que deseja exportar: ")
            exportar_contato(nome_do_arquivo)
        elif (opcao_usuario == "7"):
            print("")
            nome_do_arquivo = input("Digite o nome do arquivo que deseja importar: ")
            importar_contatos(nome_do_arquivo )          
        elif (opcao_usuario == "0"):
            print("")
            print("Fechando a agenda!")
            break
        else:
            print("")
            print("Opção invalida! :( ")

# -------------------------------------

principal()