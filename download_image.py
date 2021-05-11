from lib.firebase_manager import FirebaseManager
import argparse
from datetime import date, datetime
from pytz import timezone

parser = argparse.ArgumentParser(description='post data with firebase')
parser.add_argument('--key-path', help='path to firebase admin credentials')
parser.add_argument('--storage-name', help='name of firebase storage')
parser.add_argument('--save-dir', help='path to image download directory')
parser.add_argument('--start-date')
parser.add_argument('--end-date')

args = parser.parse_args()
key_path = args.key_path
storage_name = args.storage_name
save_dir = args.save_dir
start_date = datetime.strptime(args.start_date, "%Y%m%d").replace(tzinfo=timezone("Asia/Tokyo")).astimezone(tz=timezone("UTC"))
end_date = datetime.strptime(args.end_date, "%Y%m%d").replace(tzinfo=timezone("Asia/Tokyo")).astimezone(tz=timezone("UTC"))


# init firebase manager
fm = FirebaseManager(key_path, storage_name)

if start_date is None and end_date is None:
    # download all images
    fm.download_all_images(save_dir)
else:
    fm.download_images_by_daterange(save_dir, start_date, end_date)