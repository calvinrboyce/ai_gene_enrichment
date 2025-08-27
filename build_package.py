#!/usr/bin/env python3
"""Build script for testing package creation."""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"Running: {description}")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        if result.stdout:
            print(f"Output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed")
        print(f"Error: {e}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return False

def main():
    """Main build process."""
    print("Building AI Gene Enrichment package...")
    
    # Clean previous builds
    print("\nCleaning previous builds...")
    for path in ['build/', 'dist/', '*.egg-info/']:
        subprocess.run(['rm', '-rf', path], capture_output=True)
    
    # Check if we're in a virtual environment
    if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("Warning: Not running in a virtual environment")
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            print("Aborting build")
            return
    
    # Install build dependencies
    print("\nInstalling build dependencies...")
    if not run_command([sys.executable, '-m', 'pip', 'install', '--upgrade', 'build', 'wheel'], 
                      "Installing build tools"):
        return
    
    # Build the package
    print("\nBuilding package...")
    if not run_command([sys.executable, '-m', 'build'], "Building package"):
        return
    
    # Check the built package
    print("\nChecking built package...")
    dist_dir = Path('dist')
    if dist_dir.exists():
        files = list(dist_dir.glob('*'))
        print(f"Built files: {[f.name for f in files]}")
        
        # Try installing in a test environment
        print("\nTesting package installation...")
        test_install_dir = Path('test_install')
        test_install_dir.mkdir(exist_ok=True)
        
        # Find the wheel file
        wheel_files = [f for f in files if f.suffix == '.whl']
        if wheel_files:
            wheel_file = wheel_files[0]
            print(f"Installing wheel: {wheel_file.name}")
            
            # Create a test virtual environment
            if run_command([sys.executable, '-m', 'venv', 'test_venv'], "Creating test virtual environment"):
                # Activate and install
                if os.name == 'nt':  # Windows
                    activate_script = 'test_venv\\Scripts\\activate'
                    pip_cmd = ['test_venv\\Scripts\\python.exe', '-m', 'pip']
                else:  # Unix/Linux/macOS
                    activate_script = 'test_venv/bin/activate'
                    pip_cmd = ['test_venv/bin/pip']
                
                if run_command(pip_cmd + ['install', str(wheel_file)], "Installing package in test environment"):
                    print("✓ Package installation test successful!")
                    
                    # Test import
                    if run_command(pip_cmd + ['install', 'ipython'], "Installing IPython for testing"):
                        test_script = f"""
import sys
sys.path.insert(0, '{test_install_dir}')
try:
    from aige import AIGeneEnrichment
    print("✓ Import successful!")
    print(f"✓ AIGeneEnrichment class found: {{AIGeneEnrichment}}")
except ImportError as e:
    print(f"✗ Import failed: {{e}}")
    sys.exit(1)
"""
                        test_file = test_install_dir / 'test_import.py'
                        test_file.write_text(test_script)
                        
                        if run_command(['test_venv/bin/python', str(test_file)], "Testing package import"):
                            print("✓ All tests passed!")
                        else:
                            print("✗ Import test failed")
                else:
                    print("✗ Package installation failed")
                
                # Clean up test environment
                subprocess.run(['rm', '-rf', 'test_venv'], capture_output=True)
        else:
            print("✗ No wheel file found")
    else:
        print("✗ Build directory not found")
    
    print("\nBuild process completed!")
    print("\nTo publish to PyPI:")
    print("1. Update version in pyproject.toml and setup.cfg")
    print("2. Run: python -m build")
    print("3. Run: python -m twine upload dist/*")

if __name__ == "__main__":
    main()
