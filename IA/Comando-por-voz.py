print('testando...')

import speech_recognition as sr
import os

def ouvir_microfone():
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # Usando o microfone
    with sr.Microphone() as source:
        # Chama um algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuário dizer
        print('Diga alguma coisa: ')

        # Armazena o que foi dito numa variável
        audio = microfone.listen(source)

    try:
        # Passa a variável para o algoritmo reconhecedor de padrões 
        frase = microfone.recognize_google(audio, language='pt-BR')

        if 'navegador' in frase:
            os.system('start Chrome.exe')
            return False
        
        elif 'Excel' in frase:
            os.system('start Excel.exe')
            return False
        
        elif 'PowerPoint' in frase:
            os.system('start POWERPNT.exe')
            return False
        
        elif 'Edge' in frase:
            os.system('start msedge.exe')
            return False
        
        elif 'Fechar' in frase:
            return True

        # Retorna a frase pronunciada
        return frase

    except sr.UnknownValueError:
        print('Não entendi o que você disse.')

    except sr.RequestError as e:
        print('Não foi possível acessar o serviço de reconhecimento de fala:', e)

# Chama a função para ouvir o microfone
ouvir_microfone()
