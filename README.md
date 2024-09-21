Explicación del programa:
1.	Interfaz Gráfica:
Utilizamos Tkinter para crear la interfaz gráfica.
La ventana principal incluye un widget TreeView (de ttk) que muestra una lista de eventos con columnas para Fecha, Hora, y Descripción.
Hay campos de entrada para la hora y la descripción, y un DatePicker que utiliza el widget Calendar de la biblioteca tkcalendar para la selección de fechas.
2.	Componentes Avanzados:
Se incluye un DatePicker para la selección de la fecha mediante el widget Calendar de tkcalendar.
Etiquetas para identificar cada campo de entrada.
Los botones ejecutan las acciones de agregar, eliminar y salir.
3.	Manejo de Eventos:
El botón "Agregar Evento" llama a la función agregar_evento, que toma los valores de los campos de entrada y los agrega a la lista de eventos.
El botón "Eliminar Evento Seleccionado" llama a la función eliminar_evento, que elimina el evento seleccionado en el TreeView.
El botón "Salir" cierra la aplicación.
4.	Organización con Contenedores:
Los componentes están organizados dentro de Frames para una estructura más clara.
Cada parte (entrada, botones, visualización de eventos) está separada lógicamente.
