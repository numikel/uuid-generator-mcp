# UUID Generator MCP

UUID Generator MCP is a Model Context Protocol (MCP) server for generating universally unique identifiers (UUIDs) with seamless AI assistant integration.

## ✨ Features

✅ **Simple UUID Generation** - Generate RFC 4122 compliant UUIDs using Python's cryptographically secure uuid4()
✅ **MCP Integration** - Built on FastMCP framework for seamless integration with MCP-compatible AI applications
✅ **Fast and Reliable** - Lightweight implementation with minimal dependencies and instant UUID generation
✅ **Python Native** - Leverages Python's built-in uuid module for industry-standard UUID creation

## Quick Start

1. **Install MCP server in your AI tool**

   👉 Guidelines for most popular AI Tools below

2. **Ask your AI assistant:**

   > "Please generate me a uuid with available tools"

## Installation & setup

- [Cursor IDE](#cursor-ide)
- [Claude Code](#claude-code)
- [Other tools](#other-tools)

### Cursor IDE

Add the following configuration to your `.cursor/mcp.json` file:

```json
{
  "mcpServers": {
    "generate-uuid-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/numikel/uuid-generator-mcp",
        "generate-uuid"
      ],
      "transport": "stdio"
    }
  }
}
```

### Claude Code

**Run the following command in your project directory:**

```
claude mcp add generate-uuid-mcp uvx '--from' 'git+https://github.com/numikel/uuid-generator-mcp' 'generate-uuid'
```

You can alternatively create `.mcp.json` file in your project directory with the following content:

```json
{
  "mcpServers": {
    "generate-uuid-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/numikel/uuid-generator-mcp",
        "generate-uuid"
      ],
      "transport": "stdio"
    }
  }
}
```

### Other tools

For other MCP-compatible tools, create an `mcp_config.json` file in your project's root directory:

```json
{
  "mcpServers": {
    "generate-uuid-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "git+https://github.com/numikel/uuid-generator-mcp",
        "generate-uuid"
      ],
      "transport": "stdio"
    }
  }
}
```

## Usage

Once installed and configured, you can invoke the tool by asking your AI assistant:

> "Please generate me a uuid with available tools"

## Output Format

The tool generates RFC 4122 compliant UUID4 strings:

```
550e8400-e29b-41d4-a716-446655440000
```

## Development

### Prerequisites

```bash
# Python 3.12 or higher
# Package Manager: uv
```

### Development mode

```bash
# Using uv
uv run app.py

# Or using the installed script
generate-uuid
```

## 📁 Project structure

```
uuid-generator-mcp/
├── app.py                  # Main MCP server implementation with UUID generation tool
├── pyproject.toml          # Project configuration, dependencies, and CLI script definition
├── uv.lock                 # Lock file for uv package manager ensuring reproducible builds
└── README.md               # Project documentation
```

## 🛠️ Development

### Development commands

```bash
# Run the server in development mode
uv run app.py

# Or use the script
generate-uuid
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Author

[@numikel](https://github.com/numikel)

## Repository

[https://github.com/numikel/uuid-generator-mcp](https://github.com/numikel/uuid-generator-mcp)
