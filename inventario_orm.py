from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, Session

engine = create_engine("sqlite:///inventario_equipos.db", echo=False)
Base = declarative_base()

class EquipoComputo(Base):
    """Modelo ORM para equipos de cómputo en el inventario."""
    __tablename__ = "equipos"

    nombre = Column(String, primary_key=True)
    cantidad = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Equipo(nombre={self.nombre}, cantidad={self.cantidad}, precio={self.precio})>"


def inicializar_db():
    """Crea las tablas en la base de datos si no existen."""
    Base.metadata.create_all(engine)

def registrar_equipo(nombre: str, cantidad: int, precio: float) -> None:
    """Registra o actualiza un equipo en la base de datos."""
    with Session(engine) as session:
        equipo = session.get(EquipoComputo, nombre)
        if equipo:
            equipo.cantidad = cantidad
            equipo.precio = precio
        else:
            equipo = EquipoComputo(nombre=nombre, cantidad=cantidad, precio=precio)
            session.add(equipo)
        session.commit()
    print(f"Equipo '{nombre}' registrado correctamente.")


def listar_equipos() -> list:
    """Retorna todos los equipos registrados en la base de datos."""
    with Session(engine) as session:
        return session.query(EquipoComputo).all()


def mostrar_equipos() -> None:
    """Imprime el inventario de equipos de cómputo."""
    equipos = listar_equipos()
    if not equipos:
        print("No hay equipos registrados.")
        return
    print("\n" + "=" * 40)
    print("    INVENTARIO DE EQUIPOS DE CÓMPUTO")
    print("=" * 40)
    for eq in equipos:
        print(f"- {eq.nombre}: {eq.cantidad} unidades | S/. {eq.precio:.2f}")


if __name__ == "__main__":
    inicializar_db()
    registrar_equipo("Laptop Dell XPS 14", 5, 4400.0)
    registrar_equipo("Monitor LG 27", 10, 850.0)
    registrar_equipo("Teclado Logitech G512", 88, 55.0)
    registrar_equipo("Mouse Logitech G502", 55, 200.0)
    mostrar_equipos()
