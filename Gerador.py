import random
import string
import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedTk
from PIL import Image, ImageTk, ImageSequence

def gerar_senha():
    tamanho = tamanho_combobox.get()
    tamanho = int(tamanho)
    caracteres_permitidos = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%&*"
    senha = ''.join(random.choice(caracteres_permitidos) for _ in range(tamanho))
    resultado_label.config(text="Senha gerada: " + senha)
    senha_gerada_temp = senha  # Armazena temporariamente a senha gerada

    # Botão para salvar a senha
    salvar_button = ttk.Button(janela, text="Salvar Senha", command=lambda: salvar_senha(site_app_entry.get(), usuario_email_entry.get(), senha_gerada_temp))
    salvar_button.pack(pady=10)

def salvar_senha(site_app, usuario_email, senha):
    arquivo_salvar = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Arquivos de Texto", "*.txt")])

    if arquivo_salvar:
        with open(arquivo_salvar, "a") as arquivo_saida:
            arquivo_saida.write(f"Site/App: {site_app}\n")
            arquivo_saida.write(f"Usuário/Email: {usuario_email}\n")
            arquivo_saida.write(f"Senha: {senha}\n\n")

# Configuração da janela com o tema personalizado e tamanho padrão
janela = ThemedTk(theme="breeze")
janela.title("Gerador de Senhas VERONEZE")
janela.geometry("400x350")  # Tamanho padrão da janela (largura x altura)

# Rótulo e entrada para o site/app
site_app_label = ttk.Label(janela, text="Site/App:")
site_app_label.pack(pady=10)
site_app_entry = ttk.Entry(janela)
site_app_entry.pack()

# Rótulo e entrada para o usuário/email
usuario_email_label = ttk.Label(janela, text="Usuário/Email:")
usuario_email_label.pack(pady=10)
usuario_email_entry = ttk.Entry(janela)
usuario_email_entry.pack()

# Rótulo e entrada para o tamanho da senha
tamanho_label = ttk.Label(janela, text="Tamanho da senha:")
tamanho_label.pack(pady=10)
tamanho_combobox = ttk.Combobox(janela, values=list(range(8, 21)))
tamanho_combobox.set(12)  # Valor padrão
tamanho_combobox.pack()

# Botão para gerar senha
gerar_button = ttk.Button(janela, text="Gerar Senha", command=gerar_senha)
gerar_button.pack(pady=10)

# Rótulo para exibir a senha gerada
resultado_label = ttk.Label(janela, text="")
resultado_label.pack()

# Iniciar a interface gráfica
janela.mainloop()
