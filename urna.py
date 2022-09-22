ct_votos = 0
ct_candidato_1 = 0
ct_candidato_2 = 0
ct_candidato_3 = 0
ct_candidato_4 = 0
ct_candidato_5 = 0
ct_candidato_6 = 0
while True:
    voto = int(input("insira o numero do seu candidato: "))
    if voto == 1:
        print ("voto computado")
        ct_candidato_1 += 1
        ct_votos += 1

    elif voto ==2:
        print("voto computado")
        ct_candidato_2 += 1
        ct_votos += 1

    elif voto ==3:
        print("voto computado")
        ct_candidato_3 += 1
        ct_votos += 1

    elif voto ==4:
        print("voto computado")
        ct_candidato_4 += 1
        ct_votos += 1

    elif voto ==5:
        print("voto computado")
        ct_candidato_5 += 1
        ct_votos += 1

    elif voto ==6:
        print("voto computado")
        ct_candidato_6 += 1
        ct_votos += 1

    elif voto ==0:
        print("****************************************")
        print("Resumo dos votos")
        print("votos de Jose:",ct_candidato_1)
        print("votos de João:",ct_candidato_2)
        print("votos de Gustavo:",ct_candidato_3)
        print("votos de Pedro:",ct_candidato_4)
        print("votos nulos:",ct_candidato_5)
        print("votos em branco:", ct_candidato_6)
        print("Total de votos:",ct_votos)
        print(f'porcentagem de votos nulos sobre o total: {(ct_candidato_5/ct_votos)*100:.2f}%')
        print(f'porcentagem de votos brancos sobre o total: {(ct_candidato_6 / ct_votos) * 100:.2f}%')
        break

    else:
        print("ERRO CANDIDATO DESCONHECIDO")

