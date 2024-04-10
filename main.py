import bluetooth
import pyaudio
import wave
import pyttsx3

def get_device_name(address):
    try:
        name = bluetooth.lookup_name(address)
    except bluetooth.BluetoothError:
        name = "Desconocido"
    return name

def grabar_audio(address, filename, duration):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=2,
                    rate=96000,
                    input=True,
                    frames_per_buffer=1024)

    wf = wave.open(filename, "wb")
    wf.setnchannels(2)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(96000)

    for i in range(int(duration * 96000 / 1024)):
        data = stream.read(1024)
        wf.writeframes(data)

    wf.close()
    stream.stop_stream()
    stream.close()
    p.terminate()

    print(f"Grabación de audio de {address} finalizada. Guardada como {filename}")



def reproducir_texto(address, text):
    # Configurar pyttsx3
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)  # Ajustar la velocidad de habla
    engine.setProperty("volume", 0.75)  # Ajustar el volumen

    voice = engine.getProperty('voices')[0]
    # Seleccionar el dispositivo de salida Bluetooth por MAC
    engine.setProperty("voice", voice.id)

    # Reproducir el texto
    engine.say(text)
    engine.runAndWait()

    print(f"Texto reproducido en {address}")

def reproducir_audio(archivo):
    # Abrir el archivo de audio
    wf = wave.open(archivo, 'rb')

    # Configurar el stream de audio
    p = pyaudio.PyAudio()
    stream = p.open(format=wf.getsampwidth(),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    # Leer y reproducir el audio
    data = wf.readframes(chunk_size)
    while data:
        stream.write(data)
        data = wf.readframes(chunk_size)

    # Cerrar el stream y el archivo de audio
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()

def configurar_salida_audio(mac_address):
    # Conectarse al dispositivo Bluetooth
    client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_socket.connect((mac_address, 1))

    # Enviar comando para configurar la salida de audio
    comando = "A2DP_SINK_START"
    client_socket.send(comando.encode())

    # Cerrar el socket
    client_socket.close()

    # Desconfigurar la entrada de audio, si está configurada
    desconfigurar_entrada_audio(mac_address)

    print(f"Salida de audio configurada en {mac_address}")

def desconfigurar_salida_audio(mac_address):
    """
    Desconfigura el dispositivo Bluetooth con la dirección MAC proporcionada como salida de audio.
    """

    # Conectarse al dispositivo Bluetooth
    client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_socket.connect((mac_address, 1))

    # Enviar comando para desconfigurar la salida de audio
    comando = "A2DP_SINK_STOP"
    client_socket.send(comando.encode())

    # Cerrar el socket
    client_socket.close()

    print(f"Salida de audio desconfigurada en {mac_address}")
def configurar_entrada_audio(mac_address):
    """
    Configura el dispositivo Bluetooth con la dirección MAC proporcionada como entrada de audio.
    """

    # Conectarse al dispositivo Bluetooth
    client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_socket.connect((mac_address, 1))

    # Enviar comando para configurar la entrada de audio
    comando = "HFP_HF_START"
    client_socket.send(comando.encode())

    # Cerrar el socket
    client_socket.close()

    # Desconfigurar la salida de audio, si está configurada
    desconfigurar_salida_audio(mac_address)

    print(f"Entrada de audio configurada en {mac_address}")
def desconfigurar_entrada_audio(mac_address):
    """
    Desconfigura el dispositivo Bluetooth con la dirección MAC proporcionada como entrada de audio.
    """

    # Conectarse al dispositivo Bluetooth
    client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    client_socket.connect((mac_address, 1))

    # Enviar comando para desconfigurar la entrada de audio
    comando = "HFP_HF_STOP"
    client_socket.send(comando.encode())

    # Cerrar el socket
    client_socket.close()

    print(f"Entrada de audio desconfigurada en {mac_address}")



address = "C8:9B:D7:DD:B0:E8"  
filename = "./temp/grabacion.wav"
duration = 10

# desconfigurar_salida_audio(address)
# configurar_entrada_audio(address)
grabar_audio(address, filename, duration)

from faster_whisper import WhisperModel

model_size = "tiny"

# Run on GPU with FP16
# model = WhisperModel(model_size, device="cuda", compute_type="float16")

# or run on GPU with INT8
# model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
model = WhisperModel(model_size, device="cpu", compute_type="int8")

segments, info = model.transcribe("grabacion.wav", beam_size=5)

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
# desconfigurar_entrada_audio(address)
# configurar_salida_audio(address)
# reproducir_texto(address,  "Bienvenidos a este tutorial, hoy instalaremos camtasia studio 100 por 100 free 1 link mega")
