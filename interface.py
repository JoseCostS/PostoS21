import tkinter as tk
from tkinter import messagebox
from BombaGasolina import BombaGasolina
from BombaEtanol import BombaEtanol
from BombaDiesel import BombaDiesel  # Importa a classe BombaDiesel

# Instanciando as bombas de combustível
bomba_etanol = BombaEtanol(valor_litro=3, quantidade_disponivel=1000)
bomba_gasolina = BombaGasolina(valor_litro=4, quantidade_disponivel=1000)
bomba_diesel = BombaDiesel(valor_litro=3.5, quantidade_disponivel=1000)  # Diesel

# Função para mostrar a entrada de dados para abastecimento
def mostrar_abastecimento(modo, bomba):
    janela_abastecimento = tk.Toplevel(janela_principal)
    janela_abastecimento.title("Posto de Combustível - Abastecer")
    janela_abastecimento.geometry("400x300")
    janela_abastecimento.configure(bg="#f0f0f0")

    def realizar_abastecimento():
        try:
            entrada = float(entry_dado.get())
            if modo == "valor":
                litros = bomba.abastecer_por_valor(entrada)
                if litros > 0:
                    messagebox.showinfo("Abastecido", f"Abastecido {litros:.2f} litros.")
                else:
                    messagebox.showerror("Erro", "Quantidade insuficiente ou valor inválido.")
            elif modo == "litros":
                valor = bomba.abastecer_por_litro(entrada)
                if valor > 0:
                    messagebox.showinfo("Valor", f"Valor a pagar: R${valor:.2f}")
                else:
                    messagebox.showerror("Erro", "Quantidade insuficiente ou valor inválido.")
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor válido.")

    label_texto = "Insira o valor (R$):" if modo == "valor" else "Insira a quantidade de litros:"
    tk.Label(janela_abastecimento, text=label_texto, font=("Arial", 12), bg="#f0f0f0").pack(pady=20)

    entry_dado = tk.Entry(janela_abastecimento, font=("Arial", 12))
    entry_dado.pack(pady=10)

    tk.Button(janela_abastecimento, text="Abastecer", command=realizar_abastecimento, bg="#4CAF50", fg="white").pack(pady=20)

# Função para criar os botões iniciais de seleção
def criar_botoes_selecao():
    tk.Label(janela_principal, text="Selecione o tipo de combustível", font=("Arial", 14, "bold"), bg="#f0f0f0").pack(pady=20)

    opcoes = [
        ("Etanol por Valor", lambda: mostrar_abastecimento("valor", bomba_etanol)),
        ("Etanol por Litros", lambda: mostrar_abastecimento("litros", bomba_etanol)),
        ("Gasolina por Valor", lambda: mostrar_abastecimento("valor", bomba_gasolina)),
        ("Gasolina por Litros", lambda: mostrar_abastecimento("litros", bomba_gasolina)),
<<<<<<< HEAD
        ("Diesel por Valor", lambda: mostrar_abastecimento("valor", bomba_diesel)),  # Diesel
        ("Diesel por Litros", lambda: mostrar_abastecimento("litros", bomba_diesel)),  # Diesel
=======
        ("Diesel por Valor", lambda: mostrar_abastecimento("valor", bomba_gasolina)),
        ("Diesel por Litros", lambda: mostrar_abastecimento("litros", bomba_gasolina)),
>>>>>>> c65225249685214425530828aa65ce9f3d90e086
    ]

    for text, command in opcoes:
        tk.Button(janela_principal, text=text, command=command, width=30, bg="#2196F3", fg="white").pack(pady=10)

# Configuração inicial da janela principal
janela_principal = tk.Tk()
janela_principal.title("Posto de Combustível")
janela_principal.geometry("400x400")
janela_principal.configure(bg="#f0f0f0")

criar_botoes_selecao()

janela_principal.mainloop()
