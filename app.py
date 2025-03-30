import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email_ingresado = request.form['email']
    password_ingresada = request.form['password']

    # 📄 Leer el Excel con los datos de los alumnos
    try:
        df = pd.read_excel("data/alumnos.xlsx")
        df2 = pd.read_excel("data/datos_alumno.xlsx")

    except Exception as e:
        print("❌ Error al leer el archivo Excel:", e)
        return "Error del servidor"

    # 🔍 Buscar si hay coincidencia
    alumno = df[(df['email'] == email_ingresado) & (df['contraseña'].astype(str) == password_ingresada)]

    if not alumno.empty:
        print("✅ Usuario válido. Redirigiendo al perfil...")
        
        # ✅ Buscar datos extra del alumno
        try:
            df_datos = pd.read_excel("data/datos_alumno.xlsx")
            datos_alumno = df_datos[df_datos["dni"] == int(alumno.iloc[0]["dni"])].iloc[0]
            curso = datos_alumno["curso"]
            division = datos_alumno["division"]
        except Exception as e:
            print("❌ No se pudo obtener curso/división:", e)
            curso = "?"
            division = "?"

        # 👉 Renderizar perfil con los datos del alumno
        return render_template(
            "perfil.html",
            nombre=alumno.iloc[0]["nombre"],
            curso=curso,
            division=division
        )


    else:
        print("❌ Usuario o contraseña incorrectos.")
        return render_template("index.html", error="Usuario o contraseña incorrectos.")

if __name__ == '__main__':
     # Para Render (producción)
    app.run(host='0.0.0.0', port=10000)
    
    # Para local
   # app.run(debug=True)
