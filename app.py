from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Ruta al archivo Excel
DATA_FILE = os.path.join("data", "formulario.xlsm")  # <- ya puse .xlsm

def cargar_datos():
    """Carga los datos desde el Excel."""
    df = pd.read_excel(DATA_FILE, sheet_name="TEMPORALES FORMULA")

    # Renombramos columnas para usarlas más fácil
    df = df.rename(columns={
        "No.": "ID",
        "FECHA DE RECEPCION": "Fecha_Recepcion",
        "NUMERO DE SOLICITUD": "Numero_Solicitud",
        "INICIO VIGENCIA": "Inicio_Vigencia",
        "TERMINO VIGENCIA": "Termino_Vigencia",
        "PLAZA": "Plaza",
        "ID. PLAZA": "ID_Plaza",
        "NOMBRE DEL CANDIDATO": "Nombre_Candidato",
        "REGIMEN CONTRACTUAL": "Regimen_Contractual",
        "STATUS": "Status",
        "FECHA LIBERACION AL DP": "Fecha_Liberacion",
        "DEPARTAMENTO DEL PERSONAL": "Departamento",
        "OBSERVACIONES": "Observaciones"
    })
    return df

# Página principal con menú
@app.route("/")
def index():
    return render_template("menu.html")

# Página de consulta
@app.route("/consultar")
def consultar():
    df = cargar_datos()
    data = df.to_dict(orient="records")
    return render_template("consultar.html", solicitudes=data)

# Página de modificar (placeholder)
@app.route("/modificar")
def modificar():
    return render_template("modificar.html")

@app.route("/temporales")
def temporales():
    df = cargar_datos()
    data = df.to_dict(orient="records")
    return render_template("consultar.html", solicitudes=data, titulo="Temporales")

@app.route("/prorrogas")
def prorrogas():
    df = cargar_datos()  # más adelante puedes filtrar solo registros con prórrogas
    data = df.to_dict(orient="records")
    return render_template("consultar.html", solicitudes=data, titulo="Prórrogas")

@app.route("/seguimiento")
def seguimiento():
    df = cargar_datos()  # más adelante puedes hacer filtros por status
    data = df.to_dict(orient="records")
    return render_template("consultar.html", solicitudes=data, titulo="Seguimiento")

@app.route("/crear-fvs")
def crear_fvs():
    return render_template("crear_fvs.html")

if __name__ == "__main__":
    app.run(debug=True)


