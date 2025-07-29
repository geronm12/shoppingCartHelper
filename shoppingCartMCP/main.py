from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="Calculadora MCP")


@mcp.tool(name="Sumar", title="Agregar números",
          description="permite operar una suma entre dos números", structured_output=True)
def sum(a: int, b: int) -> int:
    return a + b


@mcp.tool(name="Restar", title="Quitar números",
          description="permite operar una resta entre dos números", structured_output=True)
def rest(a: int, b: int) -> int:
    return a - b


@mcp.tool(name="Multiplicar", title="Multiplicar números",
          description="permite operar una multiplicación entre dos números", structured_output=True)
def multiply(a: int, b: int) -> int:
    return a * b


@mcp.tool(name="Dividir", title="Dividir números",
          description="permite operar una división entre dos números", structured_output=True)
def div(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return a / b
