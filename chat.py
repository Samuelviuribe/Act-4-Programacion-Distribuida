#calculator py
import customtkinter as ctk


# Función para procesar la entrada del usuario

def procesar_mensaje(mensaje):
    entrada = mensaje.lower().strip()
    
    if entrada == "salir":
        return "Chat: Para cerrar la app simplemente ciérrala desde la ventana :)"

    # Respuesta hola y gracias
    if "hola" in entrada:
        return "Chat: ¡Hola! Puedo ayudarte con cálculos matemáticos."
    if "gracias" in entrada:
        return "Chat: ¡De nada! 😊"

    # operaciones matematcas
    partes = entrada.split(" ")
    if len(partes) == 3:
        operacion = partes[0]
        try:
            a = float(partes[1])
            b = float(partes[2])
            resultado = 0

            if operacion == "suma":
                resultado = a + b
                return f"Chat: El resultado de la suma es {resultado}"
            elif operacion == "resta":
                resultado = a - b
                return f"Chat: El resultado de la resta es {resultado}"
            elif operacion == "multiplica":
                resultado = a * b
                return f"Chat: El resultado de la multiplicación es {resultado}"
            elif operacion == "divide":
                if b != 0:
                    resultado = a / b
                    return f"Chat: El resultado de la división es {resultado}"
                else:
                    return "Chat: No se puede dividir entre cero."
            elif operacion == "potencia":
                resultado = a ** b
                return f"Chat: El resultado de la potencia es {resultado}"
            else:
                return "Chat: Operación no reconocida. Usa: suma, resta, multiplica, divide, potencia."
        
        except ValueError:
            return "Chat: Escribe números válidos. Ejemplo: suma 3 5"

    return "Chat: No entendí eso. Prueba con: suma 2 3, divide 10 2, potencia 2 4…"


# Interfaz gráfica con CustomTkinter

def enviar_mensaje():
    mensaje = entry.get()
    if mensaje.strip() == "":
        return
    
    chatbox.insert("end", f"Tú: {mensaje}\n")
    
    respuesta = procesar_mensaje(mensaje)
    chatbox.insert("end", f"{respuesta}\n\n")

    entry.delete(0, "end")
    chatbox.see("end")



#ventana principal

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Chat Matemático - CustomTkinter")
app.geometry("500x550")

# Caja de texto del chat
chatbox = ctk.CTkTextbox(app, width=480, height=450, font=("Arial", 14))
chatbox.pack(pady=10)

chatbox.insert("end", "Chat Matemático\nEscribe: suma 4 5, resta 10 3, multiplica 6 7...\nEscribe 'hola' o 'gracias'.\n\n")

# Entry para escribir los mensajes
entry = ctk.CTkEntry(app, placeholder_text="Envia tu mensaje...", width=380)
entry.pack(side="left", padx=10, pady=10)

# Botón enviar
btn = ctk.CTkButton(app, text="Enviar", command=enviar_mensaje)
btn.pack(side="left", pady=10)

app.mainloop()
