from flask import Blueprint, render_template, request, redirect
from app.models.inventario_model import productos

inventario_bp = Blueprint('inventario', __name__)

@inventario_bp.route('/inventario')
def inventario():
    query = request.args.get('q', '').lower()

    if query:
        filtrados = [
            p for p in productos
            if query in p["nombre"].lower() or query in p["categoria"].lower()
        ]
    else:
        filtrados = productos

    return render_template(
        'modulos/inventario/inventario.html',
        productos=filtrados,
        busqueda=query
    )

@inventario_bp.route('/inventario/crear', methods=['POST'])
def crear_producto():
    nuevo = {
        "id": len(productos) + 1,
        "nombre": request.form['nombre'],
        "precio": float(request.form['precio']),
        "stock": int(request.form['stock']),
        "min": int(request.form['min']),
        "categoria": request.form['categoria']
    }
    productos.append(nuevo)
    return redirect('/inventario')

@inventario_bp.route('/inventario/editar/<int:id>', methods=['POST'])
def editar_producto(id):
    producto = next((p for p in productos if p["id"] == id), None)

    if producto:
        producto['nombre'] = request.form['nombre']
        producto['precio'] = float(request.form['precio'])
        producto['stock'] = int(request.form['stock'])
        producto['min'] = int(request.form['min'])
        producto['categoria'] = request.form['categoria']

    return redirect('/inventario')

@inventario_bp.route('/inventario/eliminar/<int:id>')
def eliminar_producto(id):
    global productos
    productos = [p for p in productos if p["id"] != id]
    return redirect('/inventario')