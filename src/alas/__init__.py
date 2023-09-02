from importlib import resources
try:
    import tomllib
except ImportError:
    import toml as tomllib

__version__ = "1.0.0"
__author__ = "renato"
__license__ = "GNU GPLv3"
__name__ = "alsec"

_cfg = tomllib.loads(resources.read_text("config", "config.toml"))
alasURL = _cfg["feed"]["alasUrl"]
alas2URL = _cfg["feed"]["alas2Url"]
alas2023URL = _cfg["feed"]["alas2023Url"]
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'alsec/%s +https://github.com/renatorpn/alsec' % __version__
    }