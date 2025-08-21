# Modal GPU Functions for MCP

GPU-accelerated browser automation and AI processing functions deployed on Modal Labs infrastructure.

## Overview

This module provides GPU-accelerated versions of MCP browser automation tasks that require significant computational resources. When the local MCP server encounters heavy tasks, it can offload them to these Modal functions.

## Functions

### GPU-Accelerated Functions

#### `heavy_browser_automation` (GPU: T4)
- Complex browser interactions with AI vision
- Multi-step workflows requiring GPU processing
- Advanced form recognition and interaction
- **Use case**: Complex e-commerce automation, advanced web testing

#### `deep_web_research` (GPU: A10G)
- Large-scale web research with AI analysis
- Parallel processing across multiple sites
- Content synthesis and insight generation
- **Use case**: Market research, competitive intelligence

#### `ai_powered_form_filling` (GPU: T4)
- AI-driven form recognition and completion
- Visual understanding of form layouts
- Intelligent field mapping and validation
- **Use case**: Automated application submissions, data entry

#### `multi_site_monitoring` (GPU: A10G)
- Parallel monitoring of multiple websites
- AI-powered anomaly detection
- Performance analysis and recommendations
- **Use case**: Website monitoring, uptime tracking

### CPU-Only Functions

#### `lightweight_web_scraping` (CPU)
- Simple data extraction tasks
- Basic web scraping without AI processing
- Fast, efficient processing for simple tasks
- **Use case**: Basic data collection, content extraction

## Setup

### 1. Install Modal
```bash
pip install modal
```

### 2. Authenticate with Modal
```bash
modal setup
```

### 3. Create Required Secrets
```bash
# Google API key for AI browser automation
modal secret create google-api-key GOOGLE_API_KEY=your_google_api_key_here
```

### 4. Deploy Functions
```bash
python modal/deploy.py
```

## Usage

### Direct Modal Usage
```bash
# Heavy browser automation
modal run modal/mcp_gpu_functions.py::heavy_browser_automation --task "Navigate to shopify.com and extract product data"

# Deep web research  
modal run modal/mcp_gpu_functions.py::deep_web_research --research-topic "AI automation trends 2024" --max-sites 20

# Lightweight scraping
modal run modal/mcp_gpu_functions.py::lightweight_web_scraping --urls '["https://example.com", "https://test.com"]'
```

### Integration with MCP Browser-Use

The Modal functions integrate automatically with your MCP browser-use server. When complex tasks are detected, they're automatically routed to Modal for GPU processing.

#### Local MCP Configuration
Your `.mcp.json` is already configured to work with Modal integration:

```json
{
  "browser-use": {
    "env": {
      "MCP_MODAL_INTEGRATION": "true",
      "MCP_MODAL_APP_NAME": "mcp-gpu-functions",
      "MCP_MODAL_FALLBACK": "local"
    }
  }
}
```

## GPU Selection Guide

| Task Type | Recommended GPU | Reasoning |
|-----------|----------------|-----------|
| Simple browser automation | CPU only | No GPU needed |
| Complex form filling | T4 | Good balance of cost/performance |
| Multi-site research | A10G | Higher memory for parallel processing |
| Large-scale monitoring | A10G | Sustained performance for long tasks |
| Advanced AI analysis | A100 | Maximum performance for heavy AI workloads |

## Cost Optimization

### Automatic Task Routing
The system automatically routes tasks based on complexity:

1. **Simple tasks** → Local CPU processing
2. **Medium complexity** → Modal T4 GPU
3. **High complexity** → Modal A10G GPU
4. **Maximum performance** → Modal A100 GPU (optional)

### Cost Monitoring
```bash
# Monitor Modal usage and costs
modal logs mcp-gpu-functions
modal apps list
```

## Development

### Local Testing
```bash
# Test functions locally (CPU only)
python modal/mcp_gpu_functions.py

# Test deployment script
python modal/deploy.py
```

### Adding New Functions
1. Add function to `mcp_gpu_functions.py`
2. Update routing in `route_mcp_task()`
3. Redeploy with `python modal/deploy.py`
4. Update documentation

### Environment Variables
- `GOOGLE_API_KEY`: Required for AI browser automation
- `MODAL_TOKEN_ID`: Modal authentication (set via `modal setup`)
- `MODAL_TOKEN_SECRET`: Modal authentication (set via `modal setup`)

## Troubleshooting

### Common Issues

#### Authentication Errors
```bash
modal setup
```

#### GPU Quota Limits
- Check Modal dashboard for GPU availability
- Consider using smaller GPU tiers
- Implement retry logic with exponential backoff

#### Memory Issues
- Use A10G or A100 for memory-intensive tasks
- Implement batch processing for large datasets
- Monitor memory usage in Modal logs

#### Network Timeouts
- Increase function timeout values
- Implement chunked processing
- Add retry mechanisms

### Monitoring and Debugging
```bash
# View function logs
modal logs mcp-gpu-functions

# Monitor function performance
modal volume ls
modal apps list

# Debug specific function
modal run modal/mcp_gpu_functions.py::function_name --debug
```

## Integration Examples

### E-commerce Automation
```python
# Automatically routes to GPU for complex product extraction
result = heavy_browser_automation.remote(
    task="Extract all product data from amazon.com search results for 'laptops'",
    config={"max_steps": 100, "use_vision": True}
)
```

### Research Pipeline
```python
# Large-scale research with AI synthesis
research = deep_web_research.remote(
    research_topic="Sustainable technology trends",
    max_sites=50
)
```

### Monitoring Dashboard
```python
# Multi-site monitoring with anomaly detection
monitoring = multi_site_monitoring.remote(
    sites=["site1.com", "site2.com", "site3.com"],
    monitoring_config={"check_interval": 300, "ai_analysis": True}
)
```