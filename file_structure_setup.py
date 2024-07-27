import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def create_file(path, content=""):
    with open(path, 'w') as f:
        f.write(content)
        print(f"Created file: {path}")

def main():
    # Define the directory structure
    directories = [
        "data/raw",
        "data/processed",
        "notebooks",
        "src",
        "models"
    ]

    # Define the files to be created with optional content
    files = {
        "src/__init__.py": "",
        "src/data_preprocessing.py": "# Data Preprocessing Script",
        "src/feature_extraction.py": "# Feature Extraction Script",
        "src/model_training.py": "# Model Training Script",
        "src/model_evaluation.py": "# Model Evaluation Script",
        "src/model_deployment.py": "# Model Deployment Script",
        "requirements.txt": "",
        "setup.py": (
            "from setuptools import setup, find_packages\n\n"
            "setup(\n"
            "    name='fake-news-detection',\n"
            "    version='0.1',\n"
            "    packages=find_packages(),\n"
            "    install_requires=[],\n"
            "    author='Harshal Shinoy Thachapully',\n"
            "    author_email='harshalts@gmail.com',\n"
            "    description='Put in project details here',\n"
            ")"
        ),
    }

    # Create directories
    for directory in directories:
        create_directory(directory)

    # Create files
    for path, content in files.items():
        create_file(path, content)

if __name__ == "__main__":
    main()
