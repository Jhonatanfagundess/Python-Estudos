from pathlib import Path

root_dir = Path('dados')
files_patch = root_dir.iterdir()
#print(list(files_patch))
for path in files_patch:
   new_filename = f'python-{path.stem}{path.suffix}'
print(new_filename)
    