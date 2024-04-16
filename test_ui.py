from ui import state, update_ui, window, subtitles

state.set(8)
subtitles.set(2)
update_ui(state.get())
window.mainloop()