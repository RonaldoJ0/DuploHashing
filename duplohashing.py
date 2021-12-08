import os


class DuploHash:
    def __init__(self, tamanho) -> None:
        self.lista = [["none", "none"]] * tamanho

    def converterString(self, string):
        count = 0
        for i in string:
            count += ord(i)
        return count

    def hash1(self, valor) -> int:
        val = self.converterString(valor)
        return val % len(self.lista)

    def hash2(self, valor) -> int:
        return 3

    def inserir(self, item) -> None:
        print("\nInserindo o elemento:\n Nome: {}\n RG: {}".format(item[0], item[1]))
        pos = self.hash1(item[0])
        print("Tentando inserir no indice {}".format(pos))
        if self.lista[pos][0] == "none":
            self.lista[pos] = [item[0], item[1]]
            print("Posição final -> {}({})".format(pos, item))
        else:
            v = self.hash2(item[0])
            inserido = False
            j = 1
            while j < len(self.lista):
                print("Houve colisão! Numero de colisões: {}".format(j))
                pos1 = (pos + j * v) % len(self.lista)
                j += 1
                print("Tentando inserir no indice {}".format(pos1))
                if self.lista[pos1][0] == "none":
                    self.lista[pos1] = [item[0], item[1]]
                    print("Posição final -> {}({})".format(pos1, item))
                    inserido = True
                    break
            if not inserido:
                print("O valor {} não foi inserido".format(item))

    def tem_valor_semelhante(self, valor) -> bool:
        h1 = self.hash1(valor)
        h2 = self.hash2(valor)
        j = 0
        c = 0
        while j < len(self.lista):
            pos = (h1 + j * h2) % len(self.lista)
            if self.lista[pos][0] == valor:
                c += 1
            j += 1

        if c > 1:
            return True
        return False

    def buscar_simples(self, valor) -> None:
        encontrado = False
        pos = self.hash1(valor)
        print("Procurando na posição: {}".format(pos))
        if self.lista[pos][0] == valor:
            print("O elemento foi encontrado em: {}({})".format(pos, self.lista[pos]))
            encontrado = True
        else:
            v = self.hash2(valor)
            j = 1
            while j < len(self.lista):
                print("Elemento não encontrado! Numero de tentativas: {}".format(j))
                pos1 = (pos + j * v) % len(self.lista)
                j += 1
                print("Procurando na posição: {}".format(pos1))
                if self.lista[pos1][0] == valor:
                    print(
                        "O elemento foi encontrado em: {}({})".format(
                            pos1, self.lista[pos1]
                        )
                    )
                    encontrado = True
                    break
        if not encontrado:
            print("O valor {} não foi encontrado".format(valor))

    def buscar_com_rg(self, valor, rg) -> None:
        encontrado = False
        pos = self.hash1(valor)
        print("Procurando na posição: {}".format(pos))
        if self.lista[pos][0] == valor and self.lista[pos][1] == rg:
            print("O elemento foi encontrado em: {}({})".format(pos, self.lista[pos]))
            encontrado = True
        else:
            v = self.hash2(valor)
            j = 1
            while j < len(self.lista):
                print("Elemento não encontrado! Numero de tentativas: {}".format(j))
                pos1 = (pos + j * v) % len(self.lista)
                j += 1
                print("Procurando na posição: {}".format(pos1))
                if self.lista[pos1][0] == valor and self.lista[pos1][1] == rg:
                    print(
                        "O elemento foi encontrado em: {}({})".format(
                            pos1, self.lista[pos1]
                        )
                    )
                    encontrado = True
                    break
        if not encontrado:
            print("O valor {} não foi encontrado".format(valor))

    def deletar_simples(self, valor) -> None:
        encontrado = False
        pos = self.hash1(valor)
        print("Procurando na posição: {}".format(pos))
        if self.lista[pos][0] == valor:
            self.lista[pos] = ["###", "###"]
            print("O elemento {}({}) foi deletado".format(pos, self.lista[pos]))
            encontrado = True
        else:
            v = self.hash2(valor)
            j = 1
            while j < len(self.lista):
                print("Elemento não encontrado! Numero de tentativas: {}".format(j))
                pos1 = (pos + j * v) % len(self.lista)
                j += 1
                print("Procurando na posição: {}".format(pos1))
                if self.lista[pos1][0] == valor:
                    self.lista[pos1] = ["###", "###"]
                    print(
                        "O elemento {}({}) foi deletado".format(pos1, self.lista[pos1])
                    )
                    encontrado = True
                    break
        if not encontrado:
            print("O valor {} não foi encontrado".format(valor))

    def deletar_com_rg(self, valor, rg) -> None:
        encontrado = False
        pos = self.hash1(valor)
        print("Procurando na posição: {}".format(pos))
        if self.lista[pos][0] == valor and self.lista[pos][1] == rg:
            self.lista[pos] = ["###", "###"]
            print("O elemento {}({}) foi deletado".format(pos, self.lista[pos]))
            encontrado = True
        else:
            v = self.hash2(valor)
            j = 1
            while j < len(self.lista):
                print("Elemento não encontrado! Numero de tentativas: {}".format(j))
                pos1 = (pos + j * v) % len(self.lista)
                j += 1
                print("Procurando na posição: {}".format(pos1))
                if self.lista[pos1][0] == valor and self.lista[pos1][1] == rg:
                    self.lista[pos1] = ["###", "###"]
                    print(
                        "O elemento {}({}) foi deletado".format(pos1, self.lista[pos1])
                    )
                    encontrado = True
                    break
        if not encontrado:
            print("O valor {} não foi encontrado".format(valor))

    def exibir(self) -> None:
        for i in range(len(self.lista)):
            print("{}({})".format(i, self.lista[i]))


