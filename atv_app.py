from funcoes.funcoes_atv import produtos
from funcoes.funcoes_atv import compra_produto
from funcoes.funcoes_atv import saldo_saque
from funcoes.funcoes_atv import deleta_produto, cadastro_usuario, cadastro_funcionario

escolha_func_usu = int(input("Escolha\n"
            "1- Usuario\n"
            "2 - Funcionario\n"
            "Digite Aqui: "))
if escolha_func_usu == 1:
    cadastro_usuario()

    while True:
        n = int(input("Escolha\n"
                "1 - Para compra um Produto\n"
                "2 - Ver seu saldo / Depositar\n"
                "3 - sair\n"
                "Digite: "))

        match n:
            case 1:
                compra_produto()
            case 2:
                saldo_saque()
            case 3:
                break
            case _:
                print("Digito errado")

elif escolha_func_usu == 2:
    cadastro_funcionario()
    while True:

        b = int(input("Escolha\n"
                "1- Para add Produto\n"
                "2- Deletar Produto\n"
                "3 - sair\n"
                "Digite: "))
        match b:
            case 1:
                produtos()
            case 2:
                deleta_produto()
            case 3:
                print("Saindo....")
                break
            case _:
                print("Digito errado")
else:
    print("Digito errado")







