def fim_de_jogo(n,p):
    jogadas_vitoria = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for i in range(len(jogadas_vitoria)):
        if (jogadas_vitoria[i][0] in n and jogadas_vitoria[i][1] in n and jogadas_vitoria[i][2] in n) or (jogadas_vitoria[i][0] in p and jogadas_vitoria[i][1] in p and jogadas_vitoria[i][2] in p) or len(jogadas_jogador)+len(jogadas_cpu)==9:
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
    #print jogadas_jogador,jogadas_cpu

def podevencer(n): #n => jogadas_cpu
    for i in range(len(jogadas_vitoria)):
        if (jogadas_vitoria[i][0] in n and jogadas_vitoria[i][1] in n and jogadas_vitoria[i][2] not in jogadas_jogador and jogadas_vitoria[i][2] not in jogadas_cpu):
            return jogadas_vitoria[i][2]
        elif (jogadas_vitoria[i][0] in n and jogadas_vitoria[i][2] in n and jogadas_vitoria[i][1] not in jogadas_jogador and jogadas_vitoria[i][1] not in jogadas_cpu):
            return jogadas_vitoria[i][1]
        elif (jogadas_vitoria[i][1] in n and jogadas_vitoria[i][2] in n and jogadas_vitoria[i][0] not in jogadas_jogador and jogadas_vitoria[i][0] not in jogadas_cpu):
            return jogadas_vitoria[i][0]
    return 10


def naodeixevencer(n): # n => jogadas_jogador
    for i in range(len(jogadas_vitoria)):
        if (jogadas_vitoria[i][0] in n and jogadas_vitoria[i][1] in n and jogadas_vitoria[i][2] not in jogadas_jogador and jogadas_vitoria[i][2] not in jogadas_cpu):
            return jogadas_vitoria[i][2]
        elif (jogadas_vitoria[i][0] in n and jogadas_vitoria[i][2] in n and jogadas_vitoria[i][1] not in jogadas_jogador and jogadas_vitoria[i][1] not in jogadas_cpu):
            return jogadas_vitoria[i][1]
        elif (jogadas_vitoria[i][1] in n and jogadas_vitoria[i][2] in n and jogadas_vitoria[i][0] not in jogadas_jogador and jogadas_vitoria[i][0] not in jogadas_cpu):
            return jogadas_vitoria[i][0]
    return 10

jogadas_jogador = []
jogadas_cpu = []
#espacos = 9
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

