import nbformat

path = "resnet.ipynb"

with open(path, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

if "widgets" in nb["metadata"]:
    del nb["metadata"]["widgets"]

for cell in nb["cells"]:
    if "widgets" in cell.get("metadata", {}):
        del cell["metadata"]["widgets"]

with open(path, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Fixed notebook metadata.")