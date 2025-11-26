from flask import request, render_template, jsonify, session, redirect, url_for
from app import app, db
from foodmenu.models import FoodMenu
from bson import ObjectId


@app.route('/admin/add-item', methods=['POST'])
def add_food_item():
    fm = FoodMenu()
    return fm.add_item()


@app.route('/admin/menu', methods=['GET'])
def get_menu_items():
    if not session.get('is_admin'):
        return redirect(url_for('login_page'))
    fm = FoodMenu()
    return fm.get_menu()


@app.route('/admin/delete-item', methods=['POST'])
def delete_food_item():
    if not session.get('is_admin'):
        return jsonify({'message': 'Unauthorized'}), 401

    # Accept JSON (AJAX) or form POST (plain HTML form)
    json_payload = request.get_json(silent=True)
    if json_payload:
        db_id = json_payload.get('db_id')
        fm = FoodMenu()
        return fm.delete_item(db_id=db_id)

    # fallback for form submission: perform deletion and redirect back to view
    form_data = request.form.to_dict() or {}
    db_id = form_data.get('db_id')
    if not db_id:
        return redirect(url_for('view_page'))

    fm = FoodMenu()
    # perform deletion (fm.delete_item returns a JSON response, but we redirect for form UX)
    try:
        fm.delete_item(db_id=db_id)
    except Exception:
        pass
    return redirect(url_for('view_page'))





@app.route('/admin/update', methods=['POST'])
def admin_update_submit():
    if not session.get('is_admin'):
        return redirect(url_for('login_page'))

    db_id = request.form.get('db_id')
    # Collect partial updates from the form. Only include fields that were provided (non-empty).
    allowed = ['name', 'description', 'price', 'img', 'specialday']
    updates = {}
    for key in allowed:
        if key in request.form:
            val = request.form.get(key)
            # empty string means "don't change" for specialday; for other fields skip if empty
            if val is None or val == '':
                continue
            updates[key] = val

    # Try to coerce price to number if included
    if 'price' in updates:
        try:
            updates['price'] = float(updates['price'])
        except Exception:
            # leave as-is if conversion fails
            pass

    if db_id and updates:
        db.foodmenu.update_one({'_id': ObjectId(db_id)}, {'$set': updates})
    return redirect(url_for('view_page'))
