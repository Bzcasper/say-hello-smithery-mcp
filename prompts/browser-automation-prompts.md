# Browser Automation Prompts

## Quick Browser Task Prompts

### Basic Web Navigation
```
Use the browser-use MCP tool to:
1. Go to example.com
2. Find and extract the main title
3. Take a screenshot of the page
4. Return the page title and any important information

Use run_browser_agent tool for this task.
```

### Form Filling and Submission
```
Automate form filling on a website:
1. Navigate to the target form page
2. Fill in all required fields with provided data
3. Handle any validation errors
4. Submit the form
5. Capture confirmation or error messages

Use browser automation with vision capabilities enabled.
```

### Web Scraping and Data Extraction
```
Extract specific data from a website:
1. Navigate to the target page
2. Locate and extract specific elements (prices, descriptions, links)
3. Handle pagination if needed
4. Compile extracted data into structured format
5. Save results for further processing

Use run_browser_agent with detailed extraction instructions.
```

## E-Commerce Automation Prompts

### Product Research and Comparison
```
Research and compare products across multiple e-commerce sites:

**Task**: "Research and compare [PRODUCT] across Amazon, eBay, and other major retailers"

**Detailed Instructions**:
1. Search for the specific product on each platform
2. Extract product details (price, ratings, shipping, availability)
3. Compare features and specifications
4. Identify best deals and value propositions
5. Compile comparison report with screenshots

Use run_deep_research for comprehensive product analysis.
```

### Automated Shopping Cart Management
```
Automate shopping cart operations:
1. Search for specific products
2. Add items to cart with specified quantities
3. Apply discount codes or coupons
4. Calculate total costs including shipping
5. Proceed through checkout (stop before payment)
6. Save cart state and pricing information

Use browser automation with careful navigation through checkout process.
```

### Price Monitoring and Alerts
```
Set up automated price monitoring:
1. Navigate to product pages on multiple sites
2. Extract current pricing information
3. Compare with historical data
4. Identify price drops or deals
5. Generate price comparison reports
6. Monitor stock availability

Integrate with n8n workflows for automated monitoring and notifications.
```

## Social Media and Communication Automation

### Social Media Management
```
Automate social media tasks:
1. Log into social media platforms
2. Post content with images and hashtags
3. Respond to comments and messages
4. Monitor mentions and engagement
5. Extract analytics and performance data
6. Schedule content posting

Use browser automation for platforms without robust APIs.
```

### Email and Communication
```
Automate email and communication tasks:
1. Access web-based email clients
2. Compose and send emails with attachments
3. Organize emails into folders
4. Extract important information from emails
5. Set up automated responses
6. Monitor email analytics

Use run_browser_agent for web email automation.
```

### Content Creation and Publishing
```
Automate content publishing workflows:
1. Create and format content in web editors
2. Upload images and media files
3. Set publication settings and metadata
4. Schedule content publication
5. Monitor content performance
6. Cross-post to multiple platforms

Integrate browser automation with content management systems.
```

## Research and Data Collection Prompts

### Market Research Automation
```
Conduct comprehensive market research:

**Research Task**: "Analyze the [INDUSTRY] market landscape, key players, trends, and opportunities"

**Research Process**:
1. Identify key industry websites and resources
2. Extract company information and market data
3. Analyze competitor products and pricing
4. Research industry trends and news
5. Compile comprehensive market analysis report
6. Include charts, graphs, and data visualizations

Use run_deep_research with parallel browser instances for efficiency.
```

### Academic and Scientific Research
```
Automate academic research tasks:
1. Search academic databases and journals
2. Extract research paper abstracts and citations
3. Analyze research trends and methodologies
4. Compile bibliography and reference lists
5. Summarize key findings and conclusions
6. Generate research reports with proper citations

Use browser automation for accessing academic resources.
```

### News and Information Monitoring
```
Set up automated news monitoring:
1. Monitor news websites for specific topics
2. Extract article headlines, summaries, and links
3. Analyze sentiment and trends
4. Categorize news by topic and importance
5. Generate daily/weekly news summaries
6. Integrate with notification systems

Combine browser automation with n8n workflows for continuous monitoring.
```

## Testing and Quality Assurance Prompts

### Website Testing Automation
```
Automate website testing procedures:
1. Test website functionality across different pages
2. Verify form submissions and user interactions
3. Check responsive design on different screen sizes
4. Test loading times and performance
5. Identify broken links and missing images
6. Generate comprehensive testing reports

Use browser automation with vision capabilities for visual testing.
```

### User Experience Testing
```
Automate user experience testing:
1. Simulate user journeys and workflows
2. Test accessibility features and compliance
3. Verify mobile responsiveness
4. Check cross-browser compatibility
5. Measure page load times and performance
6. Generate UX testing reports with screenshots

Use run_browser_agent with detailed user simulation tasks.
```

