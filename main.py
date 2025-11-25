
"""
K-Blacklist: Platform Streaming Drama Korea
Main entry point - run from project root
"""
import sys
import os
src_path = os.path.join(os.path.dirname(__file__), 'src')
sys.path.insert(0, src_path)
if __name__ == "__main__":
    from src.main import main
    main()
