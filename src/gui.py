import tkinter as tk
from tkinter import messagebox
import threading
from automacao import executar_perda_colisao, executar_estelionato, stop_program

def iniciar_programa() -> None:
    global stop_program
    stop_program = False
    iniciar_btn.pack_forget()
    terminar_btn.pack(pady=20)
    opcao = var_opcao.get()
    if opcao == 1:
        threading.Thread(target=executar_perda_colisao).start()
    elif opcao == 2:
        threading.Thread(target=executar_estelionato).start()
    else:
        messagebox.showwarning("Opção Inválida", "Por favor, selecione uma opção válida.")

def terminar_programa() -> None:
    global stop_program
    stop_program = True
    terminar_btn.pack_forget()
    iniciar_btn.pack(pady=20)

# Interface gráfica
root = tk.Tk()
root.title("Despacho Automático")
root.geometry("400x300")

import os
import tkinter as tk

# Obtém o diretório atual do arquivo sendo executado
current_dir = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para a imagem
image_path = os.path.join(current_dir, 'assets', 'policia.png')

# Define o ícone da janela
root.iconphoto(True, tk.PhotoImage(file=image_path))
root.configure(bg="#344955")

# Título
title = tk.Label(root, text="Despacho Automático", font=("Helvetica", 18, 'bold'), fg="#F9AA33", bg="#344955")
title.pack(pady=20)

# Opções
var_opcao = tk.IntVar()

frame_opcoes = tk.Frame(root, bg="#344955")
frame_opcoes.pack(pady=10)

tk.Radiobutton(frame_opcoes, text="Perda-Colisão", variable=var_opcao, value=1, font=("Helvetica", 14), fg="white", bg="#344955", selectcolor="#4A6572").pack(anchor='w', pady=5)
tk.Radiobutton(frame_opcoes, text="Estelionato", variable=var_opcao, value=2, font=("Helvetica", 14), fg="white", bg="#344955", selectcolor="#4A6572").pack(anchor='w', pady=5)

# Botões
iniciar_btn = tk.Button(root, text="Iniciar", command=iniciar_programa, font=("Helvetica", 14), bg="#4CAF50", fg="white", width=15)
iniciar_btn.pack(pady=20)

terminar_btn = tk.Button(root, text="Terminar", command=terminar_programa, font=("Helvetica", 14), bg="#F44336", fg="white", width=15)

root.mainloop()
