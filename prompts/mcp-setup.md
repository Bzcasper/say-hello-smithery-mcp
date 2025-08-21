# MCP Server Setup Guide

This project includes Model Context Protocol (MCP) server configurations for enhanced AI assistant capabilities.

## Available MCP Servers

### 1. n8n-mcp
- **Purpose**: n8n workflow automation platform integration
- **Features**: Node documentation, workflow validation, API management
- **Configuration**: Uses base64 encoded API credentials

### 2. pythonanywhere-mcp-server
- **Purpose**: PythonAnywhere hosting platform integration
- **Features**: File management, web app deployment, console access
- **Configuration**: Uses base64 encoded API token

### 3. render
- **Purpose**: Render cloud platform integration
- **Features**: Deployment management, service monitoring
- **Configuration**: HTTP transport with bearer token authentication

## Usage with Claude Code

The MCP servers are configured in `.mcp.json` and will be automatically loaded when using Claude Code in this project.

### Available Commands
- Search and explore n8n nodes
- Validate workflow configurations
- Manage PythonAnywhere applications
- Deploy and monitor Render services

## Security Notes
- All API credentials are base64 encoded
- Credentials are stored in project-level configuration
- Use environment variables for sensitive data in production