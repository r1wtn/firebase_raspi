import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from firebase_admin import storage
import io
from typing import Optional


class FirebaseManager(object):
    def __init__(self, key_path, storage_name):
        cred = credentials.Certificate(key_path)
        self.app = firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.bucket = storage.bucket(storage_name)
        self.auth = firebase_admin.auth.Client(self.app)

    def find_one(self, collection_path, doc_id):
        return self.db.collection(collection_path).document(doc_id)

    def find(self, collection_path, query=None):
        return self.db.collection(collection_path).stream()

    def insert_one(self, collection_path, data, doc_id=None):
        doc_ref = self.db.collection(collection_path).document(doc_id)
        doc_ref.set(data)
        return True

    def insert_many(self, collection_path, docs):
        collection_ref = self.db.collection(collection_path)
        for doc in docs:
            collection_ref.document().set(doc)
        return True

    def update_one(self, collection_path, doc_id, data):
        doc_ref = self.db.collection(collection_path).document(doc_id)
        doc_ref.update(data)
        return True

    def delete_collection(self, collection_path):
        docs = self.db.collection(collection_path).get()
        for doc in docs:
            doc.reference.delete()
        return True

    def get_user_info_from_token(self, id_token):
        decoded_token = self.auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        email = decoded_token["email"]
        email_verified = decoded_token["email_verified"]
        return uid, email, email_verified

    # Bucket method
    def upload_image_file(self, image_id, image_path):
        blob = self.bucket.blob(image_id)
        blob.upload_from_filename(image_path)
        return True

    def upload_onmemory_image(self, image_id, image):
        blob = self.bucket.blob(image_id)
        buf = io.BytesIO()
        image.save(buf, "png")
        buf.seek(0)
        blob.upload_from_file(buf)
        return True

    def download_image(self, image_name, save_name):
        blob = self.bucket.blob(image_name)
        blob.download_to_filename(save_name)
        return True

    def delete_image(self, image_id):
        blob = self.bucket.blob(image_id)
        blob.delete()
        return True

    def clear_bucket(self):
        blobs = self.bucket.list_blobs()
        for blob in blobs:
            blob.delete()
        return True

    def create_custom_token(self, uid):
        return self.auth.create_custom_token(uid)

    def create_user(self, email, password, email_verified):
        """authでユーザ作成. 利用しない.
        """
        return self.auth.create_user(
            email=email,
            email_verified=email_verified,
            password=password,
            disabled=False
        )