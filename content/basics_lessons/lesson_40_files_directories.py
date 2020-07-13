from pathlib import Path

path_obj = Path()

for file in path_obj.glob("content/**/*.py",):
    file_path = str(file.absolute())
    new_file_path = file_path.replace("-", "_")
    
    last_slash = new_file_path.rindex("/")
    newer_file_path = f"{new_file_path[:last_slash+1]}lesson_{new_file_path[last_slash+1:]}"

    print(newer_file_path)

    file.rename(newer_file_path)