def SubMenu(obj: DuploHash) -> None:
    while True:
        print(
            """
        1. Buscar
        2. Deletar
        3. Exibir
        4. Sair
        """
        )
        ans = input("Informe o numero da opção: ")
        if ans == "1":
            n = input("Informe um nome: ")
            if obj.tem_valor_semelhante(n):
                os.system("clear")
                while True:
                    print("Existe mais de um elemento com esse nome!\n")
                    print(
                        """
                    1. Busca Simples
                    2. Busca com RG
                    """
                    )
                    a = input("Informe o numero da opção: ")
                    if a == "1":
                        os.system("clear")
                        obj.buscar_simples(n)
                        break
                    elif a == "2":
                        os.system("clear")
                        r = input("Informe o rg: ")
                        obj.buscar_com_rg(n, r)
                        break
                    else:
                        print("Opção invalida!!!")
            else:
                os.system("clear")
                obj.buscar_simples(n)
        elif ans == "2":
            n = input("Informe um nome: ")
            if obj.tem_valor_semelhante(n):
                os.system("clear")
                while True:
                    print("Existe mais de um elemento com esse nome!\n")
                    print(
                        """
                    1. Deletar Simples
                    2. Deletar por RG
                    """
                    )
                    a = input("Informe o numero da opção: ")
                    if a == "1":
                        os.system("clear")
                        obj.deletar_simples(n)
                        break
                    elif a == "2":
                        os.system("clear")
                        r = input("Informe o rg: ")
                        obj.deletar_com_rg(n, r)
                        break
                    else:
                        print("Opção invalida!!!")
            else:
                os.system("clear")
                obj.deletar_simples(n)
        elif ans == "3":
            os.system("clear")
            obj.exibir()
        elif ans == "4":
            break
        else:
            print("Opção invalida!!!")


def Menu() -> None:
    while True:
        print(
            """
        1. Inserir elementos usando um arquivo.
        2. Encerrar aplicação.
        """
        )
        ans = input("Informe o numero da opção: ")
        if ans == "1":
            p = input("Informe o caminho do arquivo nesse computador:\n")
            while os.path.exists(p) == False:
                os.system("clear")
                print("Diretório inexistente")
                p = input("Informe o caminho do arquivo nesse computador:\n")
            linhas = []
            with open(p, "r") as f:
                linhas = f.readlines()
            obj = DuploHash(len(linhas))
            for linha in linhas:
                a = linha.split(",")
                a[1] = a[1][:-1]
                obj.inserir(a)
            SubMenu(obj)
        elif ans == "2":
            print("Xau xau!!!")
            break
        else:
            print("Opção invalida!!!")


if __name__ == "__main__":
    Menu()
