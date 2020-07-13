from pathlib import Path

path_obj = Path()

for file in path_obj.glob("content/**/*.py",):
    print(file)