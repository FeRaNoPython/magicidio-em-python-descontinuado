#FUNÇÃO DA INTERFACE DE STATUS

def mostrar_status(rodada, mago, oponente, ordem_iniciativa, mago_casa, mago_visitante):

  print(f"""\n ===== {mago_casa.nome} Vs. {mago_visitante.nome} =====

Rodada: {rodada}                       OPONENTE: {oponente.jogador} | {oponente.nome} VIDA: {oponente.vida} MANA: {oponente.mana}

Ordem de jogadas:               MAGIA DEFENSIVA ATIVA: {oponente.defensiva_ativa} (valor: {oponente.valor_defensiva}) (dura até a rodada {oponente.validade_defensiva})

{ordem_iniciativa[0][0]} - {ordem_iniciativa[0][1].nome}

{ordem_iniciativa[1][0]} - {ordem_iniciativa[1][1].nome}

{mago.jogador}

{mago.nome}

VIDA: {mago.vida} MANA: {mago.mana} MAGIA DEFENSIVA ATIVA: {mago.defensiva_ativa} (valor: {mago.valor_defensiva}) (dura até a rodada {mago.validade_defensiva})

|MAGIAS|   |MEDITAR|""")