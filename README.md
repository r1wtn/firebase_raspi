# Firebase on Raspberry pi

Sample code to upload and download images to/from firebase.

## Install 

```bash
python3 -m pip install -r requirements.txt
```

## Prerequisite

- a json file of `firebase-admin-credeintials` 
- name of firebase storage

## Run

You can upload a sample image, download and save it as `test.png`.

```bash
python3 main.py \
    --key-path <path_to_credential_json_file> \
    --storage-name <storage_name> \
    --image-path /mnt/usb/current.jpg \
    --csv-path /mnt/usb/current.csv
```

## Download images from firebase

```bash
python viewer.py \
    --key-path <keypath> \
    --storage-name <storage_name> \
    --save-dir "out/"
```