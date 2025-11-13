# logic/data_manager.py
import json
import os
from typing import List, Dict
import csv

LOAD_PATH_DEFAULT = os.path.join("data", "registros.json")


def _ensure_file(path: str):
    dirpath = os.path.dirname(path)
    if dirpath and not os.path.exists(dirpath):
        os.makedirs(dirpath, exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump([], f, ensure_ascii=False, indent=2)


def load_registros(path: str = LOAD_PATH_DEFAULT) -> List[Dict]:
    _ensure_file(path)
    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
        except json.JSONDecodeError:
            return []


def save_registros(path: str, registros: List[Dict]):
    _ensure_file(path)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(registros, f, ensure_ascii=False, indent=2)


def add_registro(path: str, registro: Dict):
    registros = load_registros(path)
    registros.append(registro)
    save_registros(path, registros)


def delete_registro(path: str, index: int):
    registros = load_registros(path)
    if 0 <= index < len(registros):
        registros.pop(index)
        save_registros(path, registros)
    else:
        raise IndexError("Índice de registro fuera de rango")


def export_to_csv(path_json: str, path_csv: str):
    registros = load_registros(path_json)
    if not registros:
        # crear archivo csv vacío con header
        with open(path_csv, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["fecha", "estado", "descripcion"])
        return

    with open(path_csv, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["fecha", "estado", "descripcion"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for r in registros:
            writer.writerow({
                "fecha": r.get("fecha", ""),
                "estado": r.get("estado", ""),
                "descripcion": r.get("descripcion", "")
            })
