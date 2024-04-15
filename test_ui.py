from ui import state, update_ui, window, subtitles

state.set(11)
subtitles.set(11)
update_ui(state.get())
window.mainloop()