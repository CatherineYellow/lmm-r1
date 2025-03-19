import subprocess
import os

def login_huggingface(token):
    print("Logging into Hugging Face...")
    command = ["huggingface-cli", "login", "--token", token]
    subprocess.run(command, check=True)
    print("Login successful.")

def download_deepscaler_dataset():
    dataset_name = "VLM-Reasoner/deepscaler"
    save_path = os.path.join(os.getcwd(), dataset_name.replace("/", "_"))
    
    print(f"Downloading dataset: {dataset_name}")
    command = ["huggingface-cli", "download", dataset_name, "--local-dir", save_path]
    subprocess.run(command, check=True)
    print(f"Dataset saved to: {save_path}")
    
if __name__ == "__main__":
    HF_TOKEN = "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"
    login_huggingface(HF_TOKEN)
    download_deepscaler_dataset()