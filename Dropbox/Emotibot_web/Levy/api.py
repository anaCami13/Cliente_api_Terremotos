import tkinter as tk
from tkinter import scrolledtext
import requests

def obtener_datos():
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verificar errores en la solicitud
        datos = respuesta.json()
        
        resultados = ""
        for evento in datos["features"]:
            lugar = evento["properties"]["place"]
            magnitud = evento["properties"]["mag"]
            tiempo = evento["properties"]["time"]
            resultados += f"Lugar: {lugar}, Magnitud: {magnitud}, Tiempo: {tiempo}\n"
        
        text_area.delete(1.0, tk.END)  # Limpiar el área de texto
        text_area.insert(tk.END, resultados)  # Mostrar los datos

    except requests.exceptions.RequestException as e:
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, f"Error al obtener datos: {e}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Consulta de Terremotos")
ventana.geometry("600x400")

# Botón para obtener datos
boton = tk.Button(ventana, text="Obtener Datos de Terremotos", command=obtener_datos)
boton.pack(pady=10)

# Área de texto para mostrar los resultados
text_area = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=70, height=20)
text_area.pack(pady=10)
 
# Ejecutar la aplicación
ventana.mainloop()
