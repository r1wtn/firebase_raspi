from lib.firebase_manager import FirebaseManager
import argparse
from datetime import date, datetime
from pytz import timezone

parser = argparse.ArgumentParser(description='post data with firebase')
parser.add_argument('--key-path', help='path to firebase admin credentials')
parser.add_argument('--storage-name', help='name of firebase storage')
parser.add_argument('--start-date')
parser.add_argument('--end-date')

args = parser.parse_args()
key_path = args.key_path
storage_name = args.storage_name
start_date = datetime.strptime(args.start_date, "%Y%m%d").replace(tzinfo=timezone("Asia/Tokyo")).astimezone(tz=timezone("UTC"))
end_date = datetime.strptime(args.end_date, "%Y%m%d").replace(tzinfo=timezone("Asia/Tokyo")).astimezone(tz=timezone("UTC"))

print(start_date, end_date)

# .replace(tzinfo=timezone("Asia/Tokyo")).astimezone(tz="UTC")
# init firebase manager
fm = FirebaseManager(key_path, storage_name)
# download all images
fm.delete_image_by_daterange(start_date, end_date)
