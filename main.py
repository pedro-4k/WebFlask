contatos = []

while True:
    print("\n=== MENU ===")
    print("1 - Adicionar contato")
    print("2 - Ver contatos")
    print("3 - Editar contato")
    print("4 - Marcar/Desmarcar favorito")
    print("5 - Ver favoritos")
    print("6 - Apagar contato")
    print("7 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        contato = {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "favorito": False
        }
        contatos.append(contato)
        print("Contato adicionado.")
    elif opcao == "2":
        if not contatos:
            print("Nenhum contato.")
        else:
            for i, c in enumerate(contatos):
                fav = "*" if c["favorito"] else ""
                print(f"{i + 1}. {c['nome']} - {c['telefone']} - {c['email']} {fav}")
    elif opcao == "3":
        for i, c in enumerate(contatos):
            print(f"{i + 1}. {c['nome']}")
        idx = int(input("Número do contato para editar: ")) - 1
        if 0 <= idx < len(contatos):
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            email = input("Novo email: ")
            contatos[idx]["nome"] = nome
            contatos[idx]["telefone"] = telefone
            contatos[idx]["email"] = email
            print("Contato atualizado.")
        else:
            print("Contato inválido.")
    elif opcao == "4":
        for i, c in enumerate(contatos):
            print(f"{i + 1}. {c['nome']}")
        idx = int(input("Número do contato: ")) - 1
        if 0 <= idx < len(contatos):
            contatos[idx]["favorito"] = not contatos[idx]["favorito"]
            print("Favorito atualizado.")
        else:
            print("Contato inválido.")
    elif opcao == "5":
        for c in contatos:
            if c["favorito"]:
                print(f"{c['nome']} - {c['telefone']} - {c['email']} *")
    elif opcao == "6":
        for i, c in enumerate(contatos):
            print(f"{i + 1}. {c['nome']}")
        idx = int(input("Número do contato para apagar: ")) - 1
        if 0 <= idx < len(contatos):
            del contatos[idx]
            print("Contato removido.")
        else:
            print("Contato inválido.")
    elif opcao == "7":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
