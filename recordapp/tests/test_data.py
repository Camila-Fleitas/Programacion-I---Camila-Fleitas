# tests/test_data.py
import json
import os
import csv
from logic.data_manager import load_registros, save_registros, add_registro, delete_registro, export_to_csv
from logic.validation import validate_date, validate_description
import pytest


def test_load_empty(tmp_path):
    p = tmp_path / "reg.json"
    # Si el archivo no existe, load_registros debe devolver lista vacía y crear el archivo
    registros = load_registros(str(p))
    assert isinstance(registros, list)
    assert registros == []


def test_add_and_save_and_load(tmp_path):
    p = tmp_path / "reg.json"
    r = {"fecha": "2025-11-01", "estado": "😊", "descripcion": "Prueba"}
    add_registro(str(p), r)
    registros = load_registros(str(p))
    assert len(registros) == 1
    assert registros[0]["descripcion"] == "Prueba"


def test_delete_registro(tmp_path):
    p = tmp_path / "reg.json"
    r1 = {"fecha": "2025-11-01", "estado": "😊", "descripcion": "A"}
    r2 = {"fecha": "2025-11-02", "estado": "😐", "descripcion": "B"}
    save_registros(str(p), [r1, r2])
    delete_registro(str(p), 0)
    regs = load_registros(str(p))
    assert len(regs) == 1
    assert regs[0]["descripcion"] == "B"
    with pytest.raises(IndexError):
        delete_registro(str(p), 10)  # índice fuera de rango


def test_export_to_csv(tmp_path):
    p = tmp_path / "reg.json"
    csv_path = tmp_path / "out.csv"
    r1 = {"fecha": "2025-11-01", "estado": "😊", "descripcion": "A"}
    save_registros(str(p), [r1])
    export_to_csv(str(p), str(csv_path))
    assert csv_path.exists()
    with open(str(csv_path), newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert len(rows) == 1
    assert rows[0]["descripcion"] == "A"


def test_validation_functions():
    assert validate_date("2025-12-31")
    assert not validate_date("31-12-2025")
    assert validate_description("Algo")
    assert not validate_description("   ")
