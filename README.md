# 🎯 UUID Generator MCP

A simple and efficient Model Context Protocol (MCP) server for generating universally unique identifiers (UUIDs).

## 📊 Badges

![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-0.1.0-orange.svg)

## ✨ Features

✅ **Simple UUID Generation** - Generate RFC 4122 compliant UUIDs using Python's uuid4()  
✅ **MCP Integration** - Built on FastMCP framework for seamless integration with MCP-compatible applications  
✅ **Fast and Reliable** - Lightweight implementation with minimal dependencies  
✅ **Python Native** - Leverages Python's built-in uuid module for cryptographically secure generation  

## 🔧 Requirements / Prerequisites

- **Python**: 3.12 or higher
- **Package Manager**: uv (recommended) or pip

## 📦 Installation

### Using uv (Recommended)

```bash
cd uuid-generator-mcp
uv sync
```

### Using pip

```bash
cd uuid-generator-mcp
pip install -r requirements.txt
```

## ⚙️ Configuration

No additional configuration is required. The MCP server runs with default settings and generates UUIDs on-demand.

## 🚀 Quick Start / Usage

### Running the MCP Server

```bash
python main.py
```

### Using the UUID Generation Tool

Once the MCP server is running, you can use the `generate_uuid` tool to create new UUIDs:

```python
# The server exposes a single tool: generate_uuid()
# Returns a string representation of a UUID4
uuid = generate_uuid()  # Example: "550e8400-e29b-41d4-a716-446655440000"
```

## 📁 Project Structure

```
uuid-generator-mcp/
├── main.py              # Main MCP server implementation
├── pyproject.toml       # Project configuration and dependencies
├── uv.lock             # Lock file for uv package manager
└── README.md           # This file
```

## 🛠️ Development

### Running Tests

```bash
# No tests are currently implemented
# Add tests in a future version
```

### Code Quality

```bash
# Install development dependencies (if added)
uv sync --dev

# Run linters/formatters (when configured)
# black . && isort . && flake8 .
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/new-feature`)
3. **Commit** your changes using Conventional Commits (`feat: add new-feature`)
4. **Push** to the branch (`git push origin feature/new-feature`)
5. **Open** a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

[@numikel](https://github.com/numikel)
