class Vendedor:
    def mostrar_nome(nome):
        print(f"O nome do vendedor é: {nome}")

    def mostrar_produto(produto):
        print(f"O produto vendido é: {produto}")

    def mostrar_tudo(nome, produto):
        print(f"O vendedor {nome} está vendendo {produto}")


nome_vendedor = "Ruan Luiz"
produto_vendido = "iPhone 11 Pro Max"

Vendedor.mostrar_nome(nome_vendedor)
Vendedor.mostrar_produto(produto_vendido)
Vendedor.mostrar_tudo(nome_vendedor, produto_vendido)
