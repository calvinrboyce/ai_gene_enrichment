# Publishing Guide for AI Gene Enrichment

This guide explains how to publish the `ai-gene-enrichment` package to PyPI.

## Current Status

✅ Package structure refactored for PyPI
✅ All necessary configuration files created
✅ Package builds successfully
✅ Package structure verified
✅ Import structure: `from aige import AIGeneEnrichment`

## Package Structure

```
ai_gene_enrichment/
├── aige/                          # Main package directory
│   ├── __init__.py               # Package initialization and main class import
│   ├── core.py                   # AIGeneEnrichment class
│   ├── cli.py                    # Command-line interface
│   ├── literature.py             # Literature analysis module
│   ├── summarize.py              # AI summarization module
│   └── enrichment_tools/         # Enrichment analysis tools
│       ├── __init__.py
│       ├── enrichr.py
│       ├── gprofiler.py
│       └── toppfun.py
├── pyproject.toml                # Modern Python packaging configuration
├── setup.cfg                     # Legacy setup configuration
├── MANIFEST.in                   # Package file inclusion rules
├── LICENSE                       # MIT license
├── README.md                     # Package documentation
├── requirements.txt              # Dependencies
├── build_package.py              # Build testing script
├── test_package.py               # Package structure testing
└── example_usage.py              # Usage examples
```

## Files Created for PyPI

### 1. pyproject.toml
- Modern Python packaging configuration
- Package metadata, dependencies, and build settings
- Development tools configuration (black, mypy, etc.)

### 2. setup.cfg
- Legacy setup configuration for compatibility
- Entry points for CLI command
- Package discovery settings

### 3. MANIFEST.in
- Specifies which files to include in the package
- Excludes development and temporary files

### 4. LICENSE
- MIT license for the package

## Testing the Package

### 1. Test Package Structure
```bash
python test_package.py
```

### 2. Install in Development Mode
```bash
pip install -e .
```



### 3. Test Import
```python
from aige import AIGeneEnrichment
```

### 4. Build Package
```bash
python -m build
```

## Publishing to PyPI

### Prerequisites

1. **PyPI Account**: Create an account at [pypi.org](https://pypi.org)
2. **TestPyPI Account**: Create an account at [test.pypi.org](https://test.pypi.org) for testing
3. **API Token**: Generate an API token in your PyPI account settings

### Step 1: Install Publishing Tools

```bash
pip install twine
```

### Step 2: Test on TestPyPI (Recommended)

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ ai-gene-enrichment
```

### Step 3: Publish to PyPI

```bash
# Upload to PyPI
twine upload dist/*
```

### Step 4: Verify Installation

```bash
# Install from PyPI
pip install ai-gene-enrichment

# Test import
python -c "from aige import AIGeneEnrichment; print('Success!')"
```

## Version Management

To update the package version:

1. Update version in `pyproject.toml`:
   ```toml
   version = "0.1.1"
   ```

2. Update version in `setup.cfg`:
   ```ini
   version = 0.1.1
   ```

3. Update version in `aige/__init__.py`:
   ```python
   __version__ = "0.1.1"
   ```

4. Rebuild and publish:
   ```bash
   python -m build
   twine upload dist/*
   ```

## Package Features

- **Main Class**: `AIGeneEnrichment` - accessible via `from aige import AIGeneEnrichment`
- **Pure Python Package**: No CLI dependencies, designed for programmatic use only
- **Dependencies**: All required packages specified in `pyproject.toml`
- **Documentation**: Comprehensive README with examples
- **License**: CC-BY-NC 4.0 license for non-commercial use

## Troubleshooting

### Common Issues

1. **Build Warnings**: The deprecation warnings about license classifiers are harmless but can be fixed by updating to newer setuptools versions.

2. **Import Errors**: Ensure the package is properly installed with `pip install -e .` for development.



### Support

For issues with the package structure or publishing process, check:
- Package build logs
- Import test results

- Dependencies installation

## Next Steps

1. ✅ **Package Structure**: Complete
2. ✅ **Configuration Files**: Complete
3. ✅ **Testing**: Complete
4. 🔄 **Publishing**: Ready for PyPI upload
5. 📚 **Documentation**: Update with PyPI installation instructions
6. 🚀 **Distribution**: Share package with the community

The package is now ready for PyPI publication! Users will be able to install it with `pip install ai-gene-enrichment` and import it with `from aige import AIGeneEnrichment`.
