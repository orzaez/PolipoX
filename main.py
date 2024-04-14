from utils import cerrar_grabadora, iniciar_grabadora, grabar_audio, generar_timestamp, transcode_audio, decode_transcription
from ui import window, state, update_ui, location, size_x, mucosal_pattern_nice, mucosal_pattern_jnet, lesion_type, paris_classification, num_fragments, resection_method, subtitles
import multiprocessing
import threading
import os
import time
from states import StateMachine
import re

cola = multiprocessing.Queue()
ui_queue = multiprocessing.Queue()
signal_event = multiprocessing.Event()

def producer():
  p, stream = iniciar_grabadora()
  try:
    while True:
      timestamp = generar_timestamp()
      not_empty = grabar_audio(address, "./temp/" + timestamp + ".wav", duration, p, stream)
      if not_empty:
        cola.put("./temp/" + timestamp + ".wav")
      else:
        os.remove("./temp/" + timestamp + ".wav")

      if not signal_event.is_set():
        signal_event.set()

  except KeyboardInterrupt:
     cerrar_grabadora(p, stream)



def consumer():
  pid = os.getpid()
  os.system("sudo renice -n -19 -p " + str(pid))
  state_machine = StateMachine()

  while True:
    if not cola.empty():
      filename = cola.get()
      transcription = transcode_audio(filename)
      os.remove(filename)
      decoded_transcription = decode_transcription(transcription)
      there_is_command, commands = state_machine.check_command(decoded_transcription)
      if(there_is_command):
        while not cola.empty():
          filename = cola.get()
          os.remove(filename)

        for command in commands:
          ui_queue.put(command)

      ui_queue.put(f"""SET_SUBTITLES {decoded_transcription}""")
    else:
       signal_event.wait()
       signal_event.clear()

def producer_consumer():
    hilo_consumidor = multiprocessing.Process(target=consumer)
    hilo_productor = multiprocessing.Process(target=producer)
  
    hilo_consumidor.start()
    hilo_productor.start()

    while True:
        if not ui_queue.empty():
          ui_command = ui_queue.get()
          print(ui_command)
          if(ui_command == "NEXT_STATE"):
            state.set(state.get() + 1)
            update_ui(state.get())
          if("SET_LOCATION" in ui_command):
            location.set(ui_command.split(" ")[-1])
            update_ui(state.get())

          if("SET_SUBTITLES" in ui_command):
            subtitles.set(re.sub(r"\A\w+\s", "", ui_command))
            update_ui(state.get())
            
          if("SET_SIZE_X" in ui_command):
            size_x.set(ui_command.split(" ")[-1])
            update_ui(state.get())

          if("SET_NICE" in ui_command):
            mucosal_pattern_nice.set(ui_command.split(" ")[-1])
            update_ui(state.get())

          if("SET_JNET" in ui_command):
            mucosal_pattern_jnet.set(ui_command.split(" ")[-1])
            update_ui(state.get())

          if("SET_LESION" in ui_command):
            lesion = "Pólipo sesil" if ui_command.split(" ")[-1] == "1" else "Lesión de extensión lateral (LST)"
            lesion_type.set(lesion)
            update_ui(state.get())

          if("SET_NUM_FRAGMENTS" in ui_command):
            num_fragments.set(ui_command.split(" ")[-1])
            update_ui(state.get())

          if("SET_PARIS" in ui_command):
            argument = ui_command.split(" ")[-1]
            paris = "-"

            if argument == "1":
              paris = "0-Is"
            elif argument == "2":
              paris = "0-Ip"
            elif argument == "3":
              paris = "0-Isp"
            elif argument == "4":
              paris = "0-IIa"
            elif argument == "5":
              paris = "0-IIb"
            elif argument == "6":
              paris = "0-IIc"
            elif argument == "7":
              paris = "mixto 0-IIa+Is"
            elif argument == "8":
              paris = "mixto 0-IIb+Is"
            elif argument == "9":
              paris = "mixto 0-IIc+Is"
            elif argument == "10":
              paris = "mixto 0-IIa+IIc"
            elif argument == "11":
              paris = "mixto 0-IIb+IIc"

            paris_classification.set(paris)
            update_ui(state.get())

          if("SET_RESECTION_METHOD" in ui_command):
            argument = ui_command.split(" ")[-1]
            resection_method_argument = "-"

            if argument == "1":
              resection_method_argument = "Pinza fría"
            elif argument == "2":
              resection_method_argument = "Asa fría"
            elif argument == "3":
              resection_method_argument = "Inyección y asa caliente"
            elif argument == "4":
              resection_method_argument = "Precorte"

            resection_method.set(resection_method_argument)
            update_ui(state.get())

          if("BRANCH" in ui_command):
            state.set(ui_command.split(" ")[-1])
            update_ui(state.get())

          if("SEND_DATA" in ui_command):
            print("ENVIANDO DATAPACK")
             



if __name__ == "__main__":
    address = "C8:9B:D7:DD:B0:E8"  
    filename = "./temp/grabacion.wav"
    duration = 4

    producer_consumer_thread = threading.Thread(target=producer_consumer)
    
    producer_consumer_thread.start()

    update_ui(state.get())
    window.mainloop()

    exit(0)
