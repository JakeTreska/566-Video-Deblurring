
from huggingface_hub import hf_hub_download
from huggingface_hub import notebook_login 

repo_id = "snah/REDS"      
repo_type = "dataset"    
files_to_download = [
        "train_blur.zip",
        "train_sharp.zip",
        "val_blur.zip",
        "val_sharp.zip",
        "test_blur.zip"
]
downloaded_files = []
for file_path in files_to_download:
        local_path = hf_hub_download(
                repo_id=repo_id,
                filename=file_path,
                repo_type=repo_type,
                # token=True, 											# Use if you logged in via notebook_login() or HF_TOKEN secret
                local_dir='.',          						# Optional: Download directly to current dir (./content/) instead of cache
                local_dir_use_symlinks=False 				# Recommended with local_dir='.' to avoid symlinks
        )
        downloaded_files.append(local_path)