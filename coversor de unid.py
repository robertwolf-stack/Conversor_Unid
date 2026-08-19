import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class ConversorUnidades:
    def __init__(self, root):
        self.root = root

        # =========================
        # CONFIGURAÇÃO DA JANELA
        # =========================

        root.title("Conversor de Unidades")
        root.geometry("500x500")
        root.resizable(False, False)
        root.configure(bg="black")

        # =========================
        # TÍTULO
        # =========================

        titulo = tk.Label(
            root,
            text="Conversor de Unidades",
            font=("Arial", 22, "bold"),
            bg="black",
            fg="white"
        )
        titulo.pack(pady=20)

        subtitulo = tk.Label(
            root,
            text="Temperatura e distância",
            font=("Arial", 11),
            bg="black",
            fg="white"
        )
        subtitulo.pack()

        # =========================
        # RELÓGIO
        # =========================

        self.relogio = tk.Label(
            root,
            text="",
            font=("Arial", 18, "bold"),
            bg="black",
            fg="white"
        )
        self.relogio.pack(pady=15)

        self.atualizar_relogio()

        # =========================
        # TIPO DE CONVERSÃO
        # =========================

        tk.Label(
            root,
            text="Tipo de conversão:",
            font=("Arial", 11, "bold"),
            bg="black",
            fg="white"
        ).pack()

        self.tipo = ttk.Combobox(
            root,
            values=[
                "Celsius → Fahrenheit",
                "Celsius → Kelvin",
                "Quilômetros → Milhas"
            ],
            state="readonly",
            width=27
        )
        self.tipo.pack(pady=8)
        self.tipo.current(0)

        # =========================
        # VALOR
        # =========================

        tk.Label(
            root,
            text="Digite o valor:",
            font=("Arial", 11, "bold"),
            bg="black",
            fg="white"
        ).pack(pady=5)

        self.entrada = tk.Entry(
            root,
            font=("Arial", 14),
            justify="center",
            width=20,
            bg="#1a1a1a",
            fg="white",
            insertbackground="white",
            relief="solid",
            bd=1
        )
        self.entrada.pack(pady=5)

        # =========================
        # BOTÃO
        # =========================

        botao = tk.Button(
            root,
            text="CONVERTER",
            font=("Arial", 11, "bold"),
            command=self.converter,
            width=20,
            bg="#333333",
            fg="white",
            activebackground="#555555",
            activeforeground="white",
            relief="flat",
            cursor="hand2"
        )
        botao.pack(pady=20)

        # =========================
        # RESULTADO
        # =========================

        self.resultado = tk.Label(
            root,
            text="Resultado: --",
            font=("Arial", 15, "bold"),
            bg="black",
            fg="white"
        )
        self.resultado.pack(pady=10)

        # Pressionar ENTER converte
        root.bind("<Return>", lambda event: self.converter())

    # =========================
    # RELÓGIO
    # =========================

    def atualizar_relogio(self):

        agora = datetime.now()

        horario = agora.strftime("%H:%M:%S")
        data = agora.strftime("%d/%m/%Y")

        self.relogio.config(
            text=f"{data}  |  {horario}"
        )

        # Atualiza a cada 1 segundo
        self.root.after(1000, self.atualizar_relogio)

    # =========================
    # CONVERSÃO
    # =========================

    def converter(self):

        try:
            valor = float(self.entrada.get())

            tipo = self.tipo.get()

            if tipo == "Celsius → Fahrenheit":

                resultado = (valor * 9 / 5) + 32

                self.resultado.config(
                    text=f"Resultado: {resultado:.2f} °F"
                )

            elif tipo == "Celsius → Kelvin":

                resultado = valor + 273.15

                self.resultado.config(
                    text=f"Resultado: {resultado:.2f} K"
                )

            elif tipo == "Quilômetros → Milhas":

                resultado = valor * 0.621371

                self.resultado.config(
                    text=f"Resultado: {resultado:.2f} milhas"
                )

        except ValueError:

            messagebox.showerror(
                "Erro",
                "Digite um valor numérico válido."
            )


# =========================
# EXECUÇÃO
# =========================

if __name__ == "__main__":

    root = tk.Tk()

    app = ConversorUnidades(root)

    root.mainloop()