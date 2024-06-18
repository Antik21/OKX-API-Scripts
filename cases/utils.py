import os
import sys


def init_config_access():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
