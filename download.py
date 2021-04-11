from lib.firebase_manager import FirebaseManager
import argparse

parser = argparse.ArgumentParser(description='post data with firebase')
parser.add_argument('--key-path', help='path to firebase admin credentials')
parser.add_argument('--storage-name', help='name of firebase storage')
parser.add_argument('--save-dir', help='path to image download directory')

args = parser.parse_args()
key_path = args.key_path
storage_name = args.storage_name
save_dir = args.save_dir

# init firebase manager
fm = FirebaseManager(key_path, storage_name)
# download all images
fm.download_all_images(save_dir)