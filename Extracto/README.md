# Extractor y Empacador para APF

> ⚠️ Aviso: No me hago responsable del uso que le des ni de los mods que quieras hacer.  
> Este proyecto es solo educativo. Probablemente solo puedas modificar texturas, links, audio y sprites.

---

# 📦 Tutorial de uso

## 1. Crear espacio de trabajo

Primero crea una carpeta donde vas a trabajar con todos los archivos:

```text
Espace/
```

---

## 2. Descargar archivos necesarios

Descarga todos los archivos en Python 🐍 y asegúrate de incluir la carpeta `tools`.

Tu proyecto debe verse así:

```text
Espace/
├── extract.py
├── pack.py
├── prepack_android.py
├── input/
│   └── aqui_van_los_apf
└── tools/
    └── aqui_van_los_codigos_python_que_estan_en_tools
```

---

## 3. Abrir terminal

Ahora necesitas una terminal:

- 📱 **Android:** Termux  
- 🐧 **Linux:** Terminal integrada  
- 🪟 **Windows:** PowerShell / CMD / Cmder / FireCMD (recomendado)  
- 🍎 **Mac:** Terminal / iTerm2 / Warp / Zsh tools  

---

## 4. Ejecutar el extractor

Dentro de la carpeta del proyecto ejecuta:

```bash
python extract.py
```

---

## 5. Empaquetar archivos

Cuando termines de modificar los assets:

```bash
python pack.py
```

---

## 6. Audio 

⚠️ Si modificaste audio te recomiendo primero 
ejecutar este código antes de pack.py:

```bash
python prepack_android.py
```

---

# 🎮 Notas

- Puedes modificar texturas
- Puedes cambiar audio
- Puedes editar sprites
- Puedes modificar rutas o links dentro del juego
- modelo 3d aun no compatible ⚠️

---
