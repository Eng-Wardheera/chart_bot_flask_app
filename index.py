import sys
import os

# Hubi in Python uu arko folder-ka 'app'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from __init__ import app

# Vercel wuxuu raadinayaa 'app' variable
app = app