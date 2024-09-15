import tkinter as tk
from tkinter import messagebox
import requests
import json

# Carregar configuração do arquivo .json
with open('config.json') as f:
    config = json.load(f)

# Obtendo o API_KEY e BASE_URL do arquivo .json
API_KEY = config['API_KEY']
BASE_URL = config['BASE_URL']

# Obtendo as condições climaticas da cidade especifica
def obter_clima(cidade):
    parametros = {
        'key': API_KEY,
        'q': cidade,
        'lang': 'pt'
    }
    try:
        resposta = requests.get(BASE_URL, params=parametros)
        resposta.raise_for_status() # Lança uma exceção para códigos de status HTTP de erro
        dados = resposta.json()

        if 'error' in dados:
            # Se o código de resposta não for 200, exibe a mensagem de erro
            return None, dados['error']['message'], None
    
        temperatura = dados['current']['temp_c']
        descricao = dados['current']['condition']['text']
        localizacao = f"{dados['location']['name']}, {dados['location']['country']}"
        return temperatura, descricao, localizacao
    except requests.RequestException as e:
        return None, f"Erro na solicitação: {e}", None

# Função para buscar o clima e atualizar a interface gráfica com os dados obtidos
def buscar_clima():
    cidade = entrada_cidade.get()
    temperatura, descricao, localizacao = obter_clima(cidade)

    if temperatura is None:
        messagebox.showerror("Erro", descricao)
        return
    
    label_localizacao.config(text=f"Cidade: {localizacao}")
    label_temperatura.config(text=f"Temperatura: {temperatura:.1f}°C")
    label_descricao.config(text=f"Descrição: {descricao.capitalize()}")

# Criando a interface gráfica
app = tk.Tk()
app.title("Climate System")

# Configurando o layout
tk.Label(app, text="Digite o nome da cidade").pack(pady=5)
entrada_cidade = tk.Entry(app)
entrada_cidade.pack(pady=5)

botao_buscar = tk.Button(app, text="Buscar clima", command=buscar_clima)
botao_buscar.pack(pady=10)

label_localizacao = tk.Label(app, text="Cidade: ")
label_localizacao.pack(pady=5)
label_temperatura = tk.Label(app, text="Temperatura: ")
label_temperatura.pack(pady=5)
label_descricao = tk.Label(app, text="Descrição: ")
label_descricao.pack(pady=5)

# Iniciando o loop da interface 
app.mainloop()



