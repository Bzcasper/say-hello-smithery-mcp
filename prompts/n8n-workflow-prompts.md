# n8n Workflow Development Prompts

## Quick Start Prompts

### Basic Workflow Creation
```
Create a simple n8n workflow that:
1. Triggers on a webhook
2. Processes incoming data
3. Sends a response back

Please search for available nodes and validate the configuration.
```

### Data Processing Workflow
```
Help me build an n8n workflow to:
1. Read data from a Google Sheets document
2. Transform the data (filter, format, calculate)
3. Send results to Slack and save to database

Show me the available nodes and validate each step.
```

### API Integration Workflow
```
Create an n8n workflow that:
1. Monitors a REST API for new data every 5 minutes
2. Processes the data with custom JavaScript
3. Conditionally routes to different endpoints
4. Handles errors gracefully

Use the n8n-mcp tools to find the right nodes and validate the setup.
```

## Advanced Workflow Prompts

### E-commerce Order Processing
```
Design a comprehensive n8n workflow for e-commerce order processing:

1. **Trigger**: New order webhook from Shopify/WooCommerce
2. **Validation**: Check inventory levels and customer data
3. **Payment**: Process payment through Stripe
4. **Fulfillment**: 
   - Send order to warehouse system
   - Generate shipping labels
   - Update inventory
5. **Communication**:
   - Send confirmation email to customer
   - Notify team via Slack
   - Update CRM system
6. **Analytics**: Log order data to analytics platform

Please:
- Search for all required nodes
- Validate each node configuration
- Create the complete workflow structure
- Include error handling branches
```

### Customer Support Automation
```
Build an intelligent customer support workflow:

1. **Intake**: Receive tickets from multiple channels (email, chat, form)
2. **Classification**: Use AI to categorize and prioritize tickets
3. **Routing**: Assign to appropriate team members
4. **Auto-response**: Send acknowledgment and estimated response time
5. **Escalation**: Automatically escalate urgent/VIP tickets
6. **Follow-up**: Schedule follow-up reminders
7. **Analytics**: Track response times and satisfaction

Requirements:
- Use n8n-mcp to find AI/ML nodes
- Implement conditional logic for routing
- Set up proper error handling
- Include testing scenarios
```

### Data Pipeline Automation
```
Create a robust data pipeline workflow:

1. **Sources**: Multiple data sources (APIs, databases, files)
2. **Extraction**: Scheduled and event-driven data collection
3. **Transformation**: 
   - Data cleaning and validation
   - Format standardization
   - Enrichment with external APIs
4. **Loading**: Send to multiple destinations
5. **Monitoring**: Health checks and alerting
6. **Backup**: Data backup and recovery procedures

Use n8n-mcp tools to:
- Find database and API nodes
- Validate transformation logic
- Set up monitoring and alerts
- Test the complete pipeline
```

## Specific Node Type Prompts

### HTTP Request Mastery
```
Help me master HTTP Request nodes in n8n:

1. Show me all HTTP-related nodes available
2. Create examples for different authentication methods
3. Demonstrate error handling for API calls
4. Show how to work with different response formats
5. Include rate limiting and retry logic

Validate each configuration and provide working examples.
```

### JavaScript Code Node Optimization
```
Optimize my JavaScript Code node usage:

1. Find all available JavaScript/code execution nodes
2. Show best practices for data manipulation
3. Demonstrate async operations and promises
4. Include error handling patterns
5. Show how to integrate with other nodes

Provide validated examples with proper syntax.
```

### Database Integration Deep Dive
```
Comprehensive database integration guide:

1. List all database connector nodes
2. Show connection configuration for major databases
3. Demonstrate CRUD operations
4. Include transaction handling
5. Show bulk operations and performance optimization

Validate all database configurations and provide test scenarios.
```

## Workflow Testing Prompts

### Validation and Testing
```
Create a comprehensive testing strategy for my n8n workflow:

1. **Unit Testing**: Test individual nodes
2. **Integration Testing**: Test node connections
3. **End-to-End Testing**: Complete workflow validation
4. **Error Testing**: Simulate failure scenarios
5. **Performance Testing**: Load and stress testing
6. **Security Testing**: Validate data handling and authentication

Use n8n-mcp validation tools for each testing phase.
```

### Monitoring and Debugging
```
Set up monitoring and debugging for n8n workflows:

1. **Logging**: Implement comprehensive logging strategy
2. **Alerts**: Set up error and performance alerts
3. **Metrics**: Track workflow performance and success rates
4. **Debugging**: Create debugging workflows and tools
5. **Health Checks**: Implement automated health monitoring

Use validation tools to ensure proper setup.
```

## Performance Optimization Prompts

### Workflow Optimization
```
Analyze and optimize my n8n workflow performance:

1. **Bottleneck Analysis**: Identify slow nodes and operations
2. **Parallel Processing**: Implement concurrent execution
3. **Resource Usage**: Optimize memory and CPU usage
4. **Caching**: Implement intelligent caching strategies
5. **Scaling**: Prepare workflow for high-volume processing

Use n8n-mcp tools to validate optimizations.
```

### Error Handling Excellence
```
Implement bulletproof error handling:

1. **Error Detection**: Identify all possible failure points
2. **Graceful Degradation**: Handle partial failures
3. **Retry Logic**: Implement smart retry mechanisms
4. **Fallback Procedures**: Create alternative execution paths
5. **User Communication**: Notify users of issues appropriately
6. **Recovery**: Implement automatic recovery procedures

Validate all error handling configurations.
```

## Integration-Specific Prompts

### Slack Integration Mastery
```
Master Slack integration with n8n:

1. Find all Slack nodes and their capabilities
2. Set up bot authentication and permissions
3. Create interactive message workflows
4. Implement slash command handlers
5. Set up automated notifications and alerts
6. Handle user interactions and responses

Validate all Slack configurations and test interactions.
```

### Google Workspace Automation
```
Comprehensive Google Workspace automation:

1. **Gmail**: Email processing and automation
2. **Google Sheets**: Data manipulation and reporting
3. **Google Drive**: File management and sharing
4. **Google Calendar**: Event scheduling and management
5. **Google Forms**: Response processing and analysis

Use n8n-mcp to find nodes and validate configurations for each service.
```

### CRM Integration Suite
```
Build comprehensive CRM integration workflows:

1. **Salesforce**: Lead and opportunity management
2. **HubSpot**: Marketing automation and analytics
3. **Pipedrive**: Sales pipeline automation
4. **Airtable**: Custom database operations
5. **Notion**: Knowledge base and project management

Validate all CRM integrations and create sync workflows.
```

## Use These Prompts With:

- `/mcp` command to see available n8n-mcp tools
- `search_nodes` to find relevant nodes
- `get_node_info` for detailed node documentation
- `validate_node_config` to check configurations
- `create_workflow` to build complete workflows
- `validate_workflow` to ensure workflow integrity