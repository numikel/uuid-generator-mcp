from fastmcp import FastMCP
from uuid import uuid4

mcp = FastMCP("uuid-generator-mcp")

@mcp.tool
def generate_uuid() -> str:
    return str(uuid4())

def main():
    mcp.run()

if __name__ == "__main__":
    main()