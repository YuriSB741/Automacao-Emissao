# Automação de Emissão de Certidões

Aplicação desktop em Python para auxiliar a emissão de certidões judiciais, com interface gráfica em Tkinter e automação web usando Selenium.

No estado atual, a automação implementada é a emissão de certidão estadual no site do TJRS. A tela de certidão federal já existe na interface, mas a emissão federal é uma semi automação: o sistema preenche os dados e inicia o fluxo, porém o site exige um captcha que precisa ser resolvido manualmente pelo usuário antes da conclusão da emissão.

## Funcionalidades

- Interface gráfica simples para preenchimento dos dados da pessoa consultada
- Automação do navegador para preencher o formulário de certidão estadual do TJRS
- Semi automação para a certidão federal, com intervenção manual no captcha
- Seleção da pasta de destino para download do documento
- Histórico local em JSON para reutilizar dados já preenchidos
- Tela inicial para separar fluxo estadual e federal

## Status do Projeto

- Certidão estadual: implementada
- Certidão federal: semi automatizada, depende de captcha resolvido manualmente
- Histórico: salva e atualiza pessoas por CPF em arquivo local

## Tecnologias

- Python 3
- Tkinter
- Selenium
- Google Chrome

## Pré-requisitos

- Python 3.8 ou superior
- Google Chrome instalado
- Dependências instaladas pelo `requirements.txt`

Versões recentes do Selenium usam o Selenium Manager para gerenciar o driver do navegador automaticamente. Se houver erro relacionado ao ChromeDriver, verifique se o Chrome está atualizado.

## Instalação

1. Clone o repositório:

```bash
git clone <url-do-repositorio>
cd Automacao-Emissao
```

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como Usar

Execute a aplicação a partir da raiz do projeto:

```bash
python3 src/main.py
```

No Windows, se `python3` não estiver disponível:

```bash
python src/main.py
```

Na tela inicial, selecione `Estadual`, preencha os campos obrigatórios e clique em `Emitir Documento`. A aplicação pedirá uma pasta para salvar o arquivo e abrirá o Chrome para preencher o formulário.

## Estrutura

```text
Automacao-Emissao/
├── src/
│   ├── main.py
│   ├── interface.py
│   ├── emissao_estadual.py
│   └── historico_certidoes.json
├── requirements.txt
├── .gitignore
└── README.md
```

## Histórico Local

O arquivo `src/historico_certidoes.json` é gerado localmente para guardar os dados preenchidos e facilitar novas consultas. Ele pode conter dados pessoais, por isso está no `.gitignore` e não deve ser publicado no GitHub.

Exemplo do formato:

```json
[
    {
        "Nome": "JOAO SILVA",
        "Sexo": "Masculino",
        "CPF": "123.456.789-00",
        "Mãe": "MARIA SILVA",
        "Pai": "JOSE SILVA",
        "Nascimento": "01/01/1990",
        "Nacionalidade": "Brasileira",
        "Estado Civil": "Solteiro",
        "RG": "1234567890",
        "Órgão Expedidor": "SSP",
        "UF": "RS",
        "Endereço": "RUA DAS FLORES 123"
    }
]
```

## Observações

- A automação depende da estrutura atual do site do TJRS. Se o site mudar, alguns seletores podem precisar de ajuste.
- Use apenas dados corretos e com finalidade legítima.
- O projeto é um estudo prático de automação, interface gráfica e organização de dados locais.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
