import tkinter as tk
from tkinter import messagebox
from BombaGasolina import BombaGasolina
from BombaEtanol import BombaEtanol

bomba_etanol = BombaEtanol(valor_litro=3, quantidade_disponivel=1000)
bomba_gasolina = BombaGasolina(valor_litro=4, quantidade_disponivel=1000)

def abastecer_combustivel(bomba, por_valor, aditivo=False):
    try:
        entrada = float(entry_valor.get() if por_valor else entry_litros.get())
        if por_valor:
            litros = bomba.abastecer_por_valor_com_aditivo(entrada) if aditivo else bomba.abastecer_por_valor(entrada)
            messagebox.showinfo("Abastecido", f"Abastecido {litros:.2f} litros.") if litros > 0 else messagebox.showerror("Erro", "Quantidade insuficiente ou valor inválido.")
        else:
            valor = bomba.abastecer_por_litro_com_aditivo(entrada) if aditivo else bomba.abastecer_por_litro(entrada)
            messagebox.showinfo("Valor", f"Valor a pagar: R${valor:.2f}") if valor > 0 else messagebox.showerror("Erro", "Quantidade insuficiente ou valor inválido.")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor válido.")

janela = tk.Tk()
janela.title("Posto de Combustível")
janela.geometry("400x400")
janela.configure(bg="#f0f0f0")

tk.Label(janela, text="Posto de Combustível", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=10)
frame_entrada = tk.Frame(janela, bg="#ffffff", bd=2, relief="groove")
frame_entrada.pack(padx=20, pady=10, fill="both", expand=True)

tk.Label(frame_entrada, text="Valor (R$):", font=("Arial", 10), bg="#ffffff").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_valor = tk.Entry(frame_entrada, font=("Arial", 10))
entry_valor.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame_entrada, text="Litros:", font=("Arial", 10), bg="#ffffff").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_litros = tk.Entry(frame_entrada, font=("Arial", 10))
entry_litros.grid(row=1, column=1, padx=10, pady=5)

frame_opcoes = tk.Frame(janela, bg="#f0f0f0")
frame_opcoes.pack(pady=20)

opcoes = [
    ("Etanol por Valor", lambda: abastecer_combustivel(bomba_etanol, por_valor=True), "#4CAF50"),
    ("Etanol por Litro", lambda: abastecer_combustivel(bomba_etanol, por_valor=False), "#4CAF50"),
    ("Gasolina por Valor", lambda: abastecer_combustivel(bomba_gasolina, por_valor=True), "#2196F3"),
    ("Gasolina por Litro", lambda: abastecer_combustivel(bomba_gasolina, por_valor=False), "#2196F3"),
    ("Gasolina Aditivada por Valor", lambda: abastecer_combustivel(bomba_gasolina, por_valor=True, aditivo=True), "#FF5722"),
    ("Gasolina Aditivada por Litro", lambda: abastecer_combustivel(bomba_gasolina, por_valor=False, aditivo=True), "#FF5722"),
]

for i, (text, command, color) in enumerate(opcoes):
    tk.Button(frame_opcoes, text=text, command=command, width=20, bg=color, fg="white").grid(row=i//2, column=i%2, padx=5, pady=5)

janela.mainloop()
