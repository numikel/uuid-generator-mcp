from fastmcp import FastMCP
from uuid import uuid4

mcp = FastMCP("uuid-generator-mcp")

@mcp.tool
def generate_uuid() -> str:
    return str(uuid4())

def main():
    """Main function for the CLI script"""
    print(generate_uuid())

if __name__ == "__main__":
    mcp.run()