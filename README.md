# EcoRent — Gestão de Frota de Veículos Elétricos (UC00614)
# Autores: Ana Fundo (8095820), Marcelo Gonçalves (8448175), Nuno Fontes (6742840),
# Data: 13/11/2026 a 23/11/2026

## 📋 Descrição Geral
Plataforma web desenvolvida no âmbito do trabalho prático do módulo **UC00614** (Grupo 1 — Gestão de Frota de Veículos Elétricos), concebida para consolidar competências em desenvolvimento web, estruturação de dados e programação backend num ciclo de desenvolvimento de ~10 horas.

A aplicação simula o portal de monitorização e catálogo da **EcoRent** (empresa fictícia de rent-a-car sustentável sediada na Guarda). O sistema lê os dados dos veículos de um ficheiro **XML** estruturado, valida os valores da bateria, permite filtragem combinada (por marca/modelo e disponibilidade) e apresenta barras de progresso visuais para o estado da bateria de cada viatura.

---

## 🛠️ Tecnologias, Versões e Ferramentas
- **Linguagem:** Python 3 (desenvolvido em Python 3.14)
- **Tecnologias Web e Dados:**
  - **HTML5:** Estruturação semântica das páginas (`index.html`, `frota.html` e `contactos.html`) com motor de templates **Jinja2**.
  - **CSS3:** Estilização responsiva em grelha (*CSS Grid* e *Flexbox*) e renderização das barras visuais de nível de bateria.
  - **XML:** Armazenamento estruturado dos 10 registos da frota (`frota.xml`), cujos nós são ID, marca, modelo, autonomia, nível de bateria, disponibilidade e imagem associada.
- **Bibliotecas e Módulos Python:**
  - **`Flask` (v3+):** Micro-framework web utilizado para configurar o servidor local, gerir o roteamento entre páginas (`/` e rotas secundárias), capturar parâmetros de pesquisa via URL (`request.args`) e injetar os dados processados nos templates HTML (`render_template`).
  - **`Waitress`:** Servidor WSGI (*Web Server Gateway Interface*) utilizado para servir a aplicação Flask em ambiente de produção, permitindo a integração e o encaminhamento de pedidos (*Reverse Proxy*) com o **Apache Server**.
  - **`xml.etree.ElementTree` (Biblioteca nativa do Python):** Módulo responsável por abrir, percorrer (*parse*) e extrair os nós do ficheiro `frota.xml`, convertendo-os em estruturas de dados Python (listas de dicionários).
- **Ambiente / Servidor:** Ambiente Virtual Python (`venv`), Servidor WSGI **Waitress** integrado com **Apache HTTP Server**, Servidor Localhost Flask (`http://127.0.0.1:5000`) e Git/GitHub.
---

## 📅 Histórico de Versões e Datas
| Versão | Data | Descrição / Alterações Efetuadas |
| :--- | :--- | :--- |
| **v1.0.0** | 2026-11-17 | Lançamento da plataforma web funcional da EcoRent: leitura e validação do `frota.xml` via `ElementTree`, 3 páginas interligadas (`index.html`, `frota.html`, `contactos.html`), filtros combinados (pesquisa por marca/modelo e *checkbox* de disponibilidade), imagens por veículo e barras visuais de bateria em CSS3. |

---

## 📂 Estrutura do Repositório
Organização atual dos ficheiros e pastas do projeto:
```text
/UC00614-Projeto/
├── 📁 static/
│   ├── 📁 assets/          # Imagens dos veículos elétricos (.png, .webp)
│   └── 📄 style.css        # Folha de estilos CSS3 da plataforma
├── 📁 templates/
│   ├── 📄 contactos.html   # Página de contactos e localização (Guarda)
│   ├── 📄 frota.html       # Catálogo interativo e monitorização da frota
│   └── 📄 index.html       # Página inicial (Homepage) da EcoRent
├── 📁 venv/                # Ambiente virtual Python (local)
├── 📄 .gitattributes       # Configurações de atributos do Git
├── 📄 .gitignore           # Ficheiros e pastas ignorados no controlo de versões
├── 📄 app.py               # Servidor Flask, rotas, filtros e leitura/validação do XML
├── 📄 frota.xml            # Base de dados estruturada em XML com os registos da frota
├── 📄 wsgi.py              # Ficheiro que indica ao waitress que deve fazer o reverse proxy para o local host:8080
└── 📄 README.md            # Documentação técnica do projeto