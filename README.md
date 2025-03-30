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

portal-alumno25/ ├── app.py # Código principal de la app Flask ├── requirements.txt # Dependencias del proyecto ├── Procfile # Indicaciones de despliegue para Render ├── templates/ │ ├── index.html # Página de inicio de sesión │ └── perfil.html # Perfil del alumno con datos ├── data/ │ ├── alumnos.xlsx # Datos de validación (correo, DNI, contraseña) │ └── datos_alumno.xlsx # Datos personales (nombre, curso, división, horario_id)
