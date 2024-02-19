# import os
# import importlib

# def _import_submodules(package_name):
#     """Imports all submodules of a package (models/*.py), assuming model classes within."""

#     package_dir = os.path.dirname(os.path.abspath(__file__))  # Models directory
#     module_names = [
#         os.path.splitext(module_file)[0]  # Get module name (exclude '.py')
#         for module_file in os.listdir(package_dir)
#         if module_file.endswith('.py') and not module_file.startswith('__')
#     ]

#     # Dynamically import each model module
#     for module_name in module_names:
#         importlib.import_module(f"{package_name}.{module_name}")

# # Import all submodules within the 'app.models' package
# _import_submodules(__name__)  
from .artist import Artist
from .base import Base
from .song import Song
from .playlist import Playlist