# Say Hello - Smithery MCP Project

A TypeScript project configured with comprehensive Model Context Protocol (MCP) server integrations for enhanced AI-assisted development.

## Features

- **TypeScript Runtime**: Built with Smithery for modern TypeScript development
- **MCP Integration**: Pre-configured with n8n, PythonAnywhere, and Render MCP servers
- **AI-Enhanced Development**: Claude Code integration with specialized tools

## MCP Servers

### Configured Services
1. **n8n-mcp**: Workflow automation platform integration
2. **pythonanywhere-mcp-server**: Python hosting platform management
3. **render**: Cloud deployment and monitoring

### Security
- All API credentials are base64 encoded
- Project-level MCP configuration in `.mcp.json`
- Sensitive data isolation

## Getting Started

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Setup MCP Servers**
   ```bash
   ./scripts/setup-mcp.sh
   ```

3. **Validate MCP Configuration**
   ```bash
   node scripts/validate-mcp.js
   ```

4. **Development**
   ```bash
   npm run dev
   ```

5. **Build**
   ```bash
   npm run build
   ```

## Quick MCP Setup

For immediate MCP server setup with Claude Code:
```bash
# Run the automated setup
chmod +x scripts/setup-mcp.sh && ./scripts/setup-mcp.sh

# Validate configuration
node scripts/validate-mcp.js
```

## MCP Usage

When using Claude Code in this project, you'll have access to:
- n8n workflow development and validation
- PythonAnywhere deployment and management
- Render service deployment and monitoring

See `prompts/mcp-setup.md` for detailed usage instructions.

## Project Structure

```
├── src/           # TypeScript source code
├── prompts/       # MCP setup and usage guides
├── resources/     # MCP tools documentation
├── .mcp.json      # MCP server configuration
├── smithery.yaml  # Smithery configuration
└── package.json   # Node.js dependencies
```