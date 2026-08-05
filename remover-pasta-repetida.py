import os
import shutil


def remove_folder(root_path, folder_name):
	"""Remove all occurrences of a folder in a directory hierarchy"""
	for dirpath, dirnames, filenames in os.walk(root_path):
		if folder_name in dirnames:
			folder_path = os.path.join(dirpath, folder_name)
			shutil.rmtree(folder_path)
			print(f"Removed: {folder_path}")
			dirnames.remove(folder_name)  # Prevent descending into removed folder

# Usage
root_path = input("Entre o caminho da pasta raiz: ")
folder_to_remove = input("Entre o nome da pasta a remover: ")

remove_folder(root_path, folder_to_remove)
print("Done!")
