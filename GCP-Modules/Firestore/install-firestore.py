import subprocess
import sys

def install_package(package_name):
    """Install a package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")

# Install google-cloud-firestore
install_package("google-cloud-firestore")
install_package("firebase-admin")

# Test Firestore Import
try:
    from google.cloud import firestore
    print("google.cloud.firestore imported successfully!")
except ImportError:
    print("google.cloud.firestore is not installed!")