class Node:
    def __init__(self, cepa:str, parent = None):
        self.cepa = cepa
        self.parent = parent
        self.children = []

class Arvore:
    # A árvore é criada com uma raiz
    def __init__(self, cepa:str):
        self.root = Node(cepa)

    # Encontra o nó a que se adicionarão os filhos, pesquisando primeiro as folhas
    def add_filhos(self, pai:str, filhos:list):
        parent = self.busca_folhas(pai, self.root)
        for child in filhos:
            # É criado um novo nó, com referência ao pai, para facilitar a navegação
            f = Node(child, parent)
            parent.children.append(f)
    
    # Faz as comparações iniciando das extremidades, com intenção de agilizar na criação da árvore,
    # dado o formato de entrada
    def busca_folhas(self, cepa: str, node:Node):
        for child in node.children:
            aux = self.busca_folhas(cepa, child)
            if aux != None: return aux
        if node.cepa == cepa: return node

    # Compara o nó atual com a cepa a cada passo, retorna a pofundez ou "tamanho" do galho
    def __busca_profundeza(self, cepa: str, node:Node, profundeza:int = 0):
        for child in node.children:
            if child.cepa == cepa: return child, profundeza+1
            aux = self.__busca_profundeza(cepa, child, profundeza +1)
            if aux != None: return aux

    # Traça o caminho até o primeiro ancestral comum
    # node_a é o nó com a menor profundeza, que corresponde a profundeza_a
    def __caminho_raiz(self, node_a:Node, node_b:Node, profundeza_a:int, profundeza_b:int):
        caminho_a = []
        caminho_b = []
        # O caminho do nó mais profundo até que ambos estejam no mesmo nível
        while(profundeza_b > profundeza_a):
            node_b = node_b.parent
            caminho_b.append(node_b.cepa)
            profundeza_b -= 1
        # Então é feito o caminho de "subir" a árvore até que ambos os nós cheguem no mesmo ponto
        while(node_a != node_b):
            node_a = node_a.parent
            caminho_a.append(node_a.cepa)
            node_b = node_b.parent
            caminho_b.append(node_b.cepa)
        # Os caminhos são refeitos ao contrário
        caminho_b.reverse()
        caminho_a.reverse()
        return caminho_a , caminho_b

    # Encontra os nós das cepas A e B e sua profundidade na árvore, então acha o caminho
    def busca_ancestral(self, cepa_a:str, cepa_b:str):
    
        resposta_profundeza_a = self.__busca_profundeza(cepa_a, self.root)
        resposta_profundeza_b = self.__busca_profundeza(cepa_b, self.root)
        if resposta_profundeza_a == None or resposta_profundeza_b == None:
            print("cepa nao encontrada")
            return None , None
        else:
            node_a, profundeza_a = resposta_profundeza_a[0] , resposta_profundeza_a[1]
            node_b, profundeza_b = resposta_profundeza_b[0] , resposta_profundeza_b[1]
        if profundeza_a < profundeza_b:
            caminho_menor,caminho_maior = self.__caminho_raiz(node_a, node_b, profundeza_a, profundeza_b)
        else:
            caminho_maior,caminho_menor = self.__caminho_raiz(node_b, node_a, profundeza_b, profundeza_a)
        return caminho_menor,caminho_maior
    
# A entrada inicial ficará fora do loop, dela tiramos a raíz
linha_inicial = input().split()
raiz = linha_inicial[0].replace(':','') # Isolando o primeiro termo e limpando o ":" 
arvore = Arvore(raiz)
arvore.add_filhos(raiz,linha_inicial[1:])

while True:
    entrada = input().split()
    if entrada[0] == '0':
        break
    no = entrada[0].replace(':','') # Isolando o primeiro elemento de cada entrada e limpando ':'
    arvore.add_filhos(no,entrada[1:])

x,y = input().split()

ancestral = arvore.busca_ancestral(x,y)

if ancestral[0] != None and ancestral[1]!=None:
    caminho_1 = ancestral[0]
    caminho_2 = ancestral[1]
    print(caminho_1[0])
    imprimir =[]
    caminho_1.reverse()
    imprimir.append(x)
    for i in range(len(caminho_1)):
        imprimir.append(caminho_1[i])
    for i in range(1,len(caminho_2)):
        imprimir.append(caminho_2[i])
    imprimir.append(y)
    print(*imprimir, sep = ' - ' )
