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

`dt_provider` (opcional): callable(courant: float) -> float | None
    Devuelve el dt estimado (mínimo entre los materiales seleccionados)
    para el Courant dado, o None si no hay materiales. Solo para display.
"""

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFormLayout, QGridLayout,
    QListWidget, QListWidgetItem, QPushButton, QLineEdit, QComboBox,
    QDoubleSpinBox, QSpinBox, QLabel, QDialogButtonBox, QGroupBox,
    QWidget, QMessageBox,
)
from PySide6.QtCore import Qt


# (etiqueta visible, valor persistido TIPO)
STAGE_TYPES = [
    ("Geostático", "geostatic"),
    ("Incrementos de carga", "load_increment"),
    ("Dinámico", "dynamic"),
]

# Defaults por tipo al crear/cambiar una etapa
STAGE_DEFAULTS = {
    "geostatic":      dict(DAMPING=0.75, COURANT=0.6, PLASTICIDAD=0, GAUSS=True,
                           NUMEROINCREMENTOS=10, DELTAINCREMENTO=0.0, TIEMPOANALISIS=0.0),
    "load_increment": dict(DAMPING=0.75, COURANT=0.1, PLASTICIDAD=1, GAUSS=True,
                           NUMEROINCREMENTOS=10, DELTAINCREMENTO=1.0, TIEMPOANALISIS=0.0),
    "dynamic":        dict(DAMPING=0.05, COURANT=0.1, PLASTICIDAD=1, GAUSS=False,
                           NUMEROINCREMENTOS=1, DELTAINCREMENTO=0.0, TIEMPOANALISIS=1.0),
}

# Campos visibles según tipo
VISIBLE_FIELDS = {
    "geostatic":      {"nincre", "tolff", "tolee"},
    "load_increment": {"nincre", "dincre", "tolff", "tolee"},
    "dynamic":        {"tiempo"},
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


def _new_stage_dict(stage_type="dynamic", name="Etapa"):
    """Crea un dict de etapa con los defaults del tipo."""
    d = STAGE_DEFAULTS[stage_type]
    return {
        "NOMBRE": name,
        "TIPO": stage_type,
        "DAMPING": d["DAMPING"],
        "COURANT": d["COURANT"],
        "NUMEROINCREMENTOS": d["NUMEROINCREMENTOS"],
        "DELTAINCREMENTO": d["DELTAINCREMENTO"],
        "DELTAINCREMENTO_GRAV": 0.0,
        "TIEMPOANALISIS": d["TIEMPOANALISIS"],
        "TOLFF": 0.01,
        "TOLEE": 0.01,
        "PLASTICIDAD": d["PLASTICIDAD"],
        "GAUSS": d["GAUSS"],
    }


class DialogStages(QDialog):

    def __init__(self, model_current_project, dt_provider=None, parent=None):
        super().__init__(parent)
        self.model_current_project = model_current_project
        self.dt_provider = dt_provider
        self._loading = False  # evita write-back mientras se puebla el form

        # Copia editable de las etapas persistidas
        stages = model_current_project.getStages() or []
        self._stages = [dict(s) for s in stages]
        if not self._stages:
            self._stages = [_new_stage_dict("dynamic", "Etapa 1")]

        self.setWindowTitle("Etapas de análisis")
        self.setMinimumSize(640, 470)
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

        # ── Izquierda: lista de etapas + botones ──
        left = QVBoxLayout()
        left.setSpacing(6)
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

        self.spDincre = self._make_dspin(-1e6, 1e6, 1.0, 4)
        self._add_row(form, "dincre", "Δ carga por incremento", self.spDincre)

        self.spTiempo = self._make_dspin(0.0, 1e6, 0.5, 3)
        self._add_row(form, "tiempo", "Duración (s)", self.spTiempo)

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

        self.lblDt = QLabel("—")
        self.lblDt.setObjectName("labelDt")
        self._add_row(form, "dt", "dt estimado", self.lblDt)

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
        stage["DELTAINCREMENTO"] = defaults["DELTAINCREMENTO"]
        stage["TIEMPOANALISIS"] = defaults["TIEMPOANALISIS"]
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
            self.spDincre.setValue(float(stage.get("DELTAINCREMENTO", 0.0)))
            self.spTiempo.setValue(float(stage.get("TIEMPOANALISIS", 0.0)))
            self.spTolFF.setValue(float(stage.get("TOLFF", 0.01)))
            self.spTolEE.setValue(float(stage.get("TOLEE", 0.01)))
            self._set_combo_data(self.cbPlast, int(stage.get("PLASTICIDAD", 1)))
            self._set_combo_data(self.cbGauss, stage.get("GAUSS", None))
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
        stage["DELTAINCREMENTO"] = self.spDincre.value()
        stage["TIEMPOANALISIS"] = self.spTiempo.value()
        stage["TOLFF"] = self.spTolFF.value()
        stage["TOLEE"] = self.spTolEE.value()
        stage["PLASTICIDAD"] = self.cbPlast.currentData()
        stage["GAUSS"] = self.cbGauss.currentData()

    def _apply_type_visibility(self, stage_type):
        visible = VISIBLE_FIELDS.get(stage_type, set())
        for key in ("nincre", "dincre", "tiempo", "tolff", "tolee"):
            show = key in visible
            label, field = self._rows[key]
            label.setVisible(show)
            field.setVisible(show)

    def _update_dt_label(self):
        if self.dt_provider is None:
            self.lblDt.setText("—")
            return
        try:
            dt = self.dt_provider(self.spCourant.value())
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
            if tipo == "dynamic" and float(s.get("TIEMPOANALISIS", 0)) <= 0:
                QMessageBox.warning(self, "Etapas",
                    f"Etapa {n} (dinámica): la duración debe ser mayor que 0.")
                return
            if tipo in ("geostatic", "load_increment") and int(s.get("NUMEROINCREMENTOS", 0)) < 1:
                QMessageBox.warning(self, "Etapas",
                    f"Etapa {n}: el número de incrementos debe ser ≥ 1.")
                return

        self.model_current_project.updateStages(self._stages)
        self.accept()

    def getStages(self):
        """Retorna las etapas configuradas (útil tras exec())."""
        return self._stages
