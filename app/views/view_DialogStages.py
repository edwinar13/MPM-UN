"""
view_DialogStages.py
====================

Diálogo de configuración de ETAPAS de análisis (estilo Plaxis/Midas),
construido 100% en código (sin .ui de Qt Designer).

Es la única fuente de verdad para la configuración del análisis: cada
etapa lleva su tipo, damping, Courant, plasticidad, integración y
parámetros de carga/tiempo. La gravedad sigue siendo global (menú Data).

Uso:
    dlg = DialogStages(model_current_project, dt_provider=fn, parent=self)
    if dlg.exec():
        # el diálogo ya persistió las etapas vía model.updateStages(...)
        ...

`dt_provider` (opcional): callable(courant: float, stage_type: str) -> float | None
    Devuelve el dt con el que correrá la etapa (mínimo entre los materiales
    seleccionados; en consolidación, el de la onda no drenada) para el
    Courant dado, o None si no hay materiales. Solo para display.
"""

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout, QGridLayout,
    QListWidget, QListWidgetItem, QPushButton, QLineEdit, QComboBox,
    QDoubleSpinBox, QSpinBox, QLabel, QDialogButtonBox, QGroupBox,
    QWidget, QMessageBox,
)
from PySide6.QtCore import Qt

import os


# (etiqueta visible, valor persistido TIPO)
STAGE_TYPES = [
    ("Geostático", "geostatic"),
    ("Incrementos de carga", "load_increment"),
    ("Dinámico", "dynamic"),
    ("Consolidación (doble fase)", "consolidation"),
]

# Defaults por tipo al crear/cambiar una etapa
STAGE_DEFAULTS = {
    "geostatic":      dict(DAMPING=0.75, COURANT=0.6, PLASTICIDAD=0, GAUSS=True,
                           NUMEROINCREMENTOS=10, TIEMPOANALISIS=0.0),
    "load_increment": dict(DAMPING=0.75, COURANT=0.1, PLASTICIDAD=1, GAUSS=True,
                           NUMEROINCREMENTOS=10, TIEMPOANALISIS=0.0),
    "dynamic":        dict(DAMPING=0.05, COURANT=0.1, PLASTICIDAD=1, GAUSS=False,
                           NUMEROINCREMENTOS=1, TIEMPOANALISIS=1.0),
    # Caso de validación (Caro González, 2024): sin amortiguamiento, Courant 0.98
    "consolidation":  dict(DAMPING=0.0, COURANT=0.9, PLASTICIDAD=0, GAUSS=False,
                           NUMEROINCREMENTOS=1, TIEMPOANALISIS=1.0),
}

# Campos visibles según tipo
VISIBLE_FIELDS = {
    "geostatic":      {"nincre", "tolff", "tolee", "gauss"},
    "load_increment": {"nincre", "tolff", "tolee", "gauss"},
    "dynamic":        {"tiempo", "contact", "gauss"},
    "consolidation":  {"tiempo", "p0"},
}
TYPE_DEPENDENT_FIELDS = ("nincre", "tiempo", "tolff", "tolee", "contact", "gauss", "p0")

# Qué hace cada tipo con las cargas (nota bajo el formulario)
STAGE_LOAD_NOTE = {
    "geostatic": (
        "Aplica solo el peso propio, con una rampa de gravedad en n pasos. "
        "Las fuerzas Fx/Fy de las partículas no se usan en esta etapa."),
    "load_increment": (
        "Las fuerzas Fx/Fy de las partículas son la carga final "
        "[kN por metro de espesor]. Se aplican en rampa: 1/n, 2/n, … hasta "
        "el 100 %, con la gravedad completa."),
    "dynamic": (
        "Las fuerzas Fx/Fy de las partículas se aplican completas desde el "
        "inicio, junto con la gravedad."),
    "consolidation": (
        "Doble fase (sólido + agua). Las fuerzas Fx/Fy se aplican completas desde "
        "el inicio. Los contornos con restricción son impermeables; las superficies "
        "libres drenan. Un solo material, con porosidad, permeabilidad y módulo del "
        "agua (su densidad se toma como seca). Los esfuerzos de resultados son "
        "efectivos y se agrega la presión de poros."),
}


