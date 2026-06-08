"""Read and write files."""

from pathlib import Path


current_folder = Path(__file__).parent
file_path = current_folder / "sample_note.txt"

file_path.write_text("Python file handling example\n", encoding="utf-8")

content = file_path.read_text(encoding="utf-8")
print("File content:")
print(content)

with file_path.open("a", encoding="utf-8") as file:
    file.write("Added another line\n")

print("After append:")
print(file_path.read_text(encoding="utf-8"))

