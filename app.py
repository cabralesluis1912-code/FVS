from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

# Ruta al archivo Excel
DATA_FILE = os.path.join("data", "formulario.xlsm")

def cargar_datos():
    df = pd.read_excel(DATA_FILE, sheet_name="TEMPORALES FORMULA", header=1)
    df.columns = df.columns.str.strip()

    # Forzar columnas específicas a enteros (quita .0)
    columnas_enteras = ["ID. PLAZA", "GPO PLAZA", "NIVEL"]
    for col in columnas_enteras:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")

    return df



@app.route("/")
def index():
    return render_template("menu.html")

@app.route("/temporales")
def temporales():
    df = cargar_datos()
    data = df.to_dict(orient="records")
    return render_template("consultar.html", solicitudes=data, titulo="Temporales")

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


