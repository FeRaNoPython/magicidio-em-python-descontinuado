#FUNÇÃO QUE EXECUTA A AÇÃO "MAGIA" DO TURNO

def executar_magia(mago, oponente, rodada):

  print("")


  lista_magias = list(mago.magias_visualizacao)

  for numero, magia in enumerate(lista_magias, start=1):

    print("")

    print(f"{numero} - {magia}\n")

    for atributo, valor in mago.magias_visualizacao[magia].items():

      print(f"{atributo}: {valor}\n")

  print("\n0 - Cancelar\n")


  while True: #LOOP PARA GARANTIR QUE A OPÇÃO ESCOLHIDA EXISTE

    escolha = input("Escolha uma magia: \n")

    if escolha.isdigit() and int(escolha) <= len(lista_magias):

      break

    print("OPÇÃO INVÁLIDA!")

    print("\n")


  opcao = int(escolha)

  if opcao == 0:

    print("\n")

    return False #CANCELOU: O TURNO NÃO FOI GASTO


  magia_usada = lista_magias[opcao - 1]


  efeito = mago.usar_magia(magia_usada)

  if mago.mana < 0:

    mago.mana = 0

    print(F"\n{mago.nome}, você usou sua mana além do que podia e ela se esgotou em vão. Medite para recuperar sua mana. \n")

    return False #FALTOU MANA: O TURNO NÃO FOI GASTO


  match magia_usada.lower():


    case "projétil mágico" | "explosão": # MAGIAS DE DANO INSTANTÂNEOS

      defensiva_quebrada = ""

      if rodada <= oponente.validade_defensiva:

        if oponente.defensiva_ativa == "Barreira": # BARREIRA DO OPONENTE ATIVA

          dano_final = efeito - oponente.valor_defensiva

          oponente.valor_defensiva -= efeito

          if oponente.valor_defensiva <= 0:

            oponente.validade_defensiva = 0

            oponente.valor_defensiva = 0

            defensiva_quebrada = "Barreira"

            oponente.defensiva_ativa = "nenhuma"

        elif oponente.defensiva_ativa == "Reflexão": # REFLEXÃO DO OPONENTE ATIVA

          dano_final = efeito

          if oponente.valor_defensiva > efeito:

            mago.vida -= efeito

            dano_final = 0

          elif oponente.valor_defensiva == efeito:

            mago.vida -= (efeito * 2)

            dano_final = 0

          else:

            pass

      else:

        dano_final = efeito

      if dano_final < 0:

        dano_final = 0

      oponente.vida -= dano_final

      print(f"\n{mago.nome} usou {magia_usada.title()}! Causando {dano_final} de dano em {oponente.nome}!")

      if oponente.defensiva_ativa == "Reflexão" and oponente.valor_defensiva > efeito:

        print(f"Mas a Reflexão de {oponente.nome} refletiu {magia_usada} de {mago.nome}, causando {efeito} nele!")

      elif oponente.defensiva_ativa == "Reflexão" and oponente.valor_defensiva == efeito:

        print(f"Mas a Reflexão de {oponente.nome} refletiu {magia_usada} de {mago.nome} perfeitamente! Causando {efeito * 2} nele!")

      if defensiva_quebrada:

        print(f"A {defensiva_quebrada} de {oponente.nome} foi quebrada!")

      oponente.morte()

      mago.morte()


    case "barreira":

      mago.valor_defensiva = efeito

      mago.defensiva_ativa = magia_usada.title()

      if mago.iniciativa < oponente.iniciativa:

        mago.validade_defensiva = rodada + 3

      else:

        mago.validade_defensiva = rodada + 2

      print(f"\n{mago.nome} usou {magia_usada.title()}! Bloqueará até {efeito} de dano até o fim da rodada {mago.validade_defensiva}!")


    case "cura":

      vida_recuperada = mago.curar(efeito)

      print(f"\n{mago.nome} usou {magia_usada.title()}! Recuperando {vida_recuperada} da própria vida!")


    case "reflexão":

      mago.valor_defensiva = efeito

      mago.defensiva_ativa = magia_usada.title()

      if mago.iniciativa < oponente.iniciativa:

        mago.validade_defensiva = rodada + 2

      else:

        mago.validade_defensiva = rodada + 1

      print(f"""

{mago.nome} usou {magia_usada.title()}! 

Os próximos danos de {oponente.nome} serão refletidos caso o ataque seja menor que sua taxa de reflexão! Caso ambos os valores sejam idênticos, o dano é dobrado!

Esse efeito dura até o fim da rodada {mago.validade_defensiva}!

""")


  return True #A MAGIA FOI USADA: O TURNO ACABA