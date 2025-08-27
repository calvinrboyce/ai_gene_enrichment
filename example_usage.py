#!/usr/bin/env python3
"""Example usage of the AI Gene Enrichment package."""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    """Example of using the AIGeneEnrichment package."""
    
    # Get OpenAI API key from environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Please set OPENAI_API_KEY environment variable")
        print("You can create a .env file with: OPENAI_API_KEY=your_key_here")
        return
    
    try:
        # Import the package (this will work after installation)
        from aige import AIGeneEnrichment
        
        print("✓ Successfully imported AIGeneEnrichment from aige package")
        
        # Initialize the analyzer
        aige = AIGeneEnrichment(
            open_ai_api_key=api_key,
            open_ai_model="gpt-4.1-mini",
            results_dir="example_results"
        )
        
        print("✓ Successfully created AIGeneEnrichment instance")
        
        # Example gene list (cell cycle related genes)
        genes = ["ANLN", "CENPF", "NUSAP1", "TOP2A", "CCNB1", "PRC1", "TPX2", "UBE2C", "BIRC5"]
        
        print(f"✓ Ready to analyze {len(genes)} genes: {', '.join(genes)}")
        
        # Note: This is just a demonstration - actual analysis requires email and may take time
        print("\nTo run actual analysis:")
        print("results = aige.run_analysis(")
        print("    genes=genes,")
        print("    email='your.email@example.com',")
        print("    search_terms=['cancer', 'cell cycle'],")
        print("    context='Cell cycle analysis from RNA-seq data'")
        print(")")
        
        print("\n✓ Package is working correctly!")
        
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        print("Make sure you have installed the package:")
        print("pip install -e .")
    except Exception as e:
        print(f"✗ Error: {e}")

if __name__ == "__main__":
    main()
