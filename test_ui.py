from ui import state, update_ui, window, subtitles

state.set(0)
subtitles.set("probando")
update_ui(state.get())
window.mainloop()