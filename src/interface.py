import tkinter as tk
from tkinter import ttk
from emissao_estadual import Emissao
from emissao_federal import Emissao_federal

class Interface_App:
    def __init__(self, janela, janela_estadual, janela_federal):
        self.emissao = Emissao()
        self.emissao_f = Emissao_federal()
        self.tipos_certidoes = [
            "Certidão Judicial Cível",
            "Certidão Judicial Criminal",
            "Certidão Judicial para Fins Eleitorais"
        ]
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
        self.janela_federal = janela_federal
        self.janela.title("Emissor de Certidões")
        self.janela.geometry("300x200")
        self.janela.resizable(False, False)

    def atualizar_lista_historico(self):
        historico = self.emissao.carregar_historico()
        self.mapa_historico = {f"{p['Nome']} - {p['CPF']}": p for p in historico}
        self.historico_box["values"] = list(self.mapa_historico.keys())

    def carregar_pessoa_selecionada(self, event=None):
        chave = self.historico_box.get()
        dados = self.mapa_historico.get(chave)
        if not dados:
            return

        self.nome_entry.delete(0, tk.END)
        self.nome_entry.insert(0, dados["Nome"])

        self.sexo_box.set(dados["Sexo"])

        self.cpf_entry.delete(0, tk.END)
        self.cpf_entry.insert(0, dados["CPF"])

        self.mae_entry.delete(0, tk.END)
        self.mae_entry.insert(0, dados["Mãe"])

        self.pai_entry.delete(0, tk.END)
        self.pai_entry.insert(0, dados["Pai"])

        self.nasc_entry.delete(0, tk.END)
        self.nasc_entry.insert(0, dados["Nascimento"])

        self.nacionalidade_entry.delete(0, tk.END)
        self.nacionalidade_entry.insert(0, dados["Nacionalidade"])

        self.estadocivil_entry.set(dados["Estado Civil"])

        self.rg_entry.delete(0, tk.END)
        self.rg_entry.insert(0, dados["RG"])

        self.orgao_entry.delete(0, tk.END)
        self.orgao_entry.insert(0, dados["Órgão Expedidor"])

        self.uf_entry.delete(0, tk.END)
        self.uf_entry.insert(0, dados["UF"])

        self.endereco_entry.delete(0, tk.END)
        self.endereco_entry.insert(0, dados["Endereço"])
    
    def centralizar_janela(self):
        self.janela.update_idletasks()  
        largura = self.janela.winfo_width()
        altura = self.janela.winfo_height()
        x = (self.janela.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.janela.winfo_screenheight() // 2) - (altura // 2)
        self.janela.geometry(f"+{x}+{y}")

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

            historico_frame = tk.Frame(self.janela_estadual)
            historico_frame.grid(row=11, column=1, sticky="w")

            tk.Label(self.janela_estadual, text="Histórico").grid(row=11, column=0, sticky="w")

            self.historico_box = ttk.Combobox(historico_frame, width=32, state="readonly")
            self.historico_box.pack(side="left")
            self.historico_box.bind("<<ComboboxSelected>>", self.carregar_pessoa_selecionada)

            self.atualizar_lista_historico()

            emitir_frame = tk.Frame(self.janela_estadual)
            emitir_frame.grid(row=12, column=1, sticky="w")

            botao_emitir_estadual = tk.Button(emitir_frame, text="Emitir Documento", font=("Verdana", 11), borderwidth=3, command=lambda: self.emissao.emitir_estadual(self, self.janela_estadual))
            botao_emitir_estadual.pack(padx=20)

    def federal_info(self):
        if self.janela_federal is None or not self.janela_federal.winfo_exists():
            self.janela_federal = tk.Toplevel(self.janela)
            self.janela_federal.resizable(False, False)
            self.janela_federal.title("Certidão Cível Federal")
            self.janela_federal.geometry("400x300")

            x_principal = self.janela.winfo_x()
            y_principal = self.janela.winfo_y()

            self.janela_federal.geometry(f"+{x_principal + 50}+{y_principal + 50}")

            for i in range(4):
                self.janela_federal.columnconfigure(i, weight=1)

            for i in range(10):
                self.janela_federal.rowconfigure(i, weight=1)

            campos = ["CPF:", "Nascimento:"]
            for i, campo in enumerate(campos):
                tk.Label(self.janela_federal, text=campo).grid(row=2+i, column=0, sticky="w")

            self.certidao_box = ttk.Combobox(self.janela_federal, width=32, values=self.tipos_certidoes ,state="readonly")
            self.certidao_box.grid(row=0, column=1, sticky="w")
            self.certidao_box.set(self.tipos_certidoes[0])

            self.cpf2_entry = tk.Entry(self.janela_federal, width=35)
            self.cpf2_entry.grid(row=2, column=1, sticky="w")

            self.nasc2_entry = tk.Entry(self.janela_federal, width=35)
            self.nasc2_entry.grid(row=3, column=1, sticky="w")

            historico_frame = tk.Frame(self.janela_federal)
            historico_frame.grid(row=6, column=1, sticky="w")

            tk.Label(self.janela_federal, text="Histórico").grid(row=6, column=0, sticky="w")

            self.historico_box2 = ttk.Combobox(historico_frame, width=32, state="readonly")
            self.historico_box2.pack(side="left")
            # self.historico_box2.bind("<<ComboboxSelected>>", self.carregar_pessoa_selecionada)

            emitir_frame = tk.Frame(self.janela_federal)
            emitir_frame.grid(row=8, column=1, sticky="w")

            botao_emitir_federal = tk.Button(emitir_frame, text="Emitir Documento", font=("Verdana", 11), borderwidth=3, command=lambda: self.emissao_f.emitir_federal(self, self.janela_federal))
            botao_emitir_federal.pack(padx=20)

janela = tk.Tk()
janela_estadual = None
janela_federal = None
app = Interface_App(janela, janela_estadual, janela_federal)

certidao_estadual_botao = tk.Button(janela, text="Estadual", font=("Verdana", 11), borderwidth=3, command=app.estadual_info)
certidao_estadual_botao.pack(pady=30)

certidao_federal_botao = tk.Button(janela, text="Federal", font=("Verdana", 11), borderwidth=3, command=app.federal_info)
certidao_federal_botao.pack(pady=20)

app.centralizar_janela()
