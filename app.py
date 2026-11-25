from flask import Flask, render_template, request
import xml.etree.ElementTree as ET

def lerXML(ficheiro):
    tree = ET.parse(ficheiro)
    root = tree.getroot()
    
    veiculos = []
    
    for item in root:
        veiculo = {}
        for child in item:
            if child.tag == "bateria":
                try:
                    bateria = int(child.text)
                    veiculo["bateria"] = bateria if 0 <= bateria <= 100 else "Fora do intervalo esperado"
                except ValueError: # child.text não é uma string convertível em número
                    veiculo["bateria"] = "NaN"
                except TypeError: # child.text is None
                    veiculo["bateria"] = "N/A"
            elif child.tag == "autonomia":
                try:
                    autonomia = int(child.text)
                    veiculo["autonomia"] = autonomia if autonomia > 0 else "Valor inválido"
                except ValueError: # child.text não é uma string convertível em número
                    veiculo["autonomia"] = "NaN"
                except TypeError: # child.text is None
                    veiculo["bateria"] = "N/A"
            else:
                if child.text is None: # métodos do branch else causam runtime error se child.text is None
                    veiculo[child.tag] = "N/A"
                else:
                    veiculo[child.tag] = " ".join(child.text.split()) if child.text.strip() else "N/A"

        veiculos.append(veiculo)

    return veiculos

# render_template gerar o html baseado no template
app = Flask(__name__, template_folder="templates")
@app.route("/")
def index ():
    return render_template('index.html')

@app.route("/frota")
def frota ():
    veiculos = lerXML("frota.xml")

    # obter texto no input field "pesquisa"
    pesquisa = request.args.get('pesquisa', "").lower().split()
    disponivelFiltro = request.args.get("disponiveis")

    if pesquisa or disponivelFiltro:
        veiculos = [
            v for v in veiculos
                if 
                # Se todas as palavras que compõem a lista pesquisa fazem parte da string obtida juntando marca e modelo.
                # Se pesquisa = [] (caixa de texto "pesquisa" vazia ou só com whitespace), a função all() returns True
                all(palavra in v["marca"].lower() + v["modelo"].lower() for palavra in pesquisa)
                and
                # Se checkbox não marcada, é verdade para todos os veículos
                # Se checkbox marcada, veículo tem de estar disponível
                (not disponivelFiltro or v["disponibilidade"].lower() == "disponível")
        ]
        
        """ 
        veiculosFiltro = []
        for v in veiculos:
            if (not disponivelFiltro or v["disponibilidade"].lower() == "disponível"):
                veiculoTexto = v["marca"].lower() + v["modelo"].lower()
                if all(palavra in veiculoTexto for palavra in pesquisa):
                    veiculosFiltro.append(v)
        veiculos = veiculosFiltro
        """

    return render_template('frota.html', frota = veiculos)

@app.route("/contactos")
def contactos ():
    return render_template('contactos.html')



if __name__ == '__main__':
    app.run(debug=True)