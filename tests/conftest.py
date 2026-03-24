"""
Pytest configuration and fixtures for Python Problem Sets
"""
import sys
from pathlib import Path

# Add Python Solutions and TIPS directories to path for imports
repo_root = Path(__file__).parent
sys.path.insert(0, str(repo_root / "Python Solutions"))
sys.path.insert(0, str(repo_root / "TIPS 102"))
sys.path.insert(0, str(repo_root / "TIPS 103"))
