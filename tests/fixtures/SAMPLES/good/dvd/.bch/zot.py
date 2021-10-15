from pathlib import Path
root=Path(__file__).parent.parent
def more():
    yield root/'movies'

def ls():
    for ii in root.glop('*'):
        print(ii)

