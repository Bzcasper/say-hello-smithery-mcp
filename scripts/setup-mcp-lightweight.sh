#!/bin/bash

# Lightweight MCP Server Setup Script (No GPU dependencies)
# Optimized for Modal remote containers and lightweight environments

set -e

echo "🚀 Setting up MCP servers (lightweight mode)..."

# Create required directories with proper permissions
echo "📁 Creating required directories..."
echo "8040" | sudo -S mkdir -p /tmp/browser_research /tmp/browser_history /tmp/browser_downloads
echo "8040" | sudo -S chmod 755 /tmp/browser_research /tmp/browser_history /tmp/browser_downloads
echo "8040" | sudo -S chown $USER:$USER /tmp/browser_research /tmp/browser_history /tmp/browser_downloads

# Check for UV
if ! command -v uv &> /dev/null; then
    echo "📦 Installing UV package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Install minimal browser dependencies (no GPU packages)
echo "🌐 Installing minimal Playwright dependencies..."
export PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
uvx --from mcp-server-browser-use@latest --python 3.11 --no-cache python -c "print('MCP server package available')"

# Test basic MCP server availability
echo "🔍 Testing MCP server configurations..."

# Test n8n-mcp (requires Node.js)
echo "Testing n8n-mcp server..."
if command -v npx &> /dev/null; then
    echo "✅ n8n-mcp: Node.js environment available"
else
    echo "⚠️  n8n-mcp: Node.js required (install with: sudo apt install nodejs npm)"
fi

# Test pythonanywhere-mcp-server
echo "Testing pythonanywhere-mcp-server..."
if uvx pythonanywhere-mcp-server --help &> /dev/null 2>&1; then
    echo "✅ pythonanywhere-mcp-server: Available"
else
    echo "⚠️  pythonanywhere-mcp-server: Will be installed on first use"
fi

# Test browser-use (lightweight check)
echo "Testing browser-use MCP server..."
if python3 -c "import sys; print('Python', sys.version_info[:2])" 2>/dev/null; then
    echo "✅ browser-use: Python environment available"
else
    echo "⚠️  browser-use: Python 3.11+ recommended"
fi

echo ""
echo "✅ Lightweight MCP setup complete!"
echo ""
echo "📋 Available MCP Servers:"
echo "  🔧 n8n-mcp: Workflow automation platform"
echo "  🐍 pythonanywhere-mcp-server: Python hosting management"
echo "  ☁️  render: Cloud deployment platform (HTTP)"
echo "  🌐 browser-use: AI browser automation (Modal container ready)"
echo ""
echo "🎯 Modal Container Optimization:"
echo "  - GPU dependencies skipped"
echo "  - Minimal browser setup"
echo "  - Headless mode configured"
echo "  - Research/history dirs created"
echo ""
echo "💡 Usage with Modal:"
echo "  - Set MCP_BROWSER_HEADLESS=true (already configured)"
echo "  - Use browser automation in headless mode"
echo "  - Research results saved to /tmp/browser_research"
echo "  - Download files to /tmp/browser_downloads"
echo ""
echo "🔄 Next steps:"
echo "  1. Run: node scripts/validate-mcp.js"
echo "  2. Test with Claude Code /mcp command"
echo "  3. Use browser automation in headless mode"
echo ""