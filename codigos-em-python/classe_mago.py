#CLASSE DE CRIAÇÃO DOS MAGOS, SEUS ATRIBUTOS E SUAS AÇÕES, DICIONÁRIO COM AS MAGIAS, OS VALORES DOS SEUS EFEITOS E SEUS CUSTOS EM MANA

from magias import *

lazy import copy

class Mago:

  def __init__(self, nome: str, jogador: str):

    self.nome = nome

    self.jogador = jogador

    self.vida_maxima = 100

    self.mana_maxima = 80

    self.vida = self.vida_maxima

    self.mana = self.mana_maxima

    self.vivo = True

    self.magias = copy.deepcopy(magias)

    self.montar_magias_visualização()

    self.iniciativa = random.randint(1, 20)

    self.valor_defensiva = 0

    self.validade_defensiva = 0

    self.defensiva_ativa = "nenhuma"

    self.vitorias = 0


  def morte(self):

    if self.vida <= 0:

      self.vida = 0

      print(f"\n{self.nome} está morto e foi derrotado!")

      self.vivo = False

      return self.vivo

    else:

      self.vivo = True

      return self.vivo


  def usar_magia(self, magia_usada: str) -> int:

    info_magia = self.magias[magia_usada.lower()]

    efeito = definir_valor_efeito(info_magia)

    self.mana -= calcular_custo(magia_usada, efeito)

    return efeito


  def meditar(self):

    mana_antes = self.mana

    sorteado = random.randint(3, 10)

    self.mana = min(self.mana + sorteado, self.mana_maxima)

    return self.mana - mana_antes


  def curar(self, valor):

    vida_antes = self.vida

    self.vida = min(self.vida + valor, self.vida_maxima)

    return self.vida - vida_antes


  def rerrolar_iniciativa(self):

    self.iniciativa = random.randint(1, 20)


  def montar_magias_visualização(self):

    self.magias_visualizacao = {}

    for chave, info in self.magias.items():

      media = (info["min"] + info["max"] + 1) // 2

      custo_medio = calcular_custo(chave, media)

      self.magias_visualizacao[info["nome"]] = {"Descrição": info["descricao"], info["rotulo_medio"]: media, "Custo médio": custo_medio}


  def editar_magias(self):

    print("===== ===== OPÇÕES DE MAGIAS PARA ESCOLHER USAR EM JOGO ===== =====")

    for magia in OPÇÕES_MAGIAS:

      print(f"""

{OPÇÕES_MAGIAS[magia]["nome"]}

Descrição: 

{OPÇÕES_MAGIAS[magia]["descricao"]}


Os valores dessa magia variam de {OPÇÕES_MAGIAS[magia]["min"]} até {OPÇÕES_MAGIAS[magia]["max"]}

""")


    print("===== ===== MAGIAS USADAS ATUALMENTE EM JOGO ===== =====")

    for magia in self.magias:

      print(f"""

{self.magias[magia]["nome"]}

Descrição: 

{self.magias[magia]["descricao"]}


Os valores dessa magia variam de {self.magias[magia]["min"]} até {self.magias[magia]["max"]}

""")

      
    print("|SAIR|\n")

    while True: # GARANTIR ESCRITA CORRETA EM MAGIA_ESCOLHIDA

      if (magia_escolhida := input("Escolha uma magia para usar no jogo\n").lower()) in OPÇÕES_MAGIAS:

        if magia_escolhida in self.magias:

          print("ESSA MAGIA JÁ ESTÁ EM USO! TENTE DE NOVO OU SAIA.")

          continue

        break

      elif magia_escolhida.lower() == "sair":

        return None

      else:

        print("ESCRITA INCORRETA!")


    print("|SAIR|\n")

    while True: # GARANTIR ESCRITA CORRETA EM MAGIA_TROCADA:


      if (magia_trocada := input("Escolha uma magia para trocar\n").lower()) in self.magias:

        break

      elif magia_trocada.lower() == "sair":

        return None

      else:

        print("ESCRITA INCORRETA!")


    magias_editadas = {}

    for magia in self.magias:

      if magia == magia_trocada:

        magias_editadas[magia_escolhida] = copy.deepcopy(OPÇÕES_MAGIAS[magia_escolhida])

      else:

        magias_editadas[magia] = copy.deepcopy(OPÇÕES_MAGIAS[magia])

    self.magias = magias_editadas

    self.montar_magias_visualização()