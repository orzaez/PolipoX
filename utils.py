import pyaudio
import wave
import pyttsx3
import datetime
from faster_whisper import WhisperModel
import requests


def iniciar_grabadora():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=48000,
                    input=True,
                    frames_per_buffer=1024)
    return p, stream

# def grabar_audio(address, filename, duration, p, stream):
#     wf = wave.open(filename, "wb")
#     wf.setnchannels(2)
#     wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
#     wf.setframerate(96000)

#     for i in range(int(duration * 96000 / 1024)):
#         data = stream.read(1024)
#         wf.writeframes(data)

#     wf.close()

def grabar_audio(address, filename, duration, p, stream):
  wf = wave.open(filename, "wb")
  wf.setnchannels(2)
  wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
  wf.setframerate(48000)

  audio_chunks = []
  
  for i in range(int(duration * 48000 / 1024)):
    data = stream.read(1024)
    if max(data) < 100:
      continue 
    audio_chunks.append(data)

  if not audio_chunks:
    return False

  wf.writeframes(b''.join(audio_chunks))
  wf.close()
  return True

def cerrar_grabadora(p, stream):
    stream.stop_stream()
    stream.close()
    p.terminate()


def generar_timestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    return timestamp

def reproducir_texto(address, text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150) 
    engine.setProperty("volume", 0.75)  

    voice = engine.getProperty('voices')[0]
    engine.setProperty("voice", voice.id)

    engine.say(text)
    engine.runAndWait()

    print(f"Texto reproducido en {address}")

def transcode_audio(filename):
    # model_size = "base"

    # model = WhisperModel(model_size, device="cpu", compute_type="int8")

    # segments, info = model.transcribe(filename, beam_size=1, language="es", vad_filter=True,vad_parameters=dict(min_silence_duration_ms=500))

    # for segment in segments:
    #      return segment.text

    # return "" 
    file = {'audio_file': open(filename, 'rb')}

    # Enviar la petición HTTP al servidor
    response = requests.post('http://ec2-3-254-80-112.eu-west-1.compute.amazonaws.com:8080/transcribe', files=file)

    # Procesar la respuesta
    if response.status_code == 200:
        print(response.json())
        transcribed_text =  response.json()["text"]
        return transcribed_text
    else:
        return ""

def decode_transcription(transcription):  
  cadena_mayusculas = transcription.upper()
  without_sign = cadena_mayusculas.replace(",", "").replace(".","").replace("?","").replace("!","").replace("¿", "").replace("¡", "")
  
  numbers_with_digits = without_sign.replace("INCO", " 5 ").replace("SINCO", "5").replace("UNO", "1").replace("DOS", "2").replace("TRES", "3").replace("CUATRO", "4").replace("CINCO", "5").replace("SEIS", "6").replace("SIETE", "7").replace("OCHO", "8").replace("NUEVE", "9").replace("DIEZ", "10").replace("ONCE", "11").replace("DOCE", "12")

  return " " + numbers_with_digits + " "

def check_there_is_command(command, decoded_transcription):
    return command in decoded_transcription

