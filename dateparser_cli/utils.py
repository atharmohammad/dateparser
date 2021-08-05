import sys
import os
from pathlib import Path

DEFAULT_UNIX_CACHE_DIR = os.environ.get("DEFAULT_CACHE_DIR", '~/.cache')
DEFAULT_WIXDOWS_CACHE_DIR = os.environ.get("DEFAULT_CACHE_DIR", os.path.join(str(Path.home()), "AppData", "Roaming"))
DEFAULT_DIR_NAME = os.environ.get("DEFAULT_DIR_NAME", 'dateparser_models')


if sys.platform.startswith('win'):
    # For Windows:
    _cache_dir = DEFAULT_WIXDOWS_CACHE_DIR
else:
    # UNIX & OS X:
    _cache_dir = DEFAULT_UNIX_CACHE_DIR

dateparser_model_home = os.path.expanduser(
    os.path.join(_cache_dir, DEFAULT_DIR_NAME)
)


def create_data_model_home():
    if not os.path.isdir(dateparser_model_home):
        os.mkdir(dateparser_model_home)


def clear_cache(*args):
    for path in Path(dateparser_model_home).rglob('*.*'):
        os.remove(path)
