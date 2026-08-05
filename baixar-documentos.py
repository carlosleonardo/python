import requests
from pathlib import Path
import json

def download_from_onedrive(share_link, download_path="./downloads"):
	"""
	Download documents from OneDrive using a shared link.
	
	Args:
		share_link (str): The OneDrive shared link
		download_path (str): Local directory to save files
	"""
	Path(download_path).mkdir(parents=True, exist_ok=True)
	
	# Convert sharing link to direct download link
	if "onedrive.live.com" in share_link:
		# Extract file ID and convert to direct download link
		file_id = share_link.split("id=")[-1].split("&")[0]
		direct_url = f"https://onedrive.live.com/download?resid={file_id}"
	else:
		direct_url = share_link
	
	try:
		response = requests.get(direct_url, stream=True)
		response.raise_for_status()
		
		# Get filename from Content-Disposition header or URL
		filename = "downloaded_file"
		if "Content-Disposition" in response.headers:
			filename = response.headers["Content-Disposition"].split("filename=")[-1].strip('"')
		
		file_path = Path(download_path) / filename
		
		with open(file_path, "wb") as f:
			for chunk in response.iter_content(chunk_size=8192):
				f.write(chunk)
		
		print(f"✓ Downloaded: {file_path}")
		return file_path
		
	except Exception as e:
		print(f"✗ Error downloading file: {e}")
		return None	

if __name__ == "__main__":
	# Example usage
	onedrive_link = input("Entre o link compartilhado: ")
	download_from_onedrive(onedrive_link)
	