
def read(filepath):
    with open(filepath) as f:
        return f.read().splitlines()
