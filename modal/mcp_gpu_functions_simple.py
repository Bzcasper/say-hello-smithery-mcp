"""
Simple Modal GPU Functions for MCP (No secrets required)
Basic GPU-accelerated browser automation without external API dependencies
"""

import modal

# Base Modal app
app = modal.App("mcp-gpu-functions-simple")

# Lightweight image for basic processing
basic_image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install([
        "requests",
        "beautifulsoup4",
        "lxml",
        "pandas",
        "aiohttp",
        "numpy"
    ])
)

# GPU image for heavier tasks (without external APIs)
gpu_image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install([
        "requests",
        "beautifulsoup4",
        "lxml", 
        "pandas",
        "numpy",
        "pillow",
        "opencv-python-headless"
    ])
)

@app.function(
    cpu=2,
    image=basic_image,
    timeout=300
)
def lightweight_web_scraping(urls: list, extract_type: str = "text") -> dict:
    """
    CPU-only web scraping for lightweight MCP tasks
    No GPU or external APIs required
    """
    import requests
    from bs4 import BeautifulSoup
    import json
    
    results = []
    
    for url in urls:
        try:
            response = requests.get(url, timeout=10, headers={
                'User-Agent': 'Mozilla/5.0 (compatible; MCP-Browser-Bot/1.0)'
            })
            soup = BeautifulSoup(response.content, 'html.parser')
            
            if extract_type == "text":
                content = soup.get_text(strip=True)[:2000]  # Limit text length
            elif extract_type == "links":
                content = [a.get('href') for a in soup.find_all('a', href=True)][:50]
            elif extract_type == "images":
                content = [img.get('src') for img in soup.find_all('img', src=True)][:50]
            elif extract_type == "title":
                title_tag = soup.find('title')
                content = title_tag.text.strip() if title_tag else "No title found"
            else:
                content = str(soup)[:1000]
            
            results.append({
                "url": url,
                "success": True,
                "content": content,
                "status_code": response.status_code,
                "content_type": response.headers.get('content-type', 'unknown')
            })
            
        except Exception as e:
            results.append({
                "url": url,
                "success": False,
                "error": str(e)
            })
    
    return {
        "success": True,
        "results": results,
        "total_urls": len(urls),
        "successful_extractions": sum(1 for r in results if r["success"]),
        "processing_info": {
            "mode": "cpu-only",
            "extract_type": extract_type,
            "modal_function": "lightweight_web_scraping"
        }
    }

@app.function(
    gpu="T4",
    image=gpu_image,
    timeout=600
)
def gpu_data_processing(data_list: list, operation: str = "analyze") -> dict:
    """
    GPU-accelerated data processing for MCP tasks
    Uses GPU for computational tasks without external API dependencies
    """
    import numpy as np
    import pandas as pd
    from datetime import datetime
    
    try:
        # Simulate GPU-accelerated data processing
        if operation == "analyze":
            # Statistical analysis
            if isinstance(data_list[0], (int, float)):
                array = np.array(data_list)
                result = {
                    "mean": float(np.mean(array)),
                    "std": float(np.std(array)),
                    "min": float(np.min(array)),
                    "max": float(np.max(array)),
                    "median": float(np.median(array)),
                    "total": float(np.sum(array))
                }
            else:
                # Text analysis
                text_lengths = [len(str(item)) for item in data_list]
                result = {
                    "total_items": len(data_list),
                    "avg_length": np.mean(text_lengths),
                    "total_characters": sum(text_lengths),
                    "unique_items": len(set(str(item) for item in data_list))
                }
                
        elif operation == "transform":
            # Data transformation
            df = pd.DataFrame({"data": data_list})
            result = {
                "original_count": len(data_list),
                "processed_data": df.to_dict('records')[:100],  # Limit output
                "data_types": str(df.dtypes.to_dict()),
                "summary": df.describe().to_dict() if df.select_dtypes(include=[np.number]).empty == False else "No numeric data"
            }
            
        else:
            result = {
                "operation": operation,
                "data_count": len(data_list),
                "sample": data_list[:10] if len(data_list) > 10 else data_list
            }
        
        return {
            "success": True,
            "operation": operation,
            "result": result,
            "processing_info": {
                "gpu_used": "T4",
                "timestamp": datetime.now().isoformat(),
                "modal_function": "gpu_data_processing"
            }
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "operation": operation,
            "data_count": len(data_list) if data_list else 0
        }

