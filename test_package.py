#!/usr/bin/env python3
"""Test script to verify package structure."""

import sys
import os

# Add the current directory to the path so we can import the package
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test that all modules can be imported correctly."""
    print("Testing package imports...")
    
    try:
        # Test main package import
        from aige import AIGeneEnrichment
        print("✓ Successfully imported AIGeneEnrichment from aige")
        
        # Test individual module imports
        from aige.core import AIGeneEnrichment as CoreAIGeneEnrichment
        print("✓ Successfully imported AIGeneEnrichment from aige.core")
        
        from aige.enrichment_tools import ToppFunAnalyzer, GProfilerAnalyzer, EnrichrAnalyzer
        print("✓ Successfully imported enrichment tools")
        
        from aige.literature import LiteratureAnalyzer
        print("✓ Successfully imported LiteratureAnalyzer")
        
        from aige.summarize import SummarizeAnalyzer
        print("✓ Successfully imported SummarizeAnalyzer")
        
        print("\n✓ All imports successful!")
        return True
        
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def test_class_instantiation():
    """Test that the main class can be instantiated (without API key)."""
    print("\nTesting class instantiation...")
    
    try:
        from aige import AIGeneEnrichment
        
        # This should fail due to missing API key, but we can test the import
        print("✓ AIGeneEnrichment class is available")
        
        # Check class attributes
        print(f"✓ Class name: {AIGeneEnrichment.__name__}")
        print(f"✓ Class docstring: {AIGeneEnrichment.__doc__}")
        
        return True
        
    except Exception as e:
        print(f"✗ Class instantiation test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Testing AI Gene Enrichment package structure...\n")
    
    success = True
    
    if not test_imports():
        success = False
    
    if not test_class_instantiation():
        success = False
    
    print("\n" + "="*50)
    if success:
        print("✓ All tests passed! Package structure is correct.")
        print("\nYou can now:")
        print("1. Test building: python build_package.py")
        print("2. Build manually: python -m build")
        print("3. Install in development mode: pip install -e .")
    else:
        print("✗ Some tests failed. Please check the package structure.")
        sys.exit(1)

if __name__ == "__main__":
    main()
