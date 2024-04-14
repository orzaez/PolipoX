from ui import state, update_ui, window

state.set(15)
update_ui(state.get())
window.mainloop()