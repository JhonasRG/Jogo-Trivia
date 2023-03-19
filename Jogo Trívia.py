import requests
import json
import random

def pegar_questoes():
    url = "https://the-trivia-api.com/api/questions"
    response = requests.get(url)
    if response.status_code == 200:                            
        questions = json.loads(response.text)                   
        return questions
    else:                                                      
        print("Error ao carregar as questões.")
        return None

def perguntar_questoes(questions):          
    print(questions['question'])
    options = [questions['correctAnswer']] + questions['incorrectAnswers']
    random.shuffle(options)
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    answer = input("Diga sua resposta (1-4): ")
    try:
        if options[int(answer)-1] == questions['correctAnswer']:
            print("Correto!")
            return True
        else:
            print("Incorreto.")
            return False
    except IndexError:
        print('Você inseriu um número inválido')

def jogar_jogo():
    questions = pegar_questoes()
    if questions is None:
        return
    score = 0
    num_questions = 10
    for i in range(num_questions):
        print(f"Questão {i+1}:")
        if perguntar_questoes(questions[i]):
            score += 1
    print(f"Você acertou {score} de {num_questions} questões.")
    play_again = input("Deseja jogar novamente? (S/N): ")
    if play_again.lower() == "y":
        jogar_jogo()
    else:
        print("Obrigado Por Jogar!")
        return

jogar_jogo()
