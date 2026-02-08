# StaticCAnalyzer

StaticCAnalyzer es una herramienta de **análisis estático para código C** diseñada como proyecto técnico de portafolio, con un enfoque profesional y modular.  
El objetivo del proyecto es demostrar comprensión real de cómo funcionan las herramientas de análisis estático utilizadas en entornos de software crítico e industrial.

La herramienta analiza código C **sin ejecutarlo**, construyendo un AST (Abstract Syntax Tree) y aplicando un conjunto de reglas extensibles para detectar errores comunes, problemas de calidad y malas prácticas.

---

## 🎯 Objetivos del proyecto

- Analizar código C de forma estática (sin ejecución)
- Detectar errores frecuentes relacionados con:
  - Seguridad de memoria
  - Calidad del código
  - Buenas prácticas
- Diseñar una arquitectura modular y extensible
- Generar reportes estructurados y legibles
- Facilitar la integración en pipelines CI/CD
- Documentar decisiones técnicas y limitaciones reales

Este proyecto **no pretende competir con herramientas comerciales**, sino servir como demostración técnica y base experimental.

---

## 🧠 Enfoque técnico

- El análisis se basa en **AST real**, no en expresiones regulares
- Se utilizan bindings de **Clang / libclang** para el parsing
- Cada regla de análisis está desacoplada del núcleo
- El diseño permite añadir nuevas reglas sin modificar el core

---

## 🏗️ Arquitectura del proyecto

```
StaticCAnalyzer/
├── cli/            # Interfaz de línea de comandos
├── parser/         # Construcción del AST a partir de código C
├── analyzer/       # Motor de análisis
├── rules/          # Reglas de análisis (plugins)
├── reporter/       # Generación de reportes (JSON / consola)
├── examples/       # Código C de ejemplo con errores
├── tests/          # Pruebas básicas
└── README.md
```

### Principios de diseño
- Separación clara de responsabilidades
- Bajo acoplamiento entre módulos
- Extensibilidad orientada a tooling
- Código legible y documentado

---

## 🔍 Reglas de análisis implementadas (ejemplo)

### Seguridad de memoria
- Variables no inicializadas
- Posible dereferencia de puntero nulo
- Uso de punteros sin inicializar

### Calidad de código
- Funciones excesivamente largas
- Número elevado de parámetros
- Complejidad ciclomática básica

### Buenas prácticas
- Variables no utilizadas
- Código muerto evidente
- Retornos inconsistentes en funciones

> ⚠️ Algunas reglas pueden generar falsos positivos, lo cual es una limitación conocida del análisis estático.

---

## 📤 Salida del análisis

- Reporte estructurado en **JSON**
- Salida legible por consola con advertencias
- Cada advertencia incluye:
  - Tipo
  - Ubicación (archivo y línea)
  - Regla disparada
  - Descripción técnica

---

## 🚀 Uso básico

```bash
python main.py analyze examples/example.c
```

Salida por consola:
```
[WARNING] Variable 'ptr' usada sin inicializar (example.c:42)
[INFO] Función 'process_data' supera la longitud recomendada
```

---

## 🔧 Integración en CI

La herramienta está pensada para ser ejecutada en pipelines CI/CD:

- Código de salida distinto de 0 si se superan umbrales
- Reportes exportables para análisis posterior
- Fácil integración en GitHub Actions, GitLab CI, Jenkins, etc.

---

## ⚠️ Limitaciones conocidas

- No se realiza análisis interprocedimental completo
- No se modela el flujo de ejecución real
- No se resuelven macros complejas en profundidad
- Algunas reglas son heurísticas

Estas limitaciones son intencionadas y documentadas como parte del aprendizaje.

---

## 📚 Motivación

Este proyecto nace como ejercicio técnico para profundizar en:
- Análisis estático
- Tooling de bajo nivel
- Ingeniería de software para sistemas críticos
- Diseño de herramientas extensibles

Está especialmente orientado a contextos industriales, aeronáuticos y de infraestructura crítica.
