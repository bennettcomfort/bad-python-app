from flask import render_template


def sql_injection_search_v2_page(request, app):
    term = request.args.get('q')

    conn = app.db_helper._get_db_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM products WHERE name LIKE '%{term}%'")
    rows = cur.fetchall()
    conn.close()

    products = [{'id': r[0], 'name': r[1], 'price': r[2]} for r in rows]

    return render_template(
        'sql_injection/search.html',
        sql=term,
        products=products
    )