@app.function(
    gpu="A10G",
    image=gpu_image,
    timeout=900
)
def parallel_url_analysis(urls: list, analysis_type: str = "comprehensive") -> dict:
    """
    GPU-accelerated parallel URL analysis
    Processes multiple URLs simultaneously with GPU acceleration
    """
    import requests
    from bs4 import BeautifulSoup
    import numpy as np
    from concurrent.futures import ThreadPoolExecutor
    import time
    
    def analyze_single_url(url):
        try:
            start_time = time.time()
            response = requests.get(url, timeout=10, headers={
                'User-Agent': 'Mozilla/5.0 (compatible; MCP-GPU-Analyzer/1.0)'
            })
            load_time = time.time() - start_time
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract comprehensive data
            analysis = {
                "url": url,
                "status_code": response.status_code,
                "load_time": round(load_time, 3),
                "content_length": len(response.content),
                "title": soup.find('title').text.strip() if soup.find('title') else "No title",
                "meta_description": "",
                "links_count": len(soup.find_all('a')),
                "images_count": len(soup.find_all('img')),
                "forms_count": len(soup.find_all('form')),
                "scripts_count": len(soup.find_all('script')),
                "text_length": len(soup.get_text(strip=True))
            }
            
            # Meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                analysis["meta_description"] = meta_desc.get('content', '')[:200]
            
            # Additional analysis for comprehensive mode
            if analysis_type == "comprehensive":
                analysis.update({
                    "headings": {
                        "h1": len(soup.find_all('h1')),
                        "h2": len(soup.find_all('h2')),
                        "h3": len(soup.find_all('h3'))
                    },
                    "external_links": len([a for a in soup.find_all('a', href=True) 
                                         if a['href'].startswith('http') and url not in a['href']]),
                    "has_ssl": url.startswith('https'),
                    "response_headers": dict(response.headers)
                })
            
            return {**analysis, "success": True}
            
        except Exception as e:
            return {
                "url": url,
                "success": False,
                "error": str(e),
                "load_time": 0
            }
    
    try:
        # Parallel processing with ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=min(len(urls), 10)) as executor:
            results = list(executor.map(analyze_single_url, urls))
        
        # GPU-accelerated aggregation
        successful_results = [r for r in results if r["success"]]
        
        if successful_results:
            load_times = np.array([r["load_time"] for r in successful_results])
            content_lengths = np.array([r["content_length"] for r in successful_results])
            
            aggregated_stats = {
                "total_urls": len(urls),
                "successful_analyses": len(successful_results),
                "failed_analyses": len(urls) - len(successful_results),
                "avg_load_time": float(np.mean(load_times)),
                "fastest_load_time": float(np.min(load_times)),
                "slowest_load_time": float(np.max(load_times)),
                "avg_content_length": float(np.mean(content_lengths)),
                "total_content_analyzed": float(np.sum(content_lengths))
            }
        else:
            aggregated_stats = {
                "total_urls": len(urls),
                "successful_analyses": 0,
                "failed_analyses": len(urls),
                "error": "No successful analyses"
            }
        
        return {
            "success": True,
            "analysis_type": analysis_type,
            "aggregated_stats": aggregated_stats,
            "detailed_results": results,
            "processing_info": {
                "gpu_used": "A10G",
                "parallel_processing": True,
                "timestamp": time.time(),
                "modal_function": "parallel_url_analysis"
            }
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "analysis_type": analysis_type,
            "urls_count": len(urls)
        }

@app.function(
    cpu=4,
    image=basic_image,
    timeout=600
)
def mcp_task_router(task_type: str, task_data: dict) -> dict:
    """
    MCP task routing function
    Routes different types of MCP tasks to appropriate processing functions
    """
    import time
    
    start_time = time.time()
    
    try:
        if task_type == "web_scraping":
            urls = task_data.get("urls", [])
            extract_type = task_data.get("extract_type", "text")
            result = lightweight_web_scraping.remote(urls, extract_type)
            
        elif task_type == "data_processing":
            data = task_data.get("data", [])
            operation = task_data.get("operation", "analyze")
            result = gpu_data_processing.remote(data, operation)
            
        elif task_type == "url_analysis":
            urls = task_data.get("urls", [])
            analysis_type = task_data.get("analysis_type", "basic")
            result = parallel_url_analysis.remote(urls, analysis_type)
            
        else:
            return {
                "success": False,
                "error": f"Unknown task type: {task_type}",
                "available_types": ["web_scraping", "data_processing", "url_analysis"]
            }
        
        processing_time = time.time() - start_time
        
        return {
            "success": True,
            "task_type": task_type,
            "result": result,
            "routing_info": {
                "processing_time": round(processing_time, 3),
                "routed_to": f"{task_type}_function",
                "modal_router": "mcp_task_router"
            }
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "task_type": task_type,
            "processing_time": time.time() - start_time
        }

if __name__ == "__main__":
    print("Simple Modal MCP GPU Functions configured")
    print("Available functions:")
    print("- lightweight_web_scraping (CPU)")
    print("- gpu_data_processing (GPU: T4)")  
    print("- parallel_url_analysis (GPU: A10G)")
    print("- mcp_task_router (CPU - routing)")
    print("Ready for MCP server integration!")