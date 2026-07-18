#!/usr/bin/env python3

import os
import json
from pathlib import Path

VERSION = "0.1"

INPUT_DIR = "input"
OUTPUT_DIR = "extracted"


def create_dirs():
    os.makedirs(INPUT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def classify(text):
    t = text.lower()

    if t.startswith("http://") or t.startswith("https://"):
        return "url"

    if t.startswith("www."):
        return "url"

    if "[[" in text and "]]" in text:
        return "placeholder"

    if "/" in text or "\\" in text:
        return "path"

    return "text"


def extract_strings(data):

    results = []

    i = 0

    while i < len(data):

        if data[i] >= 32:

            start = i

            while i < len(data) and data[i] != 0:
                i += 1

            raw = data[start:i]

            text = None

            for enc in ("utf-8", "latin1"):

                try:
                    text = raw.decode(enc)

                    if len(text.strip()) >= 3:
                        break

                except:
                    text = None

            if text:

                results.append({

                    "offset": start,
                    "size": len(raw),
                    "type": classify(text),
                    "text": text

                })

        i += 1

    return results


def process(path):

    print(f"Analizando {path.name}")

    with open(path, "rb") as f:
        data = f.read()

    strings = extract_strings(data)

    output = {

        "file": path.name,
        "size": len(data),
        "entries": strings

    }

    out = Path(OUTPUT_DIR) / (path.stem + ".json")

    with open(out, "w", encoding="utf8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print(f"   {len(strings)} cadenas encontradas.")
    print(f"   JSON -> {out}\n")


def main():

    print(f"\nTranslator Engine v{VERSION}\n")

    create_dirs()

    files = list(Path(INPUT_DIR).glob("*.bin"))

    if not files:
        print("No hay archivos .bin en la carpeta input/")
        return

    print(f"{len(files)} archivo(s) encontrado(s).\n")

    for f in files:
        process(f)

    print("Finalizado.")


if __name__ == "__main__":
    main()