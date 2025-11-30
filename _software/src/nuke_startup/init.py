
import os
import sys

dir_path = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(dir_path)

# Add the wolfkrow_demo src directory to the sys.path
sys.path.append(parent_dir)