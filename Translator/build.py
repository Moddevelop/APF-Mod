#!/usr/bin/env python3

import os
import json
import shutil

INPUT_DIR = "input"
EXTRACTED_DIR = "extracted"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)


def build(json_path):

    name = os.path.splitext(os.path.basename(json_path))[0]

    original_bin = os.path.join(INPUT_DIR, name + ".bin")

    if not os.path.exists(original_bin):
        print(f"[ERROR] No existe {original_bin}")
        return

    output_bin = os.path.join(OUTPUT_DIR, name + ".bin")

    shutil.copy2(original_bin, output_bin)

    with open(json_path, "r", encoding="utf-8") as f:
        entries = json.load(f)

    with open(output_bin, "r+b") as f:

        modified = 0
        skipped = 0

        for entry in entries:

            offset = entry["offset"]
            size = entry["size"]
            text = entry["text"]

            data = text.encode("utf-8")

            if len(data) > size:

                print(
                    f"[SKIP] Offset {offset} "
                    f"({len(data)}/{size} bytes)"
                )

                skipped += 1
                continue

            f.seek(offset)
            f.write(data)

            padding = size - len(data)

            if padding > 0:
                f.write(b"\x00" * padding)

            modified += 1

    print()
    print("=" * 40)
    print("Translator Engine Build")
    print("=" * 40)
    print("Archivo :", name + ".bin")
    print("Modificados :", modified)
    print("Omitidos :", skipped)
    print("Salida :", output_bin)
    print("=" * 40)


def main():

    files = [
        f for f in os.listdir(EXTRACTED_DIR)
        if f.endswith(".json")
    ]

    if not files:
        print("No hay JSON en extracted/")
        return

    for file in files:
        build(os.path.join(EXTRACTED_DIR, file))


if __name__ == "__main__":
    main()