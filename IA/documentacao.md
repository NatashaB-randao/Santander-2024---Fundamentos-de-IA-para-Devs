# Comando por Voz

Este é um script Python que permite ao usuário controlar aplicativos usando comandos de voz.

## Descrição

Este script utiliza a biblioteca SpeechRecognition para reconhecer a fala do usuário e executar ações com base nos comandos detectados.

## Requerimentos

- Python 3.x
- Instalação da biblioteca SpeechRecognition (`pip install SpeechRecognition`)

## Uso

Execute o script e fale os comandos desejados quando solicitado.

## Comandos Disponíveis

- "navegador": Abre o navegador padrão.
- "Excel": Abre o Microsoft Excel.
- "PowerPoint": Abre o Microsoft PowerPoint.
- "Edge": Abre o Microsoft Edge.
- "Fechar": Encerra o programa.

## Funcionamento Interno

O script consiste em uma função `ouvir_microfone()` que habilita o microfone do usuário, captura a fala, utiliza o reconhecedor de fala do Google para converter a fala em texto e executa ações com base nos comandos detectados.

