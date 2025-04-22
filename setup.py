from setuptools import setup, find_packages
from pathlib import Path

def get_requirements(filename='requirements.txt'):
    """Read requirements from a file and return as a list, ignoring editable installs like '-e .'."""
    try:
        req_path = Path(__file__).parent / filename
        with open(req_path, 'r') as f:
            requirements = f.read().splitlines()
        return [r for r in requirements if r and not r.startswith('#') and r.strip() != '-e .']
    except FileNotFoundError:
        print(f"[Warning] {filename} not found. Proceeding without additional install requirements.")
        return []
    except Exception as e:
        print(f"[Error] Failed to parse {filename}: {e}")
        return []

setup(
    name='mlops_pipeline_project',
    version='0.1.0',
    author='Sarthak Gaurav',
    description='An MLOps pipeline for model training, evaluation, and deployment',
    long_description=open('README.md').read() if Path('README.md').exists() else '',
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements()
)

print(get_requirements())
