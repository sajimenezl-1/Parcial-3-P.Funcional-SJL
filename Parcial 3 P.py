# Datos de ejemplo: lista de nombres
nombres = ["Santiago", "Juan", "Carlos", "Ana", "Valentina", "Franco", "Lina", "Alejandro"]

# Función pura para filtrar nombres con más de 5 letras
def filtrar_nombre_xl(nombres):
    return list(filter(lambda nombre: len(nombre) > 5, nombres))

# Función pura para convertir nombres a mayúsculas
def convertir_mayus(nombres):
    return list(map(lambda nombre: nombre.upper(), nombres))

# Función pura para contar elementos en una lista
def contar_elem(nombres):
    return len(nombres)

# Función principal que combina las operaciones
def combinar_op(nombres):
    nlargo = filtrar_nombre_xl(nombres)
    nombre_mayus = convertir_mayus(nlargo)
    total_nombres = contar_elem(nombre_mayus)

    return {
        "nlargo": nlargo,
        "nombre_mayus": nombre_mayus,
        "total_nombres": total_nombres,
    }

# Ejecución del programa
if __name__ == "__main__":
    result = combinar_op(nombres)

    print("Nombres originales:", nombres)
    print("Nombres con más de 5 letras:", result["nlargo"])
    print("Nombres en mayúsculas:", result["nombre_mayus"])
    print("Total de nombres que cumplen la condición:", result["total_nombres"])