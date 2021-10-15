from pathlib import Path
root=Path(__file__).parent.parent
def more():
    yield root/'dvd'
    yield root/'foo'
    yield root/'iso'
    yield root/'vcd'


