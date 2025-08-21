"""
Modal Deployment Script for MCP GPU Functions
Deploys GPU-accelerated browser automation to Modal Labs
"""

import modal
import os
import sys

def deploy_mcp_functions():
    """Deploy MCP GPU functions to Modal"""
    
    print("🚀 Deploying MCP GPU functions to Modal Labs...")
    
    # Import the app
    try:
        from mcp_gpu_functions import app
        print("✅ MCP GPU functions app loaded successfully")
    except ImportError as e:
        print(f"❌ Failed to import MCP GPU functions: {e}")
        return False
    
    try:
        # Deploy the app
        print("📡 Deploying to Modal...")
        app.deploy("mcp-gpu-functions")
        print("✅ Successfully deployed MCP GPU functions!")
        
        print("\n📋 Deployed Functions:")
        print("  🖥️  heavy_browser_automation - GPU T4")
        print("  🔍 deep_web_research - GPU A10G") 
        print("  📄 lightweight_web_scraping - CPU only")
        print("  📝 ai_powered_form_filling - GPU T4")
        print("  📊 multi_site_monitoring - GPU A10G")
        
        print("\n💡 Usage:")
        print("  modal run modal/mcp_gpu_functions.py::heavy_browser_automation --task 'Navigate to example.com'")
        print("  modal run modal/mcp_gpu_functions.py::deep_web_research --research-topic 'AI trends 2024'")
        
        return True
        
    except Exception as e:
        print(f"❌ Deployment failed: {e}")
        return False

def check_modal_setup():
    """Check if Modal is properly configured"""
    
    print("🔍 Checking Modal setup...")
    
    # Check if modal is installed
    try:
        import modal
        print("✅ Modal package installed")
    except ImportError:
        print("❌ Modal package not found. Install with: pip install modal")
        return False
    
    # Check if authenticated
    try:
        # This will fail if not authenticated
        modal.App("test-auth")
        print("✅ Modal authentication configured")
    except Exception as e:
        print("❌ Modal authentication required. Run: modal setup")
        print(f"   Error: {e}")
        return False
    
    # Check for required secrets
    print("⚠️  Required Modal secrets:")
    print("  - google-api-key (for AI browser automation)")
    print("  Create with: modal secret create google-api-key GOOGLE_API_KEY=your_key_here")
    
    return True

def main():
    """Main deployment function"""
    
    print("🔧 Modal MCP GPU Functions Deployment")
    print("=" * 50)
    
    # Check Modal setup
    if not check_modal_setup():
        print("\n❌ Modal setup incomplete. Please fix issues above.")
        sys.exit(1)
    
    # Deploy functions
    if deploy_mcp_functions():
        print("\n🎉 Deployment successful!")
        print("\n🔗 Integration with MCP:")
        print("  1. Functions are now available via Modal")
        print("  2. Call from browser-use MCP server when GPU needed")
        print("  3. Fallback to local processing for lightweight tasks")
        print("\n📚 Next steps:")
        print("  - Test functions: modal run modal/mcp_gpu_functions.py")
        print("  - Monitor usage: modal logs mcp-gpu-functions")
        print("  - Update config: Edit modal/mcp_gpu_functions.py")
    else:
        print("\n❌ Deployment failed. Check errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()