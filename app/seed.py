from app.database import SessionLocal, init_db
from app.models import Area, Categoria, Responsable

def cargar_datos_iniciales():
    init_db()
    db = SessionLocal()

    # 1. Áreas de ejemplo
    if db.query(Area).count() == 0:
        areas = [
            Area(nombre="Alumbrado Público", descripcion="Mantenimiento de luminarias y red eléctrica"),
            Area(nombre="Parques y Jardines", descripcion="Cuidado de áreas verdes y parques"),
            Area(nombre="Barrido Manual", descripcion="Limpieza e higiene de vialidades"),
            Area(nombre="Taller Mecánico", descripcion="Mantenimiento del parque vehicular"),
            Area(nombre="Administración", descripcion="Gestión administrativa y suministros de oficina"),
        ]
        db.add_all(areas)
        db.commit()
        print("✅ Áreas creadas exitosamente.")

    # 2. Categorías de ejemplo
    if db.query(Categoria).count() == 0:
        categorias = [
            Categoria(nombre="Material Eléctrico", descripcion="Cables, balastros, focos, fotoceldas"),
            Categoria(nombre="Herramientas", descripcion="Pinzas, martillos, desarmadores, llaves"),
            Categoria(nombre="Productos de Limpieza", descripcion="Jabón, cloro, escobas, bolsas"),
            Categoria(nombre="Ferretería", descripcion="Tornillería, cintas, conexiones"),
            Categoria(nombre="Papelería y Consumibles", descripcion="Hojas, tóner, carpetas"),
        ]
        db.add_all(categorias)
        db.commit()
        print("✅ Categorías creadas exitosamente.")

    db.close()

if __name__ == "__main__":
    cargar_datos_iniciales()
