from ui import state, update_ui, window, subtitles

state.set()
subtitles.set(9)
update_ui(state.get())
window.mainloop()