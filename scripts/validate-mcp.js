#!/usr/bin/env node

/**
 * MCP Configuration Validator
 * Validates .mcp.json configuration and tests server connectivity
 */

const fs = require('fs');
const path = require('path');

const CONFIG_PATH = path.join(__dirname, '..', '.mcp.json');

// ANSI color codes
const colors = {
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  reset: '\x1b[0m',
  bold: '\x1b[1m'
};

function log(message, color = 'reset') {
  console.log(`${colors[color]}${message}${colors.reset}`);
}

function validateMCPConfig() {
  log('🔍 Validating MCP Configuration...', 'blue');
  
  try {
    // Check if config file exists
    if (!fs.existsSync(CONFIG_PATH)) {
      log('❌ .mcp.json file not found!', 'red');
      return false;
    }
    
    // Parse configuration
    const configData = fs.readFileSync(CONFIG_PATH, 'utf8');
    const config = JSON.parse(configData);
    
    log('✅ Configuration file found and parsed successfully', 'green');
    
    // Validate structure
    if (!config.mcpServers) {
      log('❌ Missing mcpServers section in configuration', 'red');
      return false;
    }
    
    const servers = Object.keys(config.mcpServers);
    log(`📊 Found ${servers.length} MCP servers configured:`, 'blue');
    
    let allValid = true;
    
    // Validate each server
    for (const [serverName, serverConfig] of Object.entries(config.mcpServers)) {
      log(`\n🔧 Validating ${serverName}:`, 'yellow');
      
      // Check required fields
      if (serverConfig.transport === 'http') {
        // HTTP transport validation
        if (!serverConfig.url) {
          log(`  ❌ Missing URL for HTTP transport`, 'red');
          allValid = false;
        } else {
          log(`  ✅ URL: ${serverConfig.url}`, 'green');
        }
        
        if (serverConfig.headers) {
          log(`  ✅ Headers configured`, 'green');
        }
      } else {
        // Stdio transport validation
        if (!serverConfig.command) {
          log(`  ❌ Missing command for stdio transport`, 'red');
          allValid = false;
        } else {
          log(`  ✅ Command: ${serverConfig.command}`, 'green');
        }
        
        if (serverConfig.args && serverConfig.args.length > 0) {
          log(`  ✅ Args: ${serverConfig.args.join(' ')}`, 'green');
        }
        
        if (serverConfig.env) {
          const envKeys = Object.keys(serverConfig.env);
          log(`  ✅ Environment variables: ${envKeys.length} configured`, 'green');
          
          // Check for base64 encoded credentials
          const credentialKeys = envKeys.filter(key => 
            key.includes('API_KEY') || key.includes('TOKEN') || key.includes('PASSWORD')
          );
          
          for (const key of credentialKeys) {
            const value = serverConfig.env[key];
            if (isBase64(value)) {
              log(`  🔒 ${key}: Base64 encoded (secure)`, 'green');
            } else {
              log(`  ⚠️  ${key}: Plain text (consider base64 encoding)`, 'yellow');
            }
          }
        }
      }
    }
    
    // Server-specific validations
    validateServerSpecifics(config.mcpServers);
    
    if (allValid) {
      log('\n✅ All MCP server configurations are valid!', 'green');
      return true;
    } else {
      log('\n❌ Some configuration issues found', 'red');
      return false;
    }
    
  } catch (error) {
    log(`❌ Error validating configuration: ${error.message}`, 'red');
    return false;
  }
}

function validateServerSpecifics(servers) {
  log('\n🔍 Server-specific validations:', 'blue');
  
  // n8n-mcp validation
  if (servers['n8n-mcp']) {
    const env = servers['n8n-mcp'].env || {};
    if (env.N8N_API_URL && env.N8N_API_KEY) {
      log('  ✅ n8n-mcp: API configuration present', 'green');
    } else {
      log('  ⚠️  n8n-mcp: Missing API configuration (will run in limited mode)', 'yellow');
    }
  }
  
  // browser-use validation
  if (servers['browser-use']) {
    const env = servers['browser-use'].env || {};
    if (env.MCP_LLM_GOOGLE_API_KEY || env.MCP_LLM_OPENAI_API_KEY || env.MCP_LLM_API_KEY) {
      log('  ✅ browser-use: LLM API key configured', 'green');
    } else {
      log('  ❌ browser-use: No LLM API key found', 'red');
    }
    
    if (env.MCP_AGENT_TOOL_USE_VISION === 'true') {
      log('  ✅ browser-use: Vision capabilities enabled', 'green');
    }
    
    if (env.MCP_RESEARCH_TOOL_SAVE_DIR) {
      log('  ✅ browser-use: Research save directory configured', 'green');
    }
  }
  
  // pythonanywhere validation
  if (servers['pythonanywhere-mcp-server']) {
    const env = servers['pythonanywhere-mcp-server'].env || {};
    if (env.API_TOKEN && env.LOGNAME) {
      log('  ✅ pythonanywhere-mcp-server: API credentials configured', 'green');
    } else {
      log('  ❌ pythonanywhere-mcp-server: Missing API credentials', 'red');
    }
  }
  
  // render validation
  if (servers['render']) {
    if (servers['render'].headers && servers['render'].headers.Authorization) {
      log('  ✅ render: Authorization header configured', 'green');
    } else {
      log('  ❌ render: Missing authorization header', 'red');
    }
  }
}

function isBase64(str) {
  try {
    return btoa(atob(str)) === str;
  } catch (err) {
    return false;
  }
}

function generateSummary(config) {
  log('\n📊 Configuration Summary:', 'bold');
  
  const servers = Object.keys(config.mcpServers);
  const httpServers = servers.filter(name => config.mcpServers[name].transport === 'http');
  const stdioServers = servers.filter(name => config.mcpServers[name].transport !== 'http');
  
  log(`  Total servers: ${servers.length}`, 'blue');
  log(`  HTTP transport: ${httpServers.length}`, 'blue');
  log(`  Stdio transport: ${stdioServers.length}`, 'blue');
  
  log('\n🔧 Server capabilities:', 'bold');
  log('  🔧 n8n-mcp: Workflow automation, API management', 'green');
  log('  🐍 pythonanywhere-mcp-server: Python hosting, file management', 'green');
  log('  ☁️  render: Cloud deployment, monitoring', 'green');
  log('  🌐 browser-use: AI browser automation, web research', 'green');
}

// Main execution
if (require.main === module) {
  log('🚀 MCP Configuration Validator', 'bold');
  log('=' * 50, 'blue');
  
  const isValid = validateMCPConfig();
  
  if (isValid) {
    const config = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
    generateSummary(config);
    
    log('\n🎯 Ready for Claude Code integration!', 'green');
    log('\n💡 Next steps:', 'yellow');
    log('  1. Restart Claude Code if already running', 'yellow');
    log('  2. Use /mcp command to see available tools', 'yellow');
    log('  3. Test each server with simple commands', 'yellow');
    
    process.exit(0);
  } else {
    log('\n🔧 Please fix configuration issues before proceeding', 'red');
    process.exit(1);
  }
}