# __init__.py
# 作成したフォルダにparser.pyと__init__.pyを入れる
from xb_parser.parser import (
    get_fact,
    HTMLtag_remove,
    use_well_taxonomy
)

__all__ = [
    "get_fact",
    "HTMLtag_remove",
    "use_well_taxonomy"
]