# 📚 Portal del Alumno

**Portal del Alumno** es una aplicación web desarrollada con Python y Flask, pensada para que estudiantes puedan consultar su información académica de forma sencilla. El sistema permite mostrar datos como nombre, curso, división, horario escolar, materias adeudadas, asistencias y tareas pendientes.

---

## 🚀 Tecnologías utilizadas

- 🐍 Python 3
- 🌐 Flask
- 📊 Pandas
- 📄 openpyxl (para leer archivos Excel)
- 🎨 HTML + CSS
- ☁️ Render (despliegue gratuito en la nube)

---

## 🌐 Acceso en línea

Podés probar la aplicación desde este enlace:

🔗 [https://portal-alumno25.onrender.com](https://portal-alumno25.onrender.com)

> ⚠️ Si ves un error 502 al acceder, esperá unos segundos y recargá la página. El servidor gratuito puede tardar en activarse.

---

## 🗂️ Estructura del proyecto

portal-alumno25/ ├── app.py # Código principal de la app Flask├── requirements.txt # Dependencias del proyecto ├── Procfile # Indicaciones de despliegue para Render ├── templates/ │ ├── index.html # Página de inicio de sesión │ └── perfil.html # Perfil del alumno con datos ├── data/ │ ├── alumnos.xlsx # Datos de validación (correo, DNI, contraseña) │ └── datos_alumno.xlsx # Datos personales (nombre, curso, división, horario_id)


---

## 🧪 Cómo probarlo localmente

### 1. Clonar el repositorio

```bash
git clone https://github.com/C-Hidalgo/portal-alumno25.git
cd portal-alumno25

2. Crear un entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3. Instalar dependencias
pip install -r requirements.txt

4. Ejecutar la app
python app.py

Abrí tu navegador y entrá a:
🔗 http://localhost:5000

🔐 Datos de prueba
Podés usar alguno de los usuarios del archivo alumnos.xlsx como credenciales de inicio de sesión. Por ejemplo:

Email: alumno1@gmail.com

Contraseña: 36543210

📌 Notas
La contraseña inicial es el DNI del alumno.

En versiones futuras, se puede agregar cambio de contraseña, edición de datos y más seguridad.


