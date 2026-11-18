#info DAS MAGIAS E FUNÇÕES DE EFEITO E CUSTO

lazy import random


OPÇÕES_MAGIAS = { # TODAS AS MAGIAS DO JOGO

  "projétil mágico": {

    "nome": "Projétil Mágico",

    "descricao": """Magia básica de projéteis que qualquer mago sabe usar. Fraca, mas muito útil para evitar gastar mana à toa!

além disso, pode ser o cheque-mate para a vitória em qualquer confronto!""",

    "rotulo_medio": "Dano médio",

    "min": 4,

    "max": 14

  },

  "barreira": {

    "nome": "Barreira",

    "descricao": """Magia de defesa mais fácil de aprender. Dura 3 rodadas, contando com a de uso para o mago em vantagem na iniciativa.

Bloqueia o dano até que a rodada de validade chegue ou que até toda barreira ser destruída""",

    "rotulo_medio": "Defesa média",

    "min": 6,

    "max": 15

  },

  "cura": {

    "nome": "Cura",

    "descricao": """Magia de cura de certa forma, básica, masterizada pela maioria dos magos experientes para evitar aperto,

mas já foi a magia mais complexa da humanidade!""",

    "rotulo_medio": "Recuperação média",

    "min": 2,

    "max": 14

  },

  "explosão": {

    "nome": "Explosão",

    "descricao": """Magia de dano massivo onde uma grande quantidade de energia concentrada é liberada.

Ótimo para quebrar defesas e começar o combate com certa vantagem, mas gasta enormes quantidades de mana!""",

    "rotulo_medio": "Dano médio",

    "min": 15,

    "max": 30

  },

  "reflexão": {

    "nome": "Reflexão",

    "descricao": """Magia espectral que gera um "espelho" parecido com a Barreira. 

Mas pode refletir magias de ataques de inimigos a uma certa taxa de sucesso.

Dura 2 rodadas contando com a de uso para o mago em vantagem na iniciativa.""",

    "rotulo_medio": "Taxa de reflexão de dano média",

    "min": 4,

    "max": 18

  }

}


magias = { # MAGIAS BÁSICAS

  "projétil mágico": {

    "nome": "Projétil Mágico",

    "descricao": """Magia básica de projéteis que qualquer mago sabe usar. Fraca, mas muito útil para evitar gastar mana à toa!

além disso, pode ser o cheque-mate para a vitória em qualquer confronto!""",

    "rotulo_medio": "Dano médio",

    "min": 4,

    "max": 14

  },

  "barreira": {

    "nome": "Barreira",

    "descricao": """Magia de defesa mais fácil de aprender. Dura 3 rodadas, contando com a de uso para o mago em vantagem na iniciativa.

Bloqueia o dano até que a rodada de validade chegue ou que até toda barreira ser destruída""",

    "rotulo_medio": "Defesa média",

    "min": 6,

    "max": 15

  },

  "cura": {

    "nome": "Cura",

    "descricao": """Magia de cura de certa forma, básica, masterizada pela maioria dos magos experientes para evitar aperto,

mas já foi a magia mais complexa da humanidade!""",

    "rotulo_medio": "Recuperação média",

    "min": 2,

    "max": 14

  },

  "explosão": {

    "nome": "Explosão",

    "descricao": """Magia de dano massivo onde uma grande quantidade de energia concentrada é liberada.

Ótimo para quebrar defesas e começar o combate com certa vantagem, mas gasta enormes quantidades de mana!""",

    "rotulo_medio": "Dano médio",

    "min": 15,

    "max": 30

  }

}


def definir_valor_efeito(info: dict) -> int:

  return random.randint(info["min"], info["max"])



def calcular_custo(magia: str, efeito: int) -> int:

  match magia.lower():

    case "projétil mágico":

      return (efeito // 2) + 1

    case "barreira":

      return 5 + (efeito // 3)

    case "cura":

      return 10 + (efeito // 2)

    case "explosão":

      return round(efeito + (efeito / 3 - 4))

    case "reflexão":

      return round(efeito + (efeito / 4 + 4))