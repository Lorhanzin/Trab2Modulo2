candidatos_vaga1 = {}
candidatos_vaga2 = {}
candidatos_aprovados_vaga1 = {}
candidatos_aprovados_vaga2 = {}

def cadastrar_candidato():
    continuar = True
    while continuar:
        nome = input("Digite seu nome: ")
        resumo = input("Faça um breve resumo sobre seu currículo: ")
        vaga = int(input("Selecione a vaga desejada (1 - Desenvolvedor Python, 2 - Analista de Dados): "))
        
        if vaga == 1:
            candidatos_vaga1[nome] = resumo
            if "python" in resumo and "programação" in resumo and "desenvolvimento" in resumo:
                candidatos_aprovados_vaga1[nome] = resumo
        elif vaga == 2:
            candidatos_vaga2[nome] = resumo
            if "análise de dados" in resumo and "dados" in resumo and "sql" in resumo:
                candidatos_aprovados_vaga2[nome] = resumo
        else:
            print("Opção inválida.")
        
        resposta = input("Deseja cadastrar mais um candidato? (s/n): ")
        if resposta.lower() == "n":
            continuar = False
    
    print("Número de candidatos para a vaga 1: ", len(candidatos_vaga1))
    print("Número de candidatos para a vaga 2: ", len(candidatos_vaga2))
    print("Número de candidatos aprovados para a vaga 1: ", len(candidatos_aprovados_vaga1))
    print("Número de candidatos aprovados para a vaga 2: ", len(candidatos_aprovados_vaga2))

cadastrar_candidato()
