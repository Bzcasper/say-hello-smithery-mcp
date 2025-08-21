#!/usr/bin/env python3
"""
Test Modal MCP GPU Functions
Quick test to verify deployed functions work correctly
"""

import os
import json

# Set Modal environment variables
os.environ["MODAL_TOKEN_ID"] = "ak-sX7vqQHLCESBhgJBLWCzqr"
os.environ["MODAL_TOKEN_SECRET"] = "as-UN7iCC3G8Q39b2S1rBXWtx"

try:
    import modal
    
    # Import the deployed app (using correct API for v1.1.0)
    app = modal.lookup("mcp-gpu-functions-simple", environment="main")
    
    print("🧪 Testing Modal MCP GPU Functions")
    print("=" * 50)
    
    # Test 1: Lightweight web scraping
    print("\n1. Testing lightweight_web_scraping...")
    try:
        lightweight_web_scraping = app.get_function("lightweight_web_scraping")
        result = lightweight_web_scraping.remote(
            urls=["https://example.com"],
            extract_type="title"
        )
        print("✅ Lightweight web scraping:", "PASSED" if result["success"] else "FAILED")
        if result["success"]:
            print(f"   📄 Extracted: {result['results'][0]['content']}")
    except Exception as e:
        print(f"❌ Lightweight web scraping: FAILED - {e}")
    
    # Test 2: GPU data processing
    print("\n2. Testing gpu_data_processing...")
    try:
        gpu_data_processing = app.get_function("gpu_data_processing")
        result = gpu_data_processing.remote(
            data_list=[1, 2, 3, 4, 5, 10, 15, 20],
            operation="analyze"
        )
        print("✅ GPU data processing:", "PASSED" if result["success"] else "FAILED")
        if result["success"]:
            print(f"   📊 Analysis: Mean={result['result']['mean']:.2f}, GPU={result['processing_info']['gpu_used']}")
    except Exception as e:
        print(f"❌ GPU data processing: FAILED - {e}")
    
    # Test 3: Task router
    print("\n3. Testing mcp_task_router...")
    try:
        mcp_task_router = app.get_function("mcp_task_router")
        result = mcp_task_router.remote(
            task_type="web_scraping",
            task_data={
                "urls": ["https://httpbin.org/json"],
                "extract_type": "text"
            }
        )
        print("✅ MCP task router:", "PASSED" if result["success"] else "FAILED")
        if result["success"]:
            print(f"   🔀 Routed to: {result['routing_info']['routed_to']}")
    except Exception as e:
        print(f"❌ MCP task router: FAILED - {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Modal MCP GPU Functions Test Complete!")
    print("📋 Available for MCP server integration:")
    print("  • lightweight_web_scraping (CPU)")
    print("  • gpu_data_processing (GPU: T4)")  
    print("  • parallel_url_analysis (GPU: A10G)")
    print("  • mcp_task_router (CPU routing)")
    print("\n💡 Ready for browser-use MCP server integration!")
    
except ImportError:
    print("❌ Modal not available. Install with: pipx install modal")
except Exception as e:
    print(f"❌ Error: {e}")
    print("💡 Make sure Modal credentials are configured correctly")