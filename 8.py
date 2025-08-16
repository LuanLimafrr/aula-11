def calcular_metros_cm():
    metros = float(input('Metros: '))
    centimetros = metros * 100
    print(f'{metros} m = {centimetros} cm')

 

def area_circulo():
    raio = float(input('Informe o raio de um círculo: '))
    area = float((raio ** 2) * 3.14)  # (A = π r²) pi=3,1415
    print(f'Com um círculo de raio {raio} temos um círculo de área {area}.')    


def area_quadrado():
    lado = float(input('Informe  de um quadrado: '))        
    dobro = (lado**2) * 2                   
    area = lado**2  
    print(f'O dobro área do quadrado informado é de {dobro}')



def menu():
    while True:
        print('\n--Menu de opções')
        print('1 - Converter Metros para CM')
        print('2 - Calcular área do Círculo')
        print('3 - Calcular área Quadrado')
        print('0 - Sair')


        try:
            opcao = int(input('Qual opção você deseja: '))
        except ValueError:
            print("Digite um número válido.")
            continue

        if opcao == 0:
            print('Você saiu.')
            break
        elif opcao == 1:
            calcular_metros_cm()
        elif opcao == 2:
            area_circulo()
        elif opcao == 3:
            area_quadrado()
        else:
            print('Digite uma opção correta.')


# Iniciar o menu
menu()