# Stylesheet autocontenido con la paleta de la app (styles_oscuro.css):
# grises #222222/#333333/#444444, texto #DDDDDD/#999999,
# acento verde #C8CC8E, teal #77ACA2, fuente Ubuntu.
DIALOG_STYLE = """
QDialog {
    background-color: #333333;
    font: 9pt "Ubuntu";
}
QLabel {
    color: #DDDDDD;
    font: 9pt "Ubuntu";
    background: transparent;
}
QLabel#labelSectionTitle {
    color: #C8CC8E;
    font: 700 10pt "Ubuntu";
    padding-bottom: 2px;
}
QLabel#labelDt {
    color: #77ACA2;
    font: italic 9pt "Ubuntu";
}
QGroupBox {
    color: #C8CC8E;
    font: 500 10pt "Ubuntu";
    background-color: #3B3B3B;
    border: 1px solid #444444;
    border-radius: 6px;
    margin-top: 12px;
    padding: 8px 4px 4px 4px;
}
QGroupBox::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 10px;
    padding: 0px 4px;
}
QListWidget {
    background-color: #2B2B2B;
    color: #DDDDDD;
    border: 1px solid #444444;
    border-radius: 6px;
    outline: none;
    font: 9pt "Ubuntu";
}
QListWidget::item {
    padding: 8px 6px;
    margin: 2px 3px;
    border-radius: 4px;
    border-left: 3px solid transparent;
}
QListWidget::item:hover {
    background-color: #3B3B3B;
}
QListWidget::item:selected {
    background-color: #444444;
    color: #C8CC8E;
    border-left: 3px solid #C8CC8E;
}
QLineEdit, QDoubleSpinBox, QSpinBox, QComboBox {
    background-color: #444444;
    color: #DDDDDD;
    border: 1px solid #555555;
    border-radius: 4px;
    padding: 4px 6px;
    font: 9pt "Ubuntu";
    selection-background-color: #77ACA2;
    selection-color: #222222;
}
QLineEdit:hover, QDoubleSpinBox:hover, QSpinBox:hover, QComboBox:hover {
    border: 1px solid #777777;
}
QLineEdit:focus, QDoubleSpinBox:focus, QSpinBox:focus, QComboBox:focus {
    border: 1px solid #C8CC8E;
}
QComboBox::drop-down {
    border: none;
    width: 22px;
}
QComboBox::down-arrow {
    width: 0; height: 0;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 5px solid #DDDDDD;
    margin-right: 6px;
}
QComboBox QAbstractItemView {
    background-color: #383838;
    color: #DDDDDD;
    border: 1px solid #555555;
    border-radius: 4px;
    selection-background-color: #444444;
    selection-color: #C8CC8E;
    outline: none;
}
QDoubleSpinBox::up-button, QSpinBox::up-button,
QDoubleSpinBox::down-button, QSpinBox::down-button {
    background-color: #4A4A4A;
    border: none;
    width: 16px;
}
QDoubleSpinBox::up-button:hover, QSpinBox::up-button:hover,
QDoubleSpinBox::down-button:hover, QSpinBox::down-button:hover {
    background-color: #5A5A5A;
}
QDoubleSpinBox::up-arrow, QSpinBox::up-arrow {
    width: 0; height: 0;
    border-left: 3px solid transparent;
    border-right: 3px solid transparent;
    border-bottom: 4px solid #DDDDDD;
}
QDoubleSpinBox::down-arrow, QSpinBox::down-arrow {
    width: 0; height: 0;
    border-left: 3px solid transparent;
    border-right: 3px solid transparent;
    border-top: 4px solid #DDDDDD;
}
QPushButton {
    background-color: #444444;
    color: #DDDDDD;
    border: 1px solid #555555;
    border-radius: 4px;
    padding: 6px 12px;
    font: 500 9pt "Ubuntu";
}
QPushButton:hover {
    background-color: #555555;
    border: 1px solid #666666;
}
QPushButton:pressed {
    background-color: #3B3B3B;
}
QPushButton#btnOk {
    background-color: #C8CC8E;
    color: #222222;
    border: none;
    font: 700 9pt "Ubuntu";
    padding: 6px 22px;
}
QPushButton#btnOk:hover {
    background-color: #D6DA9C;
}
QPushButton#btnOk:pressed {
    background-color: #B9BD80;
}
QMessageBox {
    background-color: #333333;
}
QMessageBox QLabel {
    color: #DDDDDD;
}
"""