### Security and Penetration Testing
```
Automate basic security testing:
1. Test form input validation and sanitization
2. Check for common security vulnerabilities
3. Verify SSL certificate and HTTPS implementation
4. Test authentication and authorization flows
5. Check for information disclosure
6. Generate security assessment reports

Use browser automation for web application security testing.
```

## Advanced Integration Workflows

### Cross-Platform Data Synchronization
```
Automate data synchronization across platforms:

**Integration Workflow**:
1. **Data Extraction** (Browser Automation):
   - Extract data from web platforms without APIs
   - Handle complex authentication flows
   - Navigate multi-step data extraction processes

2. **Data Processing** (PythonAnywhere):
   - Clean and validate extracted data
   - Transform data formats and structures
   - Apply business logic and calculations

3. **Data Distribution** (Render + n8n):
   - Deploy processed data to production systems
   - Automate data distribution workflows
   - Monitor data quality and consistency

Use all MCP tools for complete data synchronization pipeline.
```

### Automated Business Intelligence
```
Create automated BI reporting system:

**BI Automation Process**:
1. **Data Collection** (Browser + APIs):
   - Extract data from multiple web sources
   - Combine with API-based data sources
   - Handle real-time and batch data collection

2. **Data Analysis** (Python Processing):
   - Perform statistical analysis and calculations
   - Generate insights and recommendations
   - Create data visualizations and charts

3. **Report Generation and Distribution**:
   - Generate automated reports and dashboards
   - Distribute via email, web portals, or APIs
   - Schedule regular reporting cycles

Integrate browser automation with data processing and distribution systems.
```

### Customer Support Automation
```
Automate customer support processes:

**Support Automation Workflow**:
1. **Ticket Collection** (Browser Automation):
   - Monitor support platforms and social media
   - Extract customer issues and complaints
   - Categorize and prioritize support requests

2. **Response Generation** (AI Integration):
   - Generate appropriate responses based on issue type
   - Access knowledge base and documentation
   - Escalate complex issues to human agents

3. **Follow-up and Monitoring**:
   - Track resolution status and customer satisfaction
   - Generate support analytics and reports
   - Optimize support processes based on data

Use browser automation for comprehensive support platform integration.
```

## Browser Automation Best Practices

### Error Handling and Recovery
```
Implement robust error handling in browser automation:
1. Handle page load timeouts and network errors
2. Implement retry logic for failed operations
3. Capture screenshots and logs on errors
4. Graceful degradation for missing elements
5. Alternative navigation paths for blocked content
6. Comprehensive error reporting and alerting

Use browser automation with detailed error handling strategies.
```

### Performance Optimization
```
Optimize browser automation performance:
1. Use headless mode for faster execution
2. Disable unnecessary browser features (images, CSS, JavaScript)
3. Implement parallel processing for multiple tasks
4. Cache frequently accessed data and pages
5. Optimize selector strategies and wait conditions
6. Monitor and report performance metrics

Configure browser automation for optimal performance.
```

### Security and Privacy
```
Implement security best practices:
1. Use secure credential management
2. Implement proper session handling
3. Clear browser data and cookies after tasks
4. Use VPN or proxy services when needed
5. Respect robots.txt and rate limiting
6. Implement GDPR and privacy compliance

Use browser automation with security-focused configurations.
```

## Integration with Other MCP Tools

### Browser + n8n Workflows
```
Combine browser automation with n8n workflows:
1. Trigger browser tasks from n8n workflows
2. Process browser results with n8n data processing
3. Schedule regular browser automation tasks
4. Monitor browser task execution and results
5. Integrate browser data with other systems
6. Create comprehensive automation pipelines

Use browser automation as part of larger n8n workflow systems.
```

### Browser + PythonAnywhere Development
```
Integrate browser automation with Python development:
1. Test Python web applications with browser automation
2. Automate deployment testing and validation
3. Extract data for Python data analysis
4. Automate content management for Python apps
5. Monitor Python application performance
6. Generate testing reports and analytics

Use browser automation for Python application testing and monitoring.
```

### Browser + Render Production Monitoring
```
Use browser automation for production monitoring:
1. Monitor production application functionality
2. Test user workflows and critical paths
3. Monitor application performance and uptime
4. Generate automated health check reports
5. Alert on application issues and errors
6. Validate deployment success and rollbacks

Integrate browser automation with production monitoring systems.
```

## Use These Prompts With:

- `run_browser_agent` for single browser automation tasks
- `run_deep_research` for comprehensive research projects
- Vision capabilities for screenshot analysis and visual testing
- Headless mode for performance-optimized automation
- Integration with n8n, PythonAnywhere, and Render MCP tools
- Parallel processing for multi-site data collection
- Error handling and retry logic for robust automation