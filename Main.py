def fim_de_jogo(n,p):
    jogadas_vitoria = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in range(len(jogadas_vitoria)):
        if (jogadas_vitoria[i][0] in n and jogadas_vitoria[i][1] in n and jogadas_vitoria[i][2] in n) or (jogadas_vitoria[i][0] in p and jogadas_vitoria[i][1] in p and jogadas_vitoria[i][2] in p):
            return True
    return False

def desenhaJogo(desenha):
    print ""
    print "",desenha[0],"|",desenha[1],"|",desenha[2]
    print "-----------"
    print "",desenha[3],"|",desenha[4],"|",desenha[5]
    print "-----------"
    print "",desenha[6],"|",desenha[7],"|",desenha[8]
    print ""

jogadas_jogador = []
jogadas_cpu = []
espacos = 9
fim = 0
jogadas_vitoria = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
no_draw = 0
allowed = 0
nan = 1
desenha = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

while fim==0:
    print "1 -> jogador | 2 -> cpu\nQuem comeca?"
    while nan==1:
        decisao_ant = raw_input()
        if decisao_ant.isdigit():
            decisao = int(decisao_ant)
            nan = 0
        else:
            print "Nao entendi, repita por favor!"
    nan = 1
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
            while nan==1:
                temp_ant = raw_input("Jogador joga:\n")
                if temp_ant.isdigit():
                    temp = int(temp_ant)
                    nan = 0
                else:
                    print "Nao entendi, repita por favor!"
            nan = 1
            if temp not in jogadas_jogador and temp not in jogadas_cpu and temp>0 and temp<10:
                jogadas_jogador.append(temp)
                desenha[temp-1] = 'x'
                allowed = 1
                desenhaJogo(desenha)
            else:
                print "Nao entendi, repita por favor!"
        allowed = 0
        espacos-=1
        if fim_de_jogo(jogadas_jogador,jogadas_cpu) == False and espacos>0:
            while allowed == 0:
                while nan==1:
                    temp_ant = raw_input("CPU joga:\n")
                    if temp_ant.isdigit():
                        temp = int(temp_ant)
                        nan = 0
                    else:
                        print "Nao entendi, repita por favor!"
                nan = 1
                if temp not in jogadas_jogador and temp not in jogadas_cpu and temp>0 and temp<10:
                    jogadas_cpu.append(temp)
                    desenha[temp-1] = 'o'
                    allowed = 1
                    desenhaJogo(desenha)
                else:
                    print "Nao entendi, repita por favor!"
            allowed = 0
            espacos-=1
    elif espacos>0:
        while allowed == 0:
            while nan==1:
                temp_ant = raw_input("CPU joga:\n")
                if temp_ant.isdigit():
                    temp = int(temp_ant)
                    nan = 0
                else:
                    print "Nao entendi, repita por favor!"
            nan = 1
            if temp not in jogadas_jogador and temp not in jogadas_cpu and temp>0 and temp<10:
                jogadas_cpu.append(temp)
                desenha[temp-1] = 'o'
                allowed = 1
                desenhaJogo(desenha)
            else:
                print "Nao entendi, repita por favor!"
        allowed = 0
        espacos-=1
        if fim_de_jogo(jogadas_jogador,jogadas_cpu) == False and espacos>0:
            while allowed == 0:
                while nan==1:
                    temp_ant = raw_input("Jogador joga:\n")
                    if temp_ant.isdigit():
                        temp = int(temp_ant)
                        nan = 0
                    else:
                        print "Nao entendi, repita por favor!"
                nan = 1
                if temp not in jogadas_jogador and temp not in jogadas_cpu and temp>0 and temp<10:
                    jogadas_jogador.append(temp)
                    desenha[temp-1] = 'x'
                    allowed = 1
                    desenhaJogo(desenha)
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
