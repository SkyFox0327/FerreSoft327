from flask import Blueprint, render_template, request, redirect, session
import bcrypt

login_bp = Blueprint('login', __name__)

# Simulación de usuarios (luego puedes conectar a BD)
usuarios = {
    "admin@ferresoft.com": {
        "password": bcrypt.hashpw("admin123".encode(), bcrypt.gensalt()),
        "rol": "admin"
    },
    "operario@ferresoft.com": {
        "password": bcrypt.hashpw("operario123".encode(), bcrypt.gensalt()),
        "rol": "operario"
    },
    "contador@ferresoft.com": {
        "password": bcrypt.hashpw("contador123".encode(), bcrypt.gensalt()),
        "rol": "contador"
    },
    "vendedor@ferresoft.com": {
        "password": bcrypt.hashpw("vendedor123".encode(), bcrypt.gensalt()),
        "rol": "vendedor"
    }
}

# Vista login
@login_bp.route('/')
def login():
    return render_template('modulos/login/login.html')

# Procesar login
@login_bp.route('/login', methods=['POST'])
def login_post():
    usuario = request.form['usuario']
    password = request.form['password']

    if usuario in usuarios:
        if bcrypt.checkpw(password.encode(), usuarios[usuario]['password']):
            session['usuario'] = usuario
            session['rol'] = usuarios[usuario]['rol']
            return redirect('/inicio')
        else:
            return render_template('modulos/login/login.html', error="Contraseña incorrecta")

    return render_template('modulos/login/login.html', error="Usuario no encontrado")

# Logout
@login_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')