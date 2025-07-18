# vou deixa as global aqui
produtin = {
    "Pão": {"preco": 2.5, "estoque": 50},
    "Leite": {"preco": 4.0, "estoque": 30},
    "Café": {"preco": 10.0, "estoque": 20},
    "Banana": {"preco": 100.0, "estoque": 5}}
saldo = 100 # ver o saldo






#------------------------------------------------

def produtos():

    while True:
        print(produtin)
        nv_produto = input("Adicione o nome do novo produto: ").title()
        produtin[nv_produto] = []
        preco = float(input("Digite o preco do produto: "))
        estoque = int(input("quantos tem em estoque: "))
        produtin[nv_produto] = {"preco": preco, "qnt_no_estoque": estoque}

        produtin[nv_produto] = {
            "preco": preco,
            "estoque": estoque,
        }
        dnv = input("Quer add mais um produto S/N: ").title()
        if dnv == "S":
         continue
        else:
            break
    print(produtin)


def compra_produto():
    global saldo
    while True:
        escolha_para_compra = input(f"Saldo atual: R${saldo:.2f}\n"
                                    f"Vc quer compra alguma coisa S/N: ").title()
        if  escolha_para_compra == "S":
            print(f"Aqui esta os produtos que temos:\n{produtin}")
            escolha_do_produto = input("Qual produto vc quer?").title()
            if escolha_do_produto not in produtin:
                print("Produto não encontrado.")
            elif saldo == 0 or saldo < 0 :
                print("Vc não tem nenhum saldo volte quando depositar mais dinheiro")
                break
            else:
                while True:
                    qntd_prduto = int(input(f"Digite a quantidade da {escolha_do_produto}: "))
                    if qntd_prduto > produtin[escolha_do_produto]["estoque"]:
                        print("Não temos no estoque essa quantidade")
                    else:
                        total = qntd_prduto * produtin[escolha_do_produto]['preco']
                        if saldo >= total:
                            sim_nao = input(f"Vc tem crtz da compra, o total deu  R${total:.2f}  S/N: ").title()
                            if sim_nao == 'S':
                                saldo = saldo - total
                                print(f"Compra feita com sucesso\n"
                                f"Total pago R${total:.2f}\n"
                                f"Saldo atual: R${saldo:.2f}\n")
                                break
                        else:
                            print(f"O total foi: R${total:.2f} e vc so tem R${saldo:.2f}\n"
                                f"Deposite Mais saldo ou pegue pouca coisa ai  ")
                            break
        else:
            break


def saldo_saque ():
    global saldo
    while True:
        print(f"Saldo atual: R${saldo:.2f}")
        escolhaaa = int(input("1 - Colocar Saldo\n"
                        "2 - Retirar Saldo\n"
                        "3 - Voltar\n"
                        "Digite aqui: "))
        match escolhaaa:
            case 1:

                qnt = float(input("Quanto vc quer colocar de saldo: "))

                saldo = qnt + saldo
            case 2:
                while True:
                    retirar = float(input("Quanto vc quer sacar: "))

                    if retirar <= saldo:
                        saldo = saldo - retirar
                        print(f"Saque feito com sucesso agr vc so tem R$ {saldo:.2f}")
                        break
                    else:
                        print(f"N tem isso para sacar nao vc so tem R${saldo:.2f} ")
                        continue
            case 3:
                break


def deleta_produto():
    print(produtin)
    remover = input("\nDigite qual produto você quer remover: ").title()

    if remover not in produtin:
        print("Produto não encontrado para remoção.")
    else:
        confirmacao = input(f"Tem certeza que quer remover '{remover}'? (S/N): ").title()
        if confirmacao == "S":
            del produtin[remover]
            print(f"Produto '{remover}' removido com sucesso!")
        else:
            print(f"Remoção de '{remover}' cancelada.")

    print("\n--- Produtos Após Remoção ---")
    print(produtin)

def cadastro_usuario():
    user = input("Fale o seu nome: ")
    email = input('Digite seu email: ')

    print(f"-------------BEM VINDO-------------\n"
          f"--------------{user}---------------")
def cadastro_funcionario():
    user = input("Fale o seu nome: ")
    print(f"-------------BEM VINDO-------------\n"
            f"--------------{user}---------------")


