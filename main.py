# firebase
from lib.firebase_manager import FirebaseManager
from PIL import Image
import argparse
from datetime import datetime

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

# 4. generate sample GPS data
tractor_id = "abc01"
lat = 35.69362830636109
lng = 139.80611369660275
timestamp = datetime.now()
gps_data = {
    "tractor_id": tractor_id,
    "latitude": lat,
    "longitude": lng,
    "timestamp": timestamp 
}

# 5. post one gps data to firestore
fm.insert_one("gps", gps_data)