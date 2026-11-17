# EcoRent — Gestão de Frota de Veículos Elétricos (UC00614)
# Autores: Ana Fundo, Nuno Fontes, Marcelo Gonçalves
# Data: 13/11/2026 a 17/11/2026

## 📋 Descrição Geral
Plataforma web desenvolvida no âmbito do trabalho prático do módulo **UC00614** (Sala 1 — Gestão de Frota de Veículos Elétricos), concebida para consolidar competências em desenvolvimento web, estruturação de dados e programação backend num ciclo de desenvolvimento de ~10 horas.

A aplicação simula o portal de monitorização e catálogo da **EcoRent** (empresa de rent-a-car sustentável sediada na Guarda), resolvendo a necessidade de apresentar e filtrar em tempo real uma frota de veículos 100% elétricos. O sistema lê os dados diretamente de um ficheiro **XML** estruturado, valida os valores de carga, permite filtragem combinada (por marca/modelo e disponibilidade) e apresenta barras de progresso visuais dinâmicas para o estado da bateria de cada viatura.

---

## 🛠️ Tecnologias, Versões e Ferramentas
- **Linguagem:** Python 3.10+ (desenvolvido em Python 3.14)
- **Tecnologias Web e Dados:**
  - **HTML5:** Estruturação semântica das páginas (`index.html`, `frota.html` e `contactos.html`) com motor de templates **Jinja2**.
  - **CSS3:** Estilização responsiva em grelha (*CSS Grid* e *Flexbox*) e renderização dinâmica das barras visuais de nível de bateria.
  - **XML:** Armazenamento estruturado dos 10 registos da frota (`frota.xml`), incluindo ID, marca, modelo, autonomia, nível de bateria, disponibilidade e imagem associada.
- **Bibliotecas e Módulos Python:**
  - **`Flask` (v3.1+):** Micro-framework web utilizado para configurar o servidor local, gerir o roteamento entre páginas (`/` e rotas secundárias), capturar parâmetros de pesquisa via URL (`request.args`) e injetar os dados processados nos templates HTML (`render_template`).
  - **`xml.etree.ElementTree` (Biblioteca nativa do Python):** Módulo responsável por abrir, percorrer (*parse*) e extrair os nós do ficheiro `frota.xml`, convertendo-os em estruturas de dados Python (listas de dicionários) com tratamento de exceções (`try/except`) e validação de intervalos (`0` a `100%`) para a bateria.
- **Ambiente / Servidor:** Ambiente Virtual Python (`venv`), Servidor Localhost Flask (`http://127.0.0.1:5000`) e Git/GitHub.

---

## 📅 Histórico de Versões e Datas
| Versão | Data | Descrição / Alterações Efetuadas |
| :--- | :--- | :--- |
| **v1.0.0** | 2026-11-13 | Criação do repositório, estruturação do ficheiro `frota.xml` com 10 veículos elétricos e configuração do ambiente virtual com Flask. |
| **v1.1.0** | 2026-11-16 | Implementação da função `lerXML()` com validação de bateria, criação das 3 páginas HTML interligadas, estilização CSS externa e barras visuais de bateria. |
| **v1.2.0** | 2026-11-17 | Adição de filtros combinados (pesquisa por texto e *checkbox* de disponibilidade), integração de imagens individuais por veículo em `static/assets/` e organização final em `frota.html`. |

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
└── 📄 README.md            # Documentação técnica do projeto