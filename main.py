   
def my_index(escolha,lista):
    for i in range(len(lista)):
        if escolha == lista[i]:
            return i

def menor(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if menor >= lista[i]:
            menor = lista[i]
            index = i
    return index

def maior(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if maior <= lista[i]:
            maior = lista[i]
            index = i
    return index

def phAlto(ph, praia):
    print(f"O pH de {ph} em {praia} é superior a 8.4, sendo considerado irregular. Algumas consequências desse pH nas águas são:")
    print("- Desbalanceamento Químico: Alterações na química da água que podem afetar os organismos marinhos.")
    print("- Impacto na Biodiversidade: Muitas espécies podem não sobreviver ou se reproduzir em condições de pH alterado.")
    print("Medidas recomendadas: Reduzir a poluição e controlar a emissão de substâncias alcalinas na água.")

def phBaixo(ph, praia):
    print(f"O pH de {ph} em {praia} é inferior a 7.8, sendo considerado irregular. Algumas consequências desse pH nas águas são:")
    print("- Impacto na Vida Marinha: Muitas espécies marinhas são sensíveis a mudanças no pH, o que pode afetar sua sobrevivência.")
    print("- Ecossistemas de Corais: Os recifes de corais são particularmente sensíveis a mudanças no pH.")
    print("- Fisiologia dos Peixes: O pH alterado pode afetar a respiração e reprodução dos peixes.")
    
def niveis_lixo(lixo, praia):    
    if lixo > 250:
        print(f"A quantidade de lixo no mar perto de {praia_escolha} é extremamente alarmante, atingindo {lixo} toneladas. Isso pode causar sérios problemas ambientais, como:")
        print("- Poluição severa da água: Resíduos podem liberar substâncias altamente tóxicas na água.")
        print("- Mortalidade elevada na Vida Marinha: Muitos animais marinhos podem morrer devido à ingestão de lixo ou emaranhamento.")
        print("- Destruição de Habitats: O excesso de lixo pode destruir habitats críticos de forma irreversível.")
        print("Ações urgentes recomendadas: Implementar programas de limpeza de emergência, promover a reciclagem intensiva e campanhas massivas de conscientização.")
    elif lixo > 180:
        print(f"A quantidade de lixo no mar perto de {praia_escolha} é alarmante, atingindo {lixo} toneladas. Isso pode causar sérios problemas ambientais, como:")
        print("- Poluição da água: Resíduos podem liberar substâncias tóxicas na água.")
        print("- Impacto significativo na Vida Marinha: Animais marinhos podem ingerir ou ficar presos no lixo.")
        print("- Degradação dos Habitats: O excesso de lixo pode destruir habitats críticos.")
        print("Ações recomendadas: Implementar programas de limpeza, promover a reciclagem e conscientizar a população sobre a importância da redução do lixo.")
    elif lixo > 100:
        print(f"A quantidade de lixo no mar perto de {praia_escolha} é preocupante, atingindo {lixo} toneladas. Isso pode causar problemas ambientais, como:")
        print("- Poluição moderada da água: Resíduos podem começar a liberar substâncias tóxicas.")
        print("- Impacto na Vida Marinha: Animais marinhos podem ser afetados pelo lixo presente na água.")
        print("- Degradação gradual dos Habitats: O lixo acumulado pode começar a danificar habitats.")
        print("Ações recomendadas: Realizar campanhas regulares de limpeza, incentivar práticas de reciclagem e educação ambiental.")
    else:
        print(f"A quantidade de lixo no mar perto de {praia_escolha} é de {lixo} toneladas. Embora não seja alarmante, é importante continuar os esforços para manter as águas limpas.")
        print("Sugestões para a preservação: Organizar campanhas de limpeza, incentivar a reciclagem e educar a comunidade sobre a importância de manter os mares livres de lixo.")    
        



def sair_continuar(msg):
    opcoes = ["sim", "não"]
    user = forca_escolha(opcoes,msg)
    if user == "sim":
        return True
    else:
        return False






def peixes_para_mes(mes):
    if mes in ["Janeiro", "Fevereiro"]:
        return ["Tilápia", "Lambari", "Bagre", "Carpa"]
    elif mes in ["Março", "Abril"]:
        return ["Tucunaré", "Dourado", "Curimba", "Pacu"]
    elif mes in ["Maio", "Junho"]:
        return ["Piau", "Pintado", "Jundiá", "Trairão"]
    elif mes in ["Julho", "Agosto"]:    
        return ["Robalo", "Corvina", "Pescada", "Sargo"]
    elif mes in ["Setembro", "Outubro"]:
        return ["Traíra", "Bagre", "Matéria", "Piau"]
    elif mes in ["Novembro", "Dezembro"]:
        return ["Surubim", "Matrinxã", "Piracanjuba", "Tambaqui"]

    
def forca_escolha(lista,msg):
    while True:
        escolha = input(msg)
        if escolha in lista:
            return escolha
        else:
            print("---------------------")
            print("Escolha uma opção válida!")
            print("Opções disponíveis: ", lista)
            
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
escolhas = ["1","2","3"]
praias = ["Boraceia","Itaguaré","Praia do Francês","Taquari","Copacabana","Praia grande"] #
lixo_nas_praias = [200,10,70,80,280,5] # em toneladas
ph_aguas = [6.8,8.1,7.4,7.6,6.1,7.9]

print("Seja Bem vindo a centar de saude do Oceano!")
while True:
    print("---------------------")
    user_escolha = forca_escolha(escolhas,"Digite [1] - Para saber informacões de determinada praia/mar\n [2]-Para saber as os peixes que podem ser pescados em cada epoca do ano \n E digite [3] para sair \n -->")
    if user_escolha == "1":
        praia_escolha = forca_escolha(praias,"Por favor digite uma praia para saber suas informacões: \n -->")
        ph_praia = ph_aguas[my_index(praia_escolha,praias)]
        lixo = lixo_nas_praias[my_index(praia_escolha,praias)]
        if ph_praia > 8.4:
            phAlto(ph_praia,praia_escolha) 
        elif ph_praia < 7.8:
            phBaixo(ph_praia,praia_escolha)
        else:
            print(f"O pH de {ph_praia} está regular, situando-se entre 7.8 e 8.4.")
            
        niveis_lixo(lixo,praia_escolha)
        sair = sair_continuar("Deseja voltar para o menu? Digite [sim] para voltar e [não] para sair: \n --> ")
        if sair:
            continue
        else:
            break
        
    elif user_escolha == "2":
        mes = forca_escolha(meses,"Digite o mes que deseja saber os peixes da epoca: \n -->")
        
        print(f"Os peixes permitidos a pescar no mês de {mes} são:")
        for peixe in peixes_para_mes(mes):
            print(f"- {peixe}")
            
        sair = sair_continuar("Deseja voltar para o menu? Digite [sim] para voltar e [não] para sair: \n --> ")
        if sair:
            continue
        else:
            break
        
    else:
        break
        
print("Obrigado por usar o nosso programa para ajudar o Oceano! Volte sempre para fazer mais pesquisas!")
        
        
    
    
