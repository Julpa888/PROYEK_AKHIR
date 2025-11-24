#!/usr/bin/env python
"""
K-Blacklist: Platform Streaming Drama Korea
Main entry point - run from project root
"""

import sys
import os

# Add src directory to Python path
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_path)

# Import and run main
if __name__ == "__main__":
    from src.main import main
    main()