def stages_summary_html(stages, gravity, fps, resume_from=0):
    """Resumen de solo lectura de la configuración del análisis (panel Ejecutar)."""
    if not stages:
        return "<i>Sin etapas: use «Configurar etapas…».</i>"
    labels = dict((v, t) for t, v in STAGE_TYPES)
    lines = [f"Gravedad {float(gravity):g} m/s² · {int(fps)} cuadros/s"]
    for i, st in enumerate(stages, start=1):
        tipo = st.get("TIPO", "")
        if tipo in ("geostatic", "load_increment"):
            extent = f"{int(st.get('NUMEROINCREMENTOS', 0))} incrementos"
        else:
            extent = f"{float(st.get('TIEMPOANALISIS', 0)):g} s"
        plast = "elastoplástico" if st.get("PLASTICIDAD") else "elástico"
        line = (f"<b>{i}. {st.get('NOMBRE') or labels.get(tipo, tipo)}</b> — "
                f"{labels.get(tipo, tipo)}, {extent}, amort. {float(st.get('DAMPING', 0)):g}, {plast}")
        if resume_from and i < resume_from:
            line = f"<span style='color:#777777'>{line} (se salta)</span>"
        lines.append(line)
    if resume_from:
        lines.append(f"<span style='color:#C8CC8E'>Reanuda desde la etapa {resume_from} "
                     f"(checkpoint de la etapa {resume_from - 1}).</span>")
    return "<br>".join(lines)


def _new_stage_dict(stage_type="dynamic", name="Etapa"):
    """Crea un dict de etapa con los defaults del tipo."""
    d = STAGE_DEFAULTS[stage_type]
    return {
        "NOMBRE": name,
        "TIPO": stage_type,
        "DAMPING": d["DAMPING"],
        "COURANT": d["COURANT"],
        "NUMEROINCREMENTOS": d["NUMEROINCREMENTOS"],
        "TIEMPOANALISIS": d["TIEMPOANALISIS"],
        "TOLFF": 0.01,
        "TOLEE": 0.01,
        "PLASTICIDAD": d["PLASTICIDAD"],
        "GAUSS": d["GAUSS"],
    }


