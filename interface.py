import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from emissao_estadual import Emissao

class Interface_App:
    def __init__(self, janela, janela_estadual):
        self.emissao = Emissao()
        self.generos = [
            "Masculino", 
            "Feminino"
            ]
        self.estados = [
            "Casado", 
            "Companheiro", 
            "Desquitado", 
            "Divorciado", 
            "Outros", 
            "Sep Consensualmente", 
            "Sep Judicialmente", 
            "Separado",
            "Solteiro", 
            "União Estável", 
            "Viúvo"
            ]
        self.janela = janela
        self.janela_estadual = janela_estadual
        self.janela_federal = None
        self.janela.title("Emissor de Certidões")
        self.janela.geometry("300x200")
        self.janela.resizable(False, False)

    def centralizar_janela(self):
        self.janela.update_idletasks()  
        largura = janela.winfo_width()
        altura = janela.winfo_height()
        x = (janela.winfo_screenwidth() // 2) - (largura // 2)
        y = (janela.winfo_screenheight() // 2) - (altura // 2)
        janela.geometry(f"+{x}+{y}")

    def estadual_info(self):
        if self.janela_estadual is None or not self.janela_estadual.winfo_exists():
            self.janela_estadual = tk.Toplevel(self.janela)
            self.janela_estadual.resizable(False, False)
            self.janela_estadual.title("Certidão Cível Estadual")
            self.janela_estadual.geometry("400x500")

            x_principal = self.janela.winfo_x()
            y_principal = self.janela.winfo_y()

            self.janela_estadual.geometry(f"+{x_principal + 50}+{y_principal + 50}")

            for i in range(6):
                self.janela_estadual.columnconfigure(i, weight=1)

            for i in range(15):
                self.janela_estadual.rowconfigure(i, weight=1)

            campos = [
                    "Nome",
                    "Sexo",
                    "CPF",
                    "Nome da mãe",
                    "Nome do pai",
                    "(dd/mm/aaaa)",
                    "Nacionalidade",
                    "Estado Civil",
                    "RG/Órgão/UF",
                    "Endereço"
                ]
            for i, campo in enumerate(campos):
                tk.Label(self.janela_estadual, text=campo).grid(row=i, column=0, sticky="w")

            self.nome_entry = tk.Entry(self.janela_estadual, width=35)
            self.nome_entry.grid(row=0, column=1, sticky="e")

            self.sexo_box = ttk.Combobox(self.janela_estadual, width=32, values=self.generos ,state="readonly")
            self.sexo_box.grid(row=1, column=1, sticky="e")
            self.sexo_box.set(self.generos[0])

            self.cpf_entry = tk.Entry(self.janela_estadual, width=35)
            self.cpf_entry.grid(row=2, column=1, sticky="e")

            self.mae_entry = tk.Entry(self.janela_estadual, width=35)
            self.mae_entry.grid(row=3, column=1, sticky="e")

            self.pai_entry = tk.Entry(self.janela_estadual, width=35)
            self.pai_entry.grid(row=4, column=1, sticky="e")

            self.nasc_entry = tk.Entry(self.janela_estadual, width=35)
            self.nasc_entry.grid(row=5, column=1, sticky="e")

            self.nacionalidade_entry = tk.Entry(self.janela_estadual, width=35)
            self.nacionalidade_entry.grid(row=6, column=1, sticky="e")

            self.estadocivil_entry = ttk.Combobox(self.janela_estadual, width=32, values=self.estados, state="readonly")
            self.estadocivil_entry.grid(row=7, column=1, sticky="e")
            self.estadocivil_entry.set(self.estados[8])

            self.endereco_entry = tk.Entry(self.janela_estadual, width=35)
            self.endereco_entry.grid(row=9, column=1, sticky="e")

            # Frame para ajustar a posição dos entrys do RG
            rg_frame = tk.Frame(self.janela_estadual)
            rg_frame.grid(row=8, column=1, sticky="w")

            self.rg_entry = tk.Entry(rg_frame, width=12)
            self.rg_entry.pack(side="left")

            tk.Label(rg_frame, text="/").pack(side="left", padx=(4, 0))

            self.orgao_entry = tk.Entry(rg_frame, width=8)
            self.orgao_entry.pack(side="left", padx=(4, 0))

            tk.Label(rg_frame, text="/").pack(side="left", padx=(4, 0))

            self.uf_entry = tk.Entry(rg_frame, width=3)
            self.uf_entry.pack(side="left", padx=(4, 0))

            emitir_frame = tk.Frame(self.janela_estadual)
            emitir_frame.grid(row=12, column=1, sticky="w")

            botao_emitir_estadual = tk.Button(emitir_frame, text="Emitir Documento", font=("Verdana", 11), borderwidth=3, command=lambda: self.emissao.emitir_estadual(self, self.janela_estadual))
            botao_emitir_estadual.pack(padx=20)

    def federal_info(self):
        if self.janela_federal is None or not self.janela_federal.winfo_exists():
            self.janela_federal = tk.Toplevel(self.janela)
            self.janela_federal.resizable(False, False)
            self.janela_federal.title("Certidão Cível Federal")
            self.janela_federal.geometry("400x500")

            x_principal = self.janela.winfo_x()
            y_principal = self.janela.winfo_y()

            self.janela_federal.geometry(f"+{x_principal + 50}+{y_principal + 50}")

janela = tk.Tk()
janela_estadual = None
app = Interface_App(janela, janela_estadual)

certidao_estadual_botao = tk.Button(janela, text="Estadual", font=("Verdana", 11), borderwidth=3, command=app.estadual_info)
certidao_estadual_botao.pack(pady=30)

certidao_federal_botao = tk.Button(janela, text="Federal", font=("Verdana", 11), borderwidth=3, command=app.federal_info)
certidao_federal_botao.pack(pady=20)

app.centralizar_janela()
