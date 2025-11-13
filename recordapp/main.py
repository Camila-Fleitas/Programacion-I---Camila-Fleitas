# main.py
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from datetime import date, datetime
import os
import json

from logic.data_manager import (
    LOAD_PATH_DEFAULT,
    load_registros,
    add_registro,
    delete_registro,
    save_registros,
    export_to_csv
)
from logic.validation import validate_date, validate_description

DATA_PATH = LOAD_PATH_DEFAULT  # 'data/registros.json'


class RecordApp:
    def __init__(self, master):
        self.master = master
        master.title("RecordApp - Registro de aprendizajes")
        master.geometry("700x450")

        # Cargar registros
        os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
        self.registros = load_registros(DATA_PATH)

        # --- UI ---
        # Panel izquierdo: formulario
        left_frame = tk.Frame(master)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)

        tk.Label(left_frame, text="Fecha (YYYY-MM-DD):").pack(anchor="w")
        self.fecha_var = tk.StringVar(value=date.today().isoformat())
        self.input_fecha = tk.Entry(left_frame, textvariable=self.fecha_var, width=20)
        self.input_fecha.pack(anchor="w")

        tk.Label(left_frame, text="Estado de ánimo:").pack(anchor="w", pady=(8, 0))
        self.mood_var = tk.StringVar(value="😊")
        moods = ["😊", "😐", "😔"]
        self.mood_menu = tk.OptionMenu(left_frame, self.mood_var, *moods)
        self.mood_menu.pack(anchor="w")

        tk.Label(left_frame, text="Descripción:").pack(anchor="w", pady=(8, 0))
        self.desc_text = tk.Text(left_frame, width=40, height=10)
        self.desc_text.pack(anchor="w")

        btn_frame = tk.Frame(left_frame)
        btn_frame.pack(anchor="w", pady=10)

        self.save_btn = tk.Button(btn_frame, text="Guardar", command=self.guardar_registro)
        self.save_btn.grid(row=0, column=0, padx=(0, 6))

        self.clear_btn = tk.Button(btn_frame, text="Limpiar", command=self.limpiar_form)
        self.clear_btn.grid(row=0, column=1, padx=(0, 6))

        self.export_btn = tk.Button(btn_frame, text="Exportar CSV", command=self.export_csv)
        self.export_btn.grid(row=0, column=2)

        # Panel derecho: lista y detalle
        right_frame = tk.Frame(master)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        tk.Label(right_frame, text="Registros guardados:").pack(anchor="w")
        self.listbox = tk.Listbox(right_frame)
        self.listbox.pack(fill=tk.BOTH, expand=True)
        self.listbox.bind("<<ListboxSelect>>", self.on_select)

        list_btn_frame = tk.Frame(right_frame)
        list_btn_frame.pack(anchor="w", pady=6)

        self.delete_btn = tk.Button(list_btn_frame, text="Eliminar seleccionado", command=self.eliminar_seleccion)
        self.delete_btn.grid(row=0, column=0, padx=(0, 6))

        self.view_btn = tk.Button(list_btn_frame, text="Ver detalle", command=self.ver_detalle)
        self.view_btn.grid(row=0, column=1)

        # Rellenar listbox
        self.refresh_listbox()

    def limpiar_form(self):
        self.fecha_var.set(date.today().isoformat())
        self.mood_var.set("😊")
        self.desc_text.delete("1.0", tk.END)

    def guardar_registro(self):
        f = self.fecha_var.get().strip()
        mood = self.mood_var.get()
        desc = self.desc_text.get("1.0", tk.END).strip()

        if not validate_date(f):
            messagebox.showerror("Fecha inválida", "La fecha debe tener formato YYYY-MM-DD.")
            return

        if not validate_description(desc):
            messagebox.showerror("Descripción inválida", "La descripción no puede estar vacía.")
            return

        registro = {
            "fecha": f,
            "estado": mood,
            "descripcion": desc
        }

        add_registro(DATA_PATH, registro)
        self.registros = load_registros(DATA_PATH)
        self.refresh_listbox()
        messagebox.showinfo("Guardado", "Registro guardado correctamente.")
        self.limpiar_form()

    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for idx, r in enumerate(self.registros):
            preview = r["descripcion"].replace("\n", " ")
            if len(preview) > 50:
                preview = preview[:47] + "..."
            display = f"{idx+1}. {r['fecha']} {r['estado']} - {preview}"
            self.listbox.insert(tk.END, display)

    def on_select(self, event):
        # al seleccionar mostramos nada automáticamente; usamos botón ver detalle
        pass

    def ver_detalle(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Selección", "No hay ningún registro seleccionado.")
            return
        idx = sel[0]
        r = self.registros[idx]
        detalle = f"Fecha: {r['fecha']}\nEstado: {r['estado']}\n\nDescripción:\n{r['descripcion']}"
        messagebox.showinfo("Detalle del registro", detalle)

    def eliminar_seleccion(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showwarning("Selección", "No hay ningún registro seleccionado.")
            return
        idx = sel[0]
        confirm = messagebox.askyesno("Confirmar", "¿Eliminar el registro seleccionado?")
        if not confirm:
            return
        delete_registro(DATA_PATH, idx)
        self.registros = load_registros(DATA_PATH)
        self.refresh_listbox()

    def export_csv(self):
        # Pedir ruta de guardado
        save_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            title="Exportar registros a CSV"
        )
        if not save_path:
            return
        try:
            export_to_csv(DATA_PATH, save_path)
            messagebox.showinfo("Exportado", f"Registros exportados a {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RecordApp(root)
    root.mainloop()
