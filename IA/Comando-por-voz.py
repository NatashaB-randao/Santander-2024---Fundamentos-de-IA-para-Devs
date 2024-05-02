print('testando...')

import speech_recognition as sr
import os

def ouvir_microfone():
    """
    Função para ouvir e reconhecer a fala do usuário.
    """
    # Habilita o microfone do usuário
    microfone = sr.Recognizer()

    # Usando o microfone
    with sr.Microphone() as source:
        # Chama um algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)

        # Solicitação para o usuário falar algo
        print('Diga alguma coisa: ')

        # Armazena o que foi dito numa variável
        audio = microfone.listen(source)

    try:
        # Converte a fala em texto usando o reconhecedor do Google
        frase = microfone.recognize_google(audio, language='pt-BR')

        # Verifica se determinadas palavras-chave estão presentes na frase
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
            # Retorna True para sinalizar que o programa deve ser encerrado
            return True

        # Retorna a frase reconhecida
        return frase

    except sr.UnknownValueError:
        print('Não consegui entender o que você disse.')

    except sr.RequestError as e:
        print('Não foi possível acessar o serviço de reconhecimento de fala:', e)

# Função principal para execução do código
if __name__ == "__main__":
    # Chama a função para ouvir o microfone
    while True:
        if ouvir_microfone():
            break  # Sai do loop se a função retornar True (quando 'Fechar' é detectado)
