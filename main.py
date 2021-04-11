# firebase
from lib.firebase_manager import FirebaseManager
from PIL import Image
import argparse
from datetime import datetime
import csv
import os

parser = argparse.ArgumentParser(description='post data with firebase')
parser.add_argument('--key-path', help='path to firebase admin credentials')
parser.add_argument('--storage-name', help='name of firebase storage')
parser.add_argument('--image-path', help='path to sample image')
parser.add_argument('--csv-path', help='path to sample csv')


args = parser.parse_args()
key_path = args.key_path
storage_name = args.storage_name
image_path = args.image_path
csv_path = args.csv_path

# init firebase manager
fm = FirebaseManager(key_path, storage_name)

# parse current.csv and generate json
gps_json = {}
keys = ("latitude", "longitude", "sampled_at")
with open(csv_path, "r") as f:
    for row in csv.DictReader(f, keys):
        gps_json = row

# image_name is string of datetime now
sent_at = datetime.now()
image_name = sent_at.isoformat(timespec='seconds') + ".jpg"

gps_json["sent_at"] = sent_at
gps_json["tractor_id"] = os.uname()[1]
gps_json["image_name"] = image_name

# insert gps data into firestore
fm.insert_one("gps", gps_json)

# upload image to firebase storage
if image_path is not None:
    fm.upload_image_file(f"test/{image_name}", image_path)
