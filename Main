def fim_de_jogo(n,p):
    jogadas_vitoria = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    vit = 0
    for i in range(len(jogadas_vitoria)):
        if (jogadas_vitoria[i][0] in n and jogadas_vitoria[i][1] in n and jogadas_vitoria[i][2] in n) or (jogadas_vitoria[i][0] in p and jogadas_vitoria[i][1] in p and jogadas_vitoria[i][2] in p):
            return True
    return False

jogadas_jogador = []
jogadas_cpu = []
fim = 0
espacos = 9
jogadas_vitoria = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
no_draw = 0
allowed = 0

while fim==0:
    print "1 -> jogador | 2 -> cpu\nQuem comeca?"
    decisao = input()
    if decisao == 1:
        jogador_comeca = True
        fim = 1
    elif decisao == 2:
        jogador_comeca = False
        fim = 1
    else:
        print "Nao entendi, repita por favor!"

while (fim_de_jogo(jogadas_jogador,jogadas_cpu) == False and espacos>0):
    if (jogador_comeca == True and espacos>0):
        while allowed == 0:
            temp = input("Jogador joga:\n")
            if temp not in jogadas_jogador and temp not in jogadas_cpu and temp>0 and temp<10:
                jogadas_jogador.append(temp)
                allowed = 1
            else:
                print "Nao entendi, repita por favor!"
        allowed = 0
        espacos-=1
        if fim_de_jogo(jogadas_jogador,jogadas_cpu) == False and espacos>0:
            while allowed == 0:
                temp = input("CPU joga:\n")
                if temp not in jogadas_jogador and temp not in jogadas_cpu and temp>0 and temp<10:
                    jogadas_cpu.append(temp)
                    allowed = 1
                else:
                    print "Nao entendi, repita por favor!"
            allowed = 0
            espacos-=1
    elif espacos>0:
        while allowed == 0:
            temp = input("CPU joga:\n")
            if temp not in jogadas_jogador and temp not in jogadas_cpu and temp>0 and temp<10:
                jogadas_cpu.append(temp)
                allowed = 1
            else:
                print "Nao entendi, repita por favor!"
        allowed = 0
        espacos-=1
        if fim_de_jogo(jogadas_jogador,jogadas_cpu) == False and espacos>0:
            while allowed == 0:
                temp = input("Jogador joga:\n")
                if temp not in jogadas_jogador and temp not in jogadas_cpu and temp>0 and temp<10:
                    jogadas_jogador.append(temp)
                    allowed = 1
                else:
                    print "Nao entendi, repita por favor!"
            allowed = 0
            espacos-=1

for i in range(len(jogadas_vitoria)):
    if jogadas_vitoria[i][0] in jogadas_jogador and jogadas_vitoria[i][1] in jogadas_jogador and jogadas_vitoria[i][2] in jogadas_jogador:
        print "Jogador venceu"
        no_draw = 1
    elif jogadas_vitoria[i][0] in jogadas_cpu and jogadas_vitoria[i][1] in jogadas_cpu and jogadas_vitoria[i][2] in jogadas_cpu:
        print "CPU venceu"
        no_draw = 1
if no_draw == 0:
    print "Deu velha"
