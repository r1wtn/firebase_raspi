# firebase
from lib.firebase_manager import FirebaseManager
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description='post data with firebase')
parser.add_argument('--key-path', help='path to firebase admin credentials')
parser.add_argument('--storage-name', help='name of firebase storage')
parser.add_argument('--image-path', help='path to sample image')

args = parser.parse_args()
key_path = args.key_path
storage_name = args.storage_name
image_path = args.image_path

# init firebase manager
fm = FirebaseManager(key_path, storage_name)

# 1. load local image
img = Image.open(image_path)

# 2. upload image to firebase storage
fm.upload_image_file("test/test01.png", image_path)

# 3. download from firebase and save as test.png
fm.download_image("test/test01.png", "test.png")