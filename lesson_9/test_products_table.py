from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:c9e1x40a@localhost:5432/QA"


def test_db_connection():
    # Используем инспектор для получения информации о таблицах
    db = create_engine(db_connection_string)
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[0] == 'products'


def test_insert():
    engine = create_engine(db_connection_string)
    sql = text(
        "INSERT INTO products (art, product, category)"
        "VALUES (:art, :product, :category)"
        )
    params = {'art': 'A13', 'product': 'Laptop', 'category': 'Electro'}
    with engine.connect() as connection:
        with connection.begin():
            connection.execute(sql, params)
        result = connection.execute(text(
            "SELECT * FROM products WHERE art = :art"), {'art': 'A13'})
        rows = result.mappings().all()
        # Проверка, что запись добавлена
        assert rows[0]['product'] == 'Laptop'


def test_update():
    engine = create_engine(db_connection_string)
    sql = text("UPDATE products SET product = :product where art = :art")
    params = {'product': 'phone', 'art': 'A13'}
    with engine.connect() as connection:
        with connection.begin():
            connection.execute(sql, params)
        result = connection.execute(text(
            "SELECT * FROM products WHERE art = :art"), {'art': 'A13'})
        rows = result.mappings().all()
        # Проверка, что запись отредактированна
        assert rows[0]['product'] == 'phone'


def test_delete():
    engine = create_engine(db_connection_string)
    sql = text("DELETE FROM products WHERE art = :art")
    params = {'art': 'A13'}
    with engine.connect() as connection:
        with connection.begin():
            connection.execute(sql, params)
        result = connection.execute(text("SELECT * FROM products"))
        rows = result.mappings().all()
        # Проверка, что запись удалена
        assert all(row['art'] != 'A13' for row in rows)
