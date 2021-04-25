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

args = parser.parse_args()
key_path = args.key_path
storage_name = args.storage_name

fm = FirebaseManager(key_path, storage_name)
