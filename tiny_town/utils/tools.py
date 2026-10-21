from langchain.tools import tool

@tool
def buscar_cliente(rut:str) -> str:
    """
    Busca un cliente por su RUT en la base de datos.

    Args:
        rut (str): El RUT del cliente a buscar.

    Returns:
        str: Información del cliente si se encuentra, de lo contrario un mensaje indicando que no se encontró.
    """
    # Aquí iría la lógica para buscar el cliente en la base de datos.
    # Por ahora, devolvemos un mensaje simulado.
    return f"Información del cliente con RUT {rut}: [Nombre: Juan Pérez, Edad: 30, Dirección: Calle Falsa 123]"


tools = [buscar_cliente]