class DialogStages(QDialog):

    def __init__(self, model_current_project, dt_provider=None, parent=None, fps=30):
        super().__init__(parent)
        self.model_current_project = model_current_project
        self.dt_provider = dt_provider
        self._fps = fps
        self._loading = False  # evita write-back mientras se puebla el form

        # Copia editable de las etapas persistidas
        stages = model_current_project.getStages() or []
        self._stages = [dict(s) for s in stages]
        if not self._stages:
            self._stages = [_new_stage_dict("dynamic", "Etapa 1")]

        # Etapa desde la que se reanudará (0 = desde el inicio)
        self._resume_from = model_current_project.getResumeFrom()
        if self._resume_from > len(self._stages):
            self._resume_from = 0

        # Grupos de puntos materiales y materiales del proyecto (para el
        # cambio de material por etapa): listas de (id, nombre)
        self._groups = [(k, m.getName()) for k, m in
                        model_current_project.getModelsPointsMaterials().items()]
        self._materials = []
        for k, p in model_current_project.getModelsProperties().items():
            data = p.getData()
            self._materials.append((k, data[list(data.keys())[0]].get("NAME", k)))

        self.setWindowTitle("Etapas de análisis")
        self.setMinimumSize(680, 600)
        self.setStyleSheet(DIALOG_STYLE)
        self._build_ui()
        self._reload_list(select=0)

    # ---------------------------------------------------------------- UI
    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(14, 14, 14, 12)
        root.setSpacing(10)

        body = QHBoxLayout()
        body.setSpacing(12)
        root.addLayout(body, 1)

        # ── Izquierda: gravedad (global del análisis), lista de etapas + botones ──
        left = QVBoxLayout()
        left.setSpacing(6)
        lbl_grav = QLabel("Gravedad [m/s²]")
        lbl_grav.setObjectName("labelSectionTitle")
        left.addWidget(lbl_grav)
        self.spGravity = QDoubleSpinBox()
        self.spGravity.setRange(0.0, 100.0)
        self.spGravity.setDecimals(3)
        self.spGravity.setSingleStep(0.01)
        self.spGravity.setValue(float(self.model_current_project.getGravity()))
        self.spGravity.setToolTip("Una sola para todas las etapas. La etapa geostática "
                                  "la aplica en rampa; 0 = sin peso propio.")
        left.addWidget(self.spGravity)
        lbl_fps = QLabel("Resultados [cuadros/s]")
        lbl_fps.setObjectName("labelSectionTitle")
        left.addWidget(lbl_fps)
        self.spFps = QSpinBox()
        self.spFps.setRange(1, 1000)
        self.spFps.setValue(int(self._fps))
        self.spFps.setToolTip("Cuántos estados se guardan por segundo de análisis en las "
                              "etapas dinámicas y de consolidación (frames de la animación). "
                              "Las cuasi-estáticas guardan uno por incremento.")
        left.addWidget(self.spFps)
        lbl_seq = QLabel("Secuencia de etapas")
        lbl_seq.setObjectName("labelSectionTitle")
        left.addWidget(lbl_seq)
        self.listWidget = QListWidget()
        self.listWidget.currentRowChanged.connect(self._on_row_changed)
        left.addWidget(self.listWidget, 1)

        btns = QGridLayout()
        btns.setSpacing(6)
        self.btnAdd = QPushButton("+ Agregar")
        self.btnRemove = QPushButton("− Quitar")
        self.btnUp = QPushButton("Subir")
        self.btnDown = QPushButton("Bajar")
        self.btnAdd.clicked.connect(self._on_add)
        self.btnRemove.clicked.connect(self._on_remove)
        self.btnUp.clicked.connect(lambda: self._on_move(-1))
        self.btnDown.clicked.connect(lambda: self._on_move(+1))
        btns.addWidget(self.btnAdd, 0, 0)
        btns.addWidget(self.btnRemove, 0, 1)
        btns.addWidget(self.btnUp, 1, 0)
        btns.addWidget(self.btnDown, 1, 1)
        left.addLayout(btns)

        # ── Reanudar desde un checkpoint ──
        lbl_resume = QLabel("Reanudar desde")
        lbl_resume.setObjectName("labelSectionTitle")
        left.addWidget(lbl_resume)
        self.cbResume = QComboBox()
        self.cbResume.currentIndexChanged.connect(self._on_resume_changed)
        left.addWidget(self.cbResume)
        self.lblResume = QLabel("")
        self.lblResume.setObjectName("labelDt")
        self.lblResume.setWordWrap(True)
        left.addWidget(self.lblResume)
        self._reload_resume_combo()

        left_box = QWidget()
        left_box.setLayout(left)
        left_box.setMaximumWidth(240)
        body.addWidget(left_box)

        # ── Derecha: formulario de la etapa seleccionada ──
        self.form_group = QGroupBox("Configuración de la etapa")
        form = QFormLayout(self.form_group)
        form.setContentsMargins(12, 14, 12, 10)
        form.setHorizontalSpacing(14)
        form.setVerticalSpacing(9)
        self._rows = {}  # nombre -> (label, field)

        self.edName = QLineEdit()
        self.edName.textChanged.connect(self._on_field_changed)
        self._add_row(form, "name", "Nombre", self.edName)

        self.cbType = QComboBox()
        for label, val in STAGE_TYPES:
            self.cbType.addItem(label, val)
        self.cbType.currentIndexChanged.connect(self._on_type_changed)
        self._add_row(form, "type", "Tipo", self.cbType)

        self.spDamping = self._make_dspin(0.0, 1.0, 0.05, 3)
        self._add_row(form, "damping", "Amortiguamiento", self.spDamping)

        self.spCourant = self._make_dspin(0.01, 1.0, 0.05, 3)
        self._add_row(form, "courant", "Número de Courant", self.spCourant)

        self.spNincre = QSpinBox()
        self.spNincre.setRange(1, 1000000)
        self.spNincre.valueChanged.connect(self._on_field_changed)
        self._add_row(form, "nincre", "N.º de incrementos", self.spNincre)

        self.spTiempo = self._make_dspin(0.0, 1e6, 0.5, 3)
        self._add_row(form, "tiempo", "Duración (s)", self.spTiempo)

        self.spP0 = self._make_dspin(0.0, 1e6, 1.0, 3)
        self.spP0.setSuffix(" kPa")
        self.spP0.setToolTip(
            "Presión de poros inicial, uniforme (positiva en compresión). Se asigna "
            "al entrar a la primera etapa de consolidación;\nuna etapa de "
            "consolidación posterior conserva la presión que trae.\nPara una carga "
            "aplicada de golpe sobre suelo saturado: p0 = carga.")
        self._add_row(form, "p0", "Presión de poros inicial", self.spP0)

        self.spTolFF = self._make_dspin(1e-6, 1.0, 0.005, 5)
        self._add_row(form, "tolff", "Tolerancia fuerza (ff)", self.spTolFF)

        self.spTolEE = self._make_dspin(1e-6, 1.0, 0.005, 5)
        self._add_row(form, "tolee", "Tolerancia energía (ee)", self.spTolEE)

        self.cbPlast = QComboBox()
        self.cbPlast.addItem("Elástico", 0)
        self.cbPlast.addItem("Elastoplástico (Mohr-Coulomb)", 1)
        self.cbPlast.currentIndexChanged.connect(self._on_field_changed)
        self._add_row(form, "plast", "Comportamiento", self.cbPlast)

        self.cbGauss = QComboBox()
        self.cbGauss.addItem("Automático (según tipo)", None)
        self.cbGauss.addItem("Sí", True)
        self.cbGauss.addItem("No", False)
        self.cbGauss.currentIndexChanged.connect(self._on_field_changed)
        self._add_row(form, "gauss", "Integración Gauss (avanzado)", self.cbGauss)

        # Interfaz entre grupos de puntos materiales (solo dinámico)
        self.cbContact = QComboBox()
        self.cbContact.addItem("Adherida (un solo campo)", False)
        self.cbContact.addItem("Friccional (cada grupo es un cuerpo)", True)
        self.cbContact.setToolTip(
            "Adherida: los grupos se mueven juntos en la interfaz (no deslizan "
            "ni se separan).\nFriccional: cada grupo es un cuerpo con contacto "
            "de Coulomb; pueden deslizar y separarse.\nPor ahora con exactamente "
            "2 grupos y sin integración Gauss.")
        self.cbContact.currentIndexChanged.connect(self._on_field_changed)
        self.cbContact.currentIndexChanged.connect(self._update_friction_visibility)
        self._add_row(form, "contact", "Interfaz entre grupos", self.cbContact)

        self.spFriction = self._make_dspin(0.0, 10.0, 0.01, 3)
        self.spFriction.setToolTip("Coeficiente de fricción de Coulomb μ entre cuerpos.")
        self._add_row(form, "friction", "Fricción μ", self.spFriction)

        self.cbReset = QComboBox()
        self.cbReset.addItem("No", False)
        self.cbReset.addItem("Sí", True)
        self.cbReset.setToolTip(
            "Al empezar la etapa pone en cero las deformaciones (elásticas, "
            "plásticas y gradiente de deformación).\nSe conservan esfuerzos y "
            "posiciones. Los desplazamientos de resultados ya se miden desde el "
            "inicio de cada etapa.")
        self.cbReset.currentIndexChanged.connect(self._on_field_changed)
        self._add_row(form, "reset", "Reiniciar deformaciones", self.cbReset)

        # Cambio de material por grupo, desde esta etapa
        lbl_mat = QLabel("Material desde esta etapa")
        lbl_mat.setObjectName("labelSectionTitle")
        form.addRow(lbl_mat)
        self.cbMaterial = {}  # id_grupo -> combo
        for gid, gname in self._groups:
            cb = QComboBox()
            cb.addItem("(sin cambio)", None)
            for mid, mname in self._materials:
                cb.addItem(mname, mid)
            cb.setToolTip("El cambio se mantiene en las etapas siguientes hasta "
                          "que otra lo cambie.")
            cb.currentIndexChanged.connect(self._on_field_changed)
            self.cbMaterial[gid] = cb
            form.addRow(QLabel(gname), cb)

        self.lblDt = QLabel("—")
        self.lblDt.setObjectName("labelDt")
        self._add_row(form, "dt", "dt estimado", self.lblDt)

        # Nota de qué hace la etapa con las cargas (cambia con el tipo)
        self.lblLoadNote = QLabel("")
        self.lblLoadNote.setObjectName("labelDt")
        self.lblLoadNote.setWordWrap(True)
        form.addRow(self.lblLoadNote)

        body.addWidget(self.form_group, 1)

        # ── Botones Aceptar/Cancelar ──
        self.buttonBox = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btn_ok = self.buttonBox.button(QDialogButtonBox.Ok)
        btn_ok.setText("Aceptar")
        btn_ok.setObjectName("btnOk")
        btn_cancel = self.buttonBox.button(QDialogButtonBox.Cancel)
        btn_cancel.setText("Cancelar")
        self.buttonBox.accepted.connect(self._on_accept)
        self.buttonBox.rejected.connect(self.reject)
        root.addWidget(self.buttonBox)

    # -------------------------------------------------- reanudar
    def _reload_resume_combo(self):
        """Puebla el combo con las etapas que tienen checkpoint disponible.

        La opción "Etapa N" usa el checkpoint guardado al terminar la etapa
        N-1, así que solo se habilita si ese archivo existe.
        """
        self.cbResume.blockSignals(True)
        self.cbResume.clear()
        self.cbResume.addItem("Desde el inicio", 0)
        model = self.cbResume.model()
        for n in range(2, len(self._stages) + 1):
            info = self._checkpoint_info(n - 1)
            name = self._stages[n - 1].get("NOMBRE") or f"Etapa {n}"
            if info:
                self.cbResume.addItem(f"Etapa {n}: {name}  ·  {info}", n)
            else:
                self.cbResume.addItem(f"Etapa {n}: {name}  (sin checkpoint)", n)
                model.item(self.cbResume.count() - 1).setEnabled(False)
        self._set_combo_data(self.cbResume, self._resume_from)
        self.cbResume.blockSignals(False)
        self._update_resume_label()

    def _checkpoint_info(self, stage_number):
        """Fecha del checkpoint de `stage_number`, o None si no existe."""
        try:
            path = self.model_current_project.getCheckpointPath(stage_number)
            if not os.path.exists(path):
                return None
            import numpy as np
            with np.load(path, allow_pickle=False) as d:
                if 'fecha' in d.files:
                    return str(d['fecha'])
            return "guardado"
        except BaseException:
            return None

    def _on_resume_changed(self, _idx):
        self._resume_from = self.cbResume.currentData() or 0
        self._update_resume_label()

    def _update_resume_label(self):
        if self._resume_from:
            self.lblResume.setText(
                f"⚠ Se saltarán las etapas 1 a {self._resume_from - 1} y se usará "
                f"el estado guardado.")
        else:
            self.lblResume.setText("")

    def _make_dspin(self, lo, hi, step, decimals):
        sp = QDoubleSpinBox()
        sp.setRange(lo, hi)
        sp.setSingleStep(step)
        sp.setDecimals(decimals)
        sp.valueChanged.connect(self._on_field_changed)
        return sp

    def _add_row(self, form, key, label_text, field):
        label = QLabel(label_text)
        form.addRow(label, field)
        self._rows[key] = (label, field)

    # ------------------------------------------------------------- lista
    def _reload_list(self, select=None):
        self.listWidget.blockSignals(True)
        self.listWidget.clear()
        type_label = {v: l for l, v in STAGE_TYPES}
        for i, s in enumerate(self._stages):
            name = s.get("NOMBRE") or f"Etapa {i + 1}"
            tipo = type_label.get(s.get("TIPO"), s.get("TIPO"))
            QListWidgetItem(f"{i + 1}. {name}  ({tipo})", self.listWidget)
        self.listWidget.blockSignals(False)
        # La lista de etapas cambió: rehacer las opciones de "Reanudar desde"
        if hasattr(self, 'cbResume'):
            if self._resume_from > len(self._stages):
                self._resume_from = 0
            self._reload_resume_combo()
        if select is not None and 0 <= select < len(self._stages):
            self.listWidget.setCurrentRow(select)
        elif self._stages:
            self.listWidget.setCurrentRow(0)
        else:
            self._load_selected_into_form()  # limpia/deshabilita

    def _current_index(self):
        return self.listWidget.currentRow()

    def _current_stage(self):
        i = self._current_index()
        if 0 <= i < len(self._stages):
            return self._stages[i]
        return None

    # ---------------------------------------------------------- handlers
    def _on_row_changed(self, _row):
        self._load_selected_into_form()

    def _on_add(self):
        self._stages.append(_new_stage_dict("dynamic", f"Etapa {len(self._stages) + 1}"))
        self._reload_list(select=len(self._stages) - 1)

    def _on_remove(self):
        i = self._current_index()
        if i < 0:
            return
        if len(self._stages) <= 1:
            QMessageBox.information(self, "Etapas", "Debe existir al menos una etapa.")
            return
        del self._stages[i]
        self._reload_list(select=min(i, len(self._stages) - 1))

    def _on_move(self, delta):
        i = self._current_index()
        j = i + delta
        if i < 0 or j < 0 or j >= len(self._stages):
            return
        self._stages[i], self._stages[j] = self._stages[j], self._stages[i]
        self._reload_list(select=j)

    def _on_type_changed(self, _idx):
        if self._loading:
            return
        stage = self._current_stage()
        if stage is None:
            return
        new_type = self.cbType.currentData()
        stage["TIPO"] = new_type
        # Reaplicar defaults del tipo (conservando el nombre)
        defaults = STAGE_DEFAULTS[new_type]
        stage["DAMPING"] = defaults["DAMPING"]
        stage["COURANT"] = defaults["COURANT"]
        stage["PLASTICIDAD"] = defaults["PLASTICIDAD"]
        stage["GAUSS"] = defaults["GAUSS"]
        stage["NUMEROINCREMENTOS"] = defaults["NUMEROINCREMENTOS"]
        stage["TIEMPOANALISIS"] = defaults["TIEMPOANALISIS"]
        if new_type == "consolidation":
            stage.setdefault("PRESIONPOROSINICIAL", 0.0)
        else:
            stage.pop("PRESIONPOROSINICIAL", None)
        self._load_selected_into_form()
        self._reload_list(select=self._current_index())

    def _on_field_changed(self, *_):
        if self._loading:
            return
        self._write_form_into_selected()
        self._update_dt_label()
        # Refrescar solo la etiqueta de la lista (nombre puede cambiar)
        i = self._current_index()
        if 0 <= i < self.listWidget.count():
            s = self._stages[i]
            type_label = {v: l for l, v in STAGE_TYPES}
            name = s.get("NOMBRE") or f"Etapa {i + 1}"
            tipo = type_label.get(s.get("TIPO"), s.get("TIPO"))
            self.listWidget.item(i).setText(f"{i + 1}. {name}  ({tipo})")

    # ---------------------------------------------------- form <-> dict
    def _load_selected_into_form(self):
        stage = self._current_stage()
        enabled = stage is not None
        self.form_group.setEnabled(enabled)
        if not enabled:
            return
        self._loading = True
        try:
            self.edName.setText(str(stage.get("NOMBRE", "")))
            self._set_combo_data(self.cbType, stage.get("TIPO", "dynamic"))
            self.spDamping.setValue(float(stage.get("DAMPING", 0.0)))
            self.spCourant.setValue(float(stage.get("COURANT", 0.1)))
            self.spNincre.setValue(int(stage.get("NUMEROINCREMENTOS", 1)))
            self.spTiempo.setValue(float(stage.get("TIEMPOANALISIS", 0.0)))
            self.spP0.setValue(float(stage.get("PRESIONPOROSINICIAL", 0.0)))
            self.spTolFF.setValue(float(stage.get("TOLFF", 0.01)))
            self.spTolEE.setValue(float(stage.get("TOLEE", 0.01)))
            self._set_combo_data(self.cbPlast, int(stage.get("PLASTICIDAD", 1)))
            self._set_combo_data(self.cbGauss, stage.get("GAUSS", None))
            self._set_combo_data(self.cbContact, bool(stage.get("MULTICUERPO", False)))
            self.spFriction.setValue(float(stage.get("FRICCION", 0.0)))
            self._set_combo_data(self.cbReset, bool(stage.get("REINICIARDEFORMACIONES", False)))
            changes = stage.get("CAMBIOMATERIAL") or {}
            for gid, cb in self.cbMaterial.items():
                self._set_combo_data(cb, changes.get(gid))
        finally:
            self._loading = False
        self._apply_type_visibility(stage.get("TIPO", "dynamic"))
        self._update_dt_label()

    def _write_form_into_selected(self):
        stage = self._current_stage()
        if stage is None:
            return
        stage["NOMBRE"] = self.edName.text()
        stage["TIPO"] = self.cbType.currentData()
        stage["DAMPING"] = self.spDamping.value()
        stage["COURANT"] = self.spCourant.value()
        stage["NUMEROINCREMENTOS"] = self.spNincre.value()
        stage["TIEMPOANALISIS"] = self.spTiempo.value()
        if stage["TIPO"] == "consolidation":
            stage["PRESIONPOROSINICIAL"] = self.spP0.value()
        else:
            stage.pop("PRESIONPOROSINICIAL", None)
        stage["TOLFF"] = self.spTolFF.value()
        stage["TOLEE"] = self.spTolEE.value()
        stage["PLASTICIDAD"] = self.cbPlast.currentData()
        stage["GAUSS"] = self.cbGauss.currentData()
        # La interfaz friccional solo existe en etapas dinámicas
        stage["MULTICUERPO"] = bool(self.cbContact.currentData()) and stage["TIPO"] == "dynamic"
        stage["FRICCION"] = self.spFriction.value()
        stage["REINICIARDEFORMACIONES"] = bool(self.cbReset.currentData())
        stage["CAMBIOMATERIAL"] = {gid: cb.currentData()
                                   for gid, cb in self.cbMaterial.items()
                                   if cb.currentData() is not None}

    def _apply_type_visibility(self, stage_type):
        visible = VISIBLE_FIELDS.get(stage_type, set())
        for key in TYPE_DEPENDENT_FIELDS:
            show = key in visible
            label, field = self._rows[key]
            label.setVisible(show)
            field.setVisible(show)
        self._update_friction_visibility()
        self.lblLoadNote.setText(STAGE_LOAD_NOTE.get(stage_type, ""))

    def _update_friction_visibility(self, *_):
        show = (self.cbType.currentData() == "dynamic"
                and bool(self.cbContact.currentData()))
        label, field = self._rows["friction"]
        label.setVisible(show)
        field.setVisible(show)

    def _update_dt_label(self):
        if self.dt_provider is None:
            self.lblDt.setText("—")
            return
        try:
            # En consolidación el proveedor usa la onda no drenada (Kw/n0)
            dt = self.dt_provider(self.spCourant.value(), self.cbType.currentData())
        except Exception:
            dt = None
        if dt is None:
            self.lblDt.setText("— (selecciona puntos materiales en Ejecutar)")
        else:
            self.lblDt.setText(f"≈ {dt:.3e} s")

    @staticmethod
    def _set_combo_data(combo, value):
        for i in range(combo.count()):
            if combo.itemData(i) == value:
                combo.setCurrentIndex(i)
                return
        combo.setCurrentIndex(0)

    # ------------------------------------------------------------- OK
    def _on_accept(self):
        # Asegurar que lo editado en el form esté volcado
        self._write_form_into_selected()

        # Validaciones mínimas
        if not self._stages:
            QMessageBox.warning(self, "Etapas", "Debe existir al menos una etapa.")
            return
        for i, s in enumerate(self._stages):
            tipo = s.get("TIPO")
            n = i + 1
            if tipo in ("dynamic", "consolidation") and float(s.get("TIEMPOANALISIS", 0)) <= 0:
                QMessageBox.warning(self, "Etapas",
                    f"Etapa {n}: la duración debe ser mayor que 0.")
                return
            if tipo in ("geostatic", "load_increment") and int(s.get("NUMEROINCREMENTOS", 0)) < 1:
                QMessageBox.warning(self, "Etapas",
                    f"Etapa {n}: el número de incrementos debe ser ≥ 1.")
                return

        # Si se quitaron etapas, la opción de reanudar puede haber quedado fuera de rango
        if self._resume_from > len(self._stages):
            self._resume_from = 0

        self.model_current_project.updateStages(self._stages)
        self.model_current_project.updateResumeFrom(self._resume_from)
        self.model_current_project.updateConfig(gravity=self.spGravity.value())
        self.model_current_project.updateFps(self.spFps.value())
        self.accept()

    def getStages(self):
        """Retorna las etapas configuradas (útil tras exec())."""
        return self._stages
