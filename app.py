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
                except ValueError:
                    bateria = "NaN"
                if bateria >= 0 and bateria <= 100:
                    veiculo["bateria"] = bateria
                else:
                    veiculo["bateria"] = "Fora do intervalo esperado"
            else: 
                veiculo[child.tag] = child.text

        veiculos.append(veiculo)

    return veiculos

lerXML("frota.xml")

# render_template para ligar ficheiros ao html
app = Flask(__name__, template_folder="templates")
@app.route("/")
def index ():
    return render_template('index.html')

@app.route("/catalogo")
def catalogo ():
    
        

    return render_template('catalogo.html')

@app.route("/contactos")
def contactos ():
    return render_template('contactos.html')



if __name__ == '__main__':
    app.run(debug=True)