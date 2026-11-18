from classe_mago import *

from acao_magia import *

from interface_status import *

from menu_principal import *

def main():

  while True: # LOOP DO JOGO RODANDO

    MAGO_CASA = Mago("Potássius", "Hulkblox") # NOME DO MAGO, NICKNAME DO JOGADOR

    MAGO_VISITANTE = Mago("Altíssimus", "FeRa") # NOME DO MAGO, NICKNAME DO JOGADOR

    # menu_principal() # menu_principal.py para ver, incompleto

    while MAGO_CASA.iniciativa == MAGO_VISITANTE.iniciativa:

      MAGO_CASA.rerrolar_iniciativa()

      MAGO_VISITANTE.rerrolar_iniciativa()

    ordem_iniciativa = sorted([(MAGO_CASA.iniciativa, MAGO_CASA ), (MAGO_VISITANTE.iniciativa, MAGO_VISITANTE)], reverse=True)

    rodada = 1

    while MAGO_CASA.vivo and MAGO_VISITANTE.vivo: #LOOP DA BATALHA

      for _, mago in ordem_iniciativa:

        if mago == MAGO_CASA:

          oponente = MAGO_VISITANTE

        else:

          oponente = MAGO_CASA

        while True: #LOOP DO TURNO

          mostrar_status(rodada, mago, oponente, ordem_iniciativa, MAGO_CASA, MAGO_VISITANTE)

          if(acao := input("Escolha uma ação: \n")).lower() == "magia" or acao.lower() == "magias":

            if not executar_magia(mago, oponente, rodada):

              continue

          elif acao.lower() == "meditar":

            mana_recuperada = mago.meditar()

            print(f"{mago.nome} passará o turno meditando. Recarregando {mana_recuperada} da sua própria mana.")

          else:

            print("ESCRITA INCORRETA!")

            print("\n")

            continue

          break

        if not MAGO_CASA.vivo or not MAGO_VISITANTE.vivo:

          break

      if not MAGO_CASA.vivo or not MAGO_VISITANTE.vivo:

        break

      rodada += 1

      # RESETA MAGIAS DEFENSIVAS

      if rodada > mago.validade_defensiva:

        mago.validade_defensiva = 0

        mago.valor_defensiva = 0

        mago.defensiva_ativa = "nenhuma"

      if rodada > oponente.validade_defensiva:

        oponente.validade_defensiva = 0

        oponente.valor_defensiva = 0

        oponente.defensiva_ativa = "nenhuma"

    # VITÓRIA

    if MAGO_CASA.vivo:

      vencedor = MAGO_CASA

    else:

      vencedor = MAGO_VISITANTE

    print(f"\n{vencedor.jogador} | {vencedor.nome} venceu o duelo na rodada {rodada}!")

if __name__ == "__main__":

  main()

