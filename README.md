# 📊 ISFPP 2025 – Reporte Académico para la Facultad

Este proyecto corresponde a la **Instancia Supervisada de Formación Profesional (ISFPP) 2025** de la carrera **Analista Programador Universitario**.  
El objetivo es desarrollar un **sistema de indicadores de gestión académica**, basado en los Informes Sintéticos de Departamentos, Informes de Cátedra y Encuestas de Estudiantes.

Se trabajará con la metodología ágil **Scrum**, usando tableros Kanban en Miro y gestión de tareas mediante **GitHub Projects** e **Issues**.

---

## 🏗️ Arquitectura del proyecto

El repositorio se organiza como un **monorepo** que contiene tanto el **backend** como el **frontend**:

repo-isfpp/
│
├── backend/ # API en FastAPI + SQLAlchemy
│ ├── src/
│ ├── tests/
│ ├── requirements.txt
│ └── README.md
│
├── frontend/ # Aplicación web en React + TypeScript
│ ├── src/
│ ├── public/
│ ├── package.json
│ └── README.md
│
└── README.md # Este archivo (general del proyecto)
