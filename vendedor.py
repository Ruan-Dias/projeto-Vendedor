class Vendedor:
    def definir_nome(self, nome):
        self.nome = nome

    def definir_produto(self, produto):
        self.produto = produto

    def mostrar_nome(self):
        print(f"O nome do vendedor é: {self.nome}")

    def mostrar_produto(self):
        print(f"O produto vendido é: {self.produto}")

    def mostrar_tudo(self):
        print(f"O vendedor {self.nome} está vendendo {self.produto}")


vendedor1 = Vendedor()

vendedor1.definir_nome("Ruan Luiz")
vendedor1.definir_produto("Placa de vídeo")

vendedor1.mostrar_nome()
vendedor1.mostrar_produto()
vendedor1.mostrar_tudo()
