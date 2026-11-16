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
                except ValueError:
                    veiculo["bateria"] = "NaN"
            elif child.tag == "autonomia":
                try:
                    autonomia = int(child.text)
                    veiculo["autonomia"] = autonomia if autonomia > 0 else "Valor inválido"
                except ValueError:
                    veiculo["autonomia"] = "NaN"
            else: 
                veiculo[child.tag] = child.text

        veiculos.append(veiculo)

    return veiculos

# render_template para ligar ficheiros ao html
app = Flask(__name__, template_folder="templates")
@app.route("/")
def index ():
    return render_template('index.html')

@app.route("/frota")
def frota ():
    veiculos = lerXML("frota.xml")

    # obter texto no input field "pesquisa"
    pesquisa = request.args.get('pesquisa', "")
    disponivelFiltro = request.args.get("disponiveis")

    if pesquisa or disponivelFiltro:
        veiculos = [
            v for v in veiculos 
            if (pesquisa.lower() in v['marca'].lower() or pesquisa.lower() in v['modelo'].lower())
            and (not disponivelFiltro or v["disponibilidade"].lower() == "disponível")
        ]
    return render_template('frota.html', frota = veiculos)

@app.route("/contactos")
def contactos ():
    return render_template('contactos.html')



if __name__ == '__main__':
    app.run(debug=True)