resolve = 0
while (fim_de_jogo(jogadas_jogador,jogadas_cpu) == False):# and espacos>0):
    if jogador_comeca == True or len(jogadas_jogador)+len(jogadas_cpu)>0:
        resolve = 1
    if (fim_de_jogo(jogadas_jogador,jogadas_cpu) == False): #if das jogadas do jogador
        while allowed == 0 and resolve == 1:
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
        #espacos-=1
        if fim_de_jogo(jogadas_jogador,jogadas_cpu) == False:#espacos>0:     # if das jogadas da cpu
            while allowed == 0:
                if jogadas_jogador==[2,8] or jogadas_jogador==[8,2] or jogadas_jogador==[4,6] or jogadas_jogador==[6,4]:
                    jogadas_cpu.append(1)
                    desenha[0] = 'o'
                    allowed = 1
                    desenhaJogo(desenha)
                else:
                    temp = podevencer(jogadas_cpu)
                    if temp not in jogadas_jogador and temp not in jogadas_cpu and temp>0 and temp<10:
                        jogadas_cpu.append(temp)
                        desenha[temp-1] = 'o'
                        allowed = 1
                        desenhaJogo(desenha)
                        #print "pode vencer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                    else:
                        temp = naodeixevencer(jogadas_jogador)
                        #print temp,'AAA'
                        if temp not in jogadas_jogador and temp not in jogadas_cpu and temp>0 and temp<10:
                            jogadas_cpu.append(temp)
                            desenha[temp-1] = 'o'
                            allowed = 1
                            desenhaJogo(desenha)
                            #print "naodeixevencer!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                        elif jogadas_jogador == [1,9] or jogadas_jogador == [9,1] or jogadas_jogador == [3,7] or jogadas_jogador == [7,3]:
                            temp = 4
                            jogadas_cpu.append(temp)
                            desenha[temp-1] = 'o'
                            allowed = 1
                            desenhaJogo(desenha)
                            #print "caso especial!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                        else:
                            temp = 5
                            if temp not in jogadas_jogador and temp not in jogadas_cpu and temp>0 and temp<10:
                                jogadas_cpu.append(temp)
                                desenha[temp-1] = 'o'
                                allowed = 1
                                desenhaJogo(desenha)
                                #print "centro!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                            else:
                                ponta = [1,3,7,9]
                                meio = [2,4,6,8]
                                original = jogadas_jogador
                                while len(jogadas_jogador)<2:
                                    jogadas_jogador.append(30)
                                if ((jogadas_jogador[0] in ponta and jogadas_jogador[1] in meio) or (jogadas_jogador[1] in ponta and jogadas_jogador[0] in meio)) and (len(jogadas_jogador) == 2):
                                    jogadas_jogador = original
                                    aux = jogadas_jogador
                                    list.sort(aux)
                                    if aux == [2,7] or aux == [3,4]:
                                        temp = 1
                                        jogadas_cpu.append(temp)
                                        desenha[temp-1] = 'o'
                                        allowed = 1
                                        desenhaJogo(desenha)
                                        #print "caso 1!!!!!!!!!!!!!!!!!!"
                                    if aux == [2,9] or aux == [1,6]:
                                        temp = 3
                                        jogadas_cpu.append(temp)
                                        desenha[temp-1] = 'o'
                                        allowed = 1
                                        desenhaJogo(desenha)
                                        #print "caso 2!!!!!!!!!!!!!!!!!!"
                                    if aux == [4,9] or aux == [1,8]:
                                        temp = 7
                                        jogadas_cpu.append(temp)
                                        desenha[temp-1] = 'o'
                                        allowed = 1
                                        desenhaJogo(desenha)
                                        #print "caso 3!!!!!!!!!!!!!!!!!!"
                                    if aux == [3,8] or aux == [6,7]:
                                        temp = 9
                                        jogadas_cpu.append(temp)
                                        desenha[temp-1] = 'o'
                                        allowed = 1
                                        desenhaJogo(desenha)
                                        #print "caso 4!!!!!!!!!!!!!!!!!!"
                                else:
                                    jogadas_jogador = original
                                    aux = jogadas_jogador
                                    list.sort(aux)
                                    if aux[0] in meio and aux[1] in meio and len(aux) == 2:
                                        if aux == [2,4]:
                                            temp = 1
                                            jogadas_cpu.append(temp)
                                            desenha[temp-1] = 'o'
                                            allowed = 1
                                            desenhaJogo(desenha)
                                            #print "caso 2.1!!!!!!!!!!!!!!!!!!"
                                        if aux == [2,6]:
                                            temp = 3
                                            jogadas_cpu.append(temp)
                                            desenha[temp-1] = 'o'
                                            allowed = 1
                                            desenhaJogo(desenha)
                                            #print "caso 2.2!!!!!!!!!!!!!!!!!!"
                                        if aux == [4,8]:
                                            temp = 7
                                            jogadas_cpu.append(temp)
                                            desenha[temp-1] = 'o'
                                            allowed = 1
                                            desenhaJogo(desenha)
                                            #print "caso 2.3!!!!!!!!!!!!!!!!!!"
                                        if aux == [6,8]:
                                            temp = 9
                                            jogadas_cpu.append(temp)
                                            desenha[temp-1] = 'o'
                                            allowed = 1
                                            desenhaJogo(desenha)
                                            #print "caso 2.4!!!!!!!!!!!!!!!!!!"
                                    else:
                                        repete = 0
                                        for i in range(len(ponta)):
                                            if ponta[i] not in jogadas_jogador and ponta[i] not in jogadas_cpu and repete == 0:
                                                temp = ponta[i]
                                                repete = 1
                                                jogadas_cpu.append(temp)
                                                desenha[temp-1] = 'o'
                                                allowed = 1
                                                desenhaJogo(desenha)
                                                #print "corners!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
                                        if repete==0:
                                            for i in range(len(meio)):
                                                if meio[i] not in jogadas_jogador and meio[i] not in jogadas_cpu and repete == 0:
                                                    temp = meio[i]
                                                    repete = 1
                                                    jogadas_cpu.append(temp)
                                                    desenha[temp-1] = 'o'
                                                    allowed = 1
                                                    desenhaJogo(desenha)
                                                    #print "middles!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"


            allowed = 0
            #espacos-=1
    
for i in range(len(jogadas_vitoria)):
    if jogadas_vitoria[i][0] in jogadas_jogador and jogadas_vitoria[i][1] in jogadas_jogador and jogadas_vitoria[i][2] in jogadas_jogador:
        print "Jogador venceu"
        no_draw = 1
    elif jogadas_vitoria[i][0] in jogadas_cpu and jogadas_vitoria[i][1] in jogadas_cpu and jogadas_vitoria[i][2] in jogadas_cpu:
        print "CPU venceu"
        no_draw = 1
if no_draw == 0:
    print "Deu velha"
