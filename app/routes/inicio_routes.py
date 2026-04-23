from flask import Blueprint, render_template, session, redirect
from datetime import datetime

inicio_bp = Blueprint('inicio', __name__)

@inicio_bp.route('/inicio')
def inicio():
    if 'usuario' in session:
        fecha = datetime.now().strftime("%A, %d de %B de %Y")

        # Datos simulados (luego los conectas a BD)
        data = {
            "ventas": 2748900,
            "productos": 425,
            "facturas": 5,
            "alertas": 1,
            "servicios": 158
        }

        return render_template(
            'modulos/inicio/inicio.html',
            usuario=session['usuario'],
            fecha=fecha,
            data=data
        )
    return redirect('/')