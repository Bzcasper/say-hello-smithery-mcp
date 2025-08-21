import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Test Smithery MCP deployment
async function testSmitheryMCP() {
  try {
    const response = await openai.responses.create({
      model: "gpt-4.1",
      input: [
        {
          role: "user",
          content: "Hello! Can you help me test the MCP server integration? Please use the /mcp command to show available tools."
        }
      ],
      text: {
        "format": {
          "type": "text"
        }
      },
      reasoning: {},
      tools: [
        {
          "type": "mcp",
          "server_label": "Smithery MCP Server",
          "server_url": "https://17b5628c.ngrok.smithery.ai/mcp",
          "allowed_tools": [], // Allow all tools
          "require_approval": "never" // Auto-approve for testing
        }
      ],
      temperature: 0.3,
      max_output_tokens: 4096,
      top_p: 1,
      store: true
    });

    console.log("🎉 Smithery MCP Response:");
    console.log(response.choices[0].message.content);
    return response;
    
  } catch (error) {
    console.error("❌ MCP Test Error:", error.message);
    return null;
  }
}

// Test individual MCP tools
async function testMCPTools() {
  const tools = [
    {
      name: "search_nodes",
      description: "Test n8n node search",
      input: "Search for HTTP Request nodes"
    },
    {
      name: "list_files", 
      description: "Test PythonAnywhere file listing",
      input: "List files in home directory"
    },
    {
      name: "list_services",
      description: "Test Render service listing", 
      input: "List deployed services"
    },
    {
      name: "run_browser_agent",
      description: "Test browser automation",
      input: "Navigate to example.com and get the page title"
    }
  ];

  console.log("🧪 Testing Individual MCP Tools:");
  console.log("=".repeat(50));

  for (const tool of tools) {
    try {
      const response = await openai.responses.create({
        model: "gpt-4.1",
        input: [
          {
            role: "user",
            content: `Please use the ${tool.name} tool to: ${tool.input}`
          }
        ],
        tools: [
          {
            "type": "mcp",
            "server_label": "Smithery MCP Server",
            "server_url": "https://17b5628c.ngrok.smithery.ai/mcp",
            "allowed_tools": [tool.name],
            "require_approval": "never"
          }
        ],
        temperature: 0.1,
        max_output_tokens: 2048
      });

      console.log(`✅ ${tool.description}:`);
      console.log(response.choices[0].message.content);
      console.log("-".repeat(30));
      
    } catch (error) {
      console.log(`❌ ${tool.description} failed:`, error.message);
    }
  }
}

// Main test execution
async function main() {
  console.log("🚀 Smithery MCP Integration Test");
  console.log("=".repeat(50));
  
  // Test basic MCP connection
  await testSmitheryMCP();
  
  console.log("\n");
  
  // Test individual tools
  await testMCPTools();
  
  console.log("\n🎯 MCP Test Complete!");
  console.log("📋 Available MCP Servers:");
  console.log("  🔧 n8n-mcp: Workflow automation");
  console.log("  🐍 pythonanywhere-mcp-server: Python hosting");
  console.log("  ☁️  render: Cloud deployment");
  console.log("  🌐 browser-use: AI browser automation");
}

// Export for module use
export { testSmitheryMCP, testMCPTools };

// Run if called directly
if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch(console.error);
}