class Remap:
“””
Represents a controller input remapping.
“””

def __init__(self, source, target):
    self.source = source
    self.target = target
def __repr__(self):
    return f"Remap({self.source!r} -> {self.target!r})"