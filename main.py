from openai import OpenAI
import os.path, time

#Ler api.txt e armazenar em uma variável
with open('api.txt', 'r') as file:
    api = file.read().replace('\n', '')
    api = str(api)

#Lendo um arquivo de texto e armazenando em uma variável
with open('texto.txt', 'r') as file:
    texto = file.read().replace('\n', '')
    texto = str(texto)

#Instanciar a classe OpenAI
client = OpenAI(api_key=api)

#Criar um arquivo de áudio com o texto
speech_file_path = 'audio.mp3'

#Verificar se arquivo audio.mp3 existe e foi atualizado nas ultimas 24 horas

if os.path.isfile(speech_file_path) and time.time() - os.path.getmtime(speech_file_path) < 24 * 3600:
    print("Arquivo audio.mp3 existe e foi atualizado nas últimas 24 horas")

else:
    #Criar o arquivo de áudio
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=texto
    )
    response.stream_to_file(speech_file_path)

