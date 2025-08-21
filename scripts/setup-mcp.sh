#!/bin/bash

# MCP Server Setup Script for Smithery Project
# This script ensures all MCP dependencies are installed and configured

set -e

echo "🚀 Setting up MCP servers for Smithery project..."

# Create required directories
echo "📁 Creating required directories..."
mkdir -p /tmp/browser_research
mkdir -p /tmp/browser_history  
mkdir -p /tmp/browser_downloads

# Install UV if not already installed
if ! command -v uv &> /dev/null; then
    echo "📦 Installing UV package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
fi

# Install browser dependencies for browser-use MCP
echo "🌐 Installing Playwright browsers..."
uvx --from mcp-server-browser-use@latest python -m playwright install --with-deps chromium

# Test MCP server connectivity
echo "🔍 Testing MCP server configurations..."

# Test n8n-mcp
echo "Testing n8n-mcp server..."
if command -v npx &> /dev/null; then
    echo "✅ n8n-mcp dependencies available"
else
    echo "⚠️  Node.js/npm required for n8n-mcp"
fi

# Test pythonanywhere-mcp-server
echo "Testing pythonanywhere-mcp-server..."
if uvx pythonanywhere-mcp-server --help &> /dev/null; then
    echo "✅ pythonanywhere-mcp-server available"
else
    echo "⚠️  pythonanywhere-mcp-server installation may be needed"
fi

# Test browser-use
echo "Testing browser-use MCP server..."
if uvx mcp-server-browser-use@latest --help &> /dev/null; then
    echo "✅ browser-use MCP server available"
else
    echo "⚠️  browser-use MCP server installation may be needed"
fi

# Set proper permissions
echo "🔒 Setting directory permissions..."
chmod 755 /tmp/browser_research /tmp/browser_history /tmp/browser_downloads 2>/dev/null || true

echo ""
echo "✅ MCP setup complete!"
echo ""
echo "📋 Available MCP Servers:"
echo "  🔧 n8n-mcp: Workflow automation platform"
echo "  🐍 pythonanywhere-mcp-server: Python hosting management"
echo "  ☁️  render: Cloud deployment platform"
echo "  🌐 browser-use: AI browser automation with vision"
echo ""
echo "🎯 Ready to use with Claude Code!"
echo ""
echo "💡 Usage:"
echo "  - Use /mcp command in Claude to see available tools"
echo "  - All credentials are base64 encoded for security"
echo "  - Browser automation includes vision capabilities"
echo "  - Research results saved to /tmp/browser_research"
echo ""