from utils import cerrar_grabadora, iniciar_grabadora, grabar_audio, generar_timestamp, transcode_audio, decode_transcription, check_there_is_command
from ui import window, state, update_ui, location
import multiprocessing
import threading
import os
import time
from states import StateMachine


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
          if("BRANCH" in ui_command):
            state.set(ui_command.split(" ")[-1])
            update_ui(state.get())
             



if __name__ == "__main__":
    address = "C8:9B:D7:DD:B0:E8"  
    filename = "./temp/grabacion.wav"
    duration = 4

    producer_consumer_thread = threading.Thread(target=producer_consumer)
    
    producer_consumer_thread.start()

    update_ui(state.get())
    window.mainloop()

    exit(0)
