# Automação de Emissão de Certidões

Aplicação desktop automatizada para emissão de certidões civis estaduais e federais, desenvolvida em Python com interface gráfica intuitiva.

## Funcionalidades

- **Interface Gráfica Intuitiva**: Interface desenvolvida com Tkinter para facilitar o uso
- **Automação Web**: Utiliza Selenium para preencher formulários automaticamente no site do TJRS
- **Emissão de Certidões Estaduais**: Automação completa da emissão de certidões civis estaduais
- **Emissão de Certidões Federais**: Estrutura preparada para emissão de certidões federais
- **Histórico de Pessoas**: Armazena dados em JSON para rápido acesso a pessoas já consultadas
- **Download Automático**: Configuração automática do navegador para download direto dos documentos

## Tecnologias Utilizadas

- **Python 3.12.3**: Linguagem principal
- **Selenium 4.45.0**: Automação de navegador web
- **Tkinter**: Interface gráfica
- **Chrome WebDriver**: Driver para automação do Chrome

## Pré-requisitos

- Python 3.8 ou superior
- Google Chrome instalado
- ChromeDriver compatível com sua versão do Chrome

## Instalação

1. **Clone o repositório**
   ```bash
   git clone <seu-repositorio>
   cd Automa-o-Emiss-o
   ```

2. **Crie um ambiente virtual** (opcional, mas recomendado)
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate  # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

## Como Usar

1. **Inicie a aplicação**
   ```bash
   python main.py
   ```

2. **Na interface principal**, escolha:
   - **Estadual**: Para emitir certidão cível estadual
   - **Federal**: Para emitir certidão cível federal

3. **Preencha os dados** solicitados na janela:
   - Nome
   - Sexo (Masculino/Feminino)
   - CPF
   - Nome da Mãe
   - Nome do Pai
   - Data de Nascimento (dd/mm/aaaa)
   - Nacionalidade
   - Estado Civil
   - RG/Órgão Expedidor/UF
   - Endereço

4. **Selecione uma pasta** para salvar o documento quando solicitado

5. **A automação fará o resto!** O navegador abrirá automaticamente e preencherá todos os campos

## Estrutura do Projeto

```
Automa-o-Emiss-o/
├── main.py                 # Ponto de entrada da aplicação
├── interface.py            # Interface gráfica (Tkinter)
├── emissao_estadual.py     # Lógica de automação das certidões estaduais
├── historico_certidoes.json # Histórico de pessoas (gerado automaticamente)
├── requirements.txt        # Dependências do projeto
└── README.md              # Este arquivo
```

## Fluxo da Aplicação

1. **interface.py** - Exibe a interface gráfica para coleta de dados
2. **emissao_estadual.py** - Valida os dados e automatiza o preenchimento no site
3. **historico_certidoes.json** - Armazena dados para consultas futuras

## Dados Armazenados

Os dados das pessoas consultadas são armazenados automaticamente em `historico_certidoes.json`:

```json
{
    "Nome": "João Silva",
    "Sexo": "Masculino",
    "CPF": "123.456.789-00",
    "Mãe": "Maria Silva",
    "Pai": "Jose Silva",
    "Nascimento": "01/01/1990",
    "Nacionalidade": "Brasileira",
    "Estado Civil": "Solteiro",
    "RG": "1234567890",
    "Órgão Expedidor": "SSP",
    "UF": "RS",
    "Endereço": "Rua das Flores 123"
}
```

## Configuração de Download

A aplicação configura automaticamente o Chrome para:
- Salvar downloads no diretório especificado pelo usuário
- Desabilitar prompts de download
- Abrir PDFs externamente

## Troubleshooting

- **ChromeDriver não encontrado**: Certifique-se que o ChromeDriver está no PATH ou na pasta do projeto
- **Timeout ao carregar página**: Aumente o tempo de espera em `WebDriverWait`
- **Campos não preenchidos**: Verifique se os seletores XPATH ainda correspondem ao site do TJRS

## Licença

Este projeto é de uso pessoal. Modificações e distribuições devem respeitar as limitações de acesso ao site do TJRS.

## Aviso Legal

Esta ferramenta é destinada a automatizar processos legais. O usuário é responsável por:
- Garantir que possua os dados corretos das pessoas
- Cumprir as regulamentações legais aplicáveis
- Utilizar apenas para fins legítimos

---

**Desenvolvido em Python**
