data_parent = [
    ("alya", "bima"),
    ("alya", "satria"),
    ("bima", "david"),
    ("bima", "emma"),
    ("satria", "yunita"),
    ("satria", "grace")
]

def get_sibling(target):
    parents = [p for p, c in data_parent if c == target]

    siblings = set()

    for p in parents:
        childern = [c for parent, c in data_parent if parent == p and c != target]
        siblings.update(childern)
    
    return list(siblings)

def get_grandparent(target):
    result = []
    parents = [p for p, c in data_parent if c == target]

    for p in parents:
        grandparents = [gp for gp, c in data_parent if c == p]
        result.extend(grandparents)

    return result

print(f"Saudara Bima: {get_sibling('bima')}")
print(f"Kakek/Nenek Emma: {get_grandparent('emma')}")