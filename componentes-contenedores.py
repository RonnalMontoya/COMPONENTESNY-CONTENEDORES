import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar

# Función para agregar un nuevo evento
def agregar_evento():
    fecha = calendario.get_date()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if not (fecha and hora and descripcion):
        messagebox.showwarning("Campos vacíos", "Todos los campos son obligatorios.")
        return

    # Insertar el evento en el TreeView
    tree.insert("", "end", values=(fecha, hora, descripcion))

    # Limpiar los campos de entrada
    entry_hora.delete(0, tk.END)
    entry_descripcion.delete(0, tk.END)

# Función para eliminar el evento seleccionado
def eliminar_evento():
    try:
        selected_item = tree.selection()[0]
        tree.delete(selected_item)
    except IndexError:
        messagebox.showwarning("Selecciona un evento", "Debes seleccionar un evento para eliminar.")

# Función para cerrar la aplicación
def salir():
    root.quit()

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("700x600")

# Frame para el calendario y la entrada de hora y descripción
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=20)

# Widget de selección de fecha (DatePicker) usando Calendar de tkcalendar
calendario = Calendar(frame_entrada, selectmode='day', date_pattern='dd/mm/yyyy')
calendario.grid(row=0, column=0, padx=10, pady=10)

# Etiquetas y campos de entrada
tk.Label(frame_entrada, text="Hora (HH:MM):").grid(row=0, column=1, padx=10)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=0, column=2, padx=10)

tk.Label(frame_entrada, text="Descripción:").grid(row=1, column=1, padx=10)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=1, column=2, padx=10)

# Frame para los botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

# Botón para agregar un evento
btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

# Botón para eliminar un evento
btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

# Botón para salir de la aplicación
btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=10)

# Frame para el TreeView (mostrar eventos)
frame_eventos = tk.Frame(root)
frame_eventos.pack(pady=20)

# Crear el TreeView para mostrar los eventos
tree = ttk.Treeview(frame_eventos, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Configuración final de la ventana principal
root.mainloop()
