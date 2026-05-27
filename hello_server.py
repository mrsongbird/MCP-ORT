from fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool
def say_hello(name: str) -> str:
    """Devolver un saludo personalizado"""
    return f"Hola, {name}!, soy Pedro el MCP, ¿cómo estás el día de hoy?"

if __name__ == "__main__":
    mcp.run()