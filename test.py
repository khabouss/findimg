import webbrowser
import sys
import firebase_admin
import datetime
from firebase_admin import credentials, firestore, storage

credentiels_obj = firebase_admin.credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(credentiels_obj, {
    'storageBucket': 'findimg-6f79c.appspot.com'
})
database = firestore.client()
bucket = storage.bucket()
blob = bucket.blob('mood.jpg')
outfile = sys.argv[1]
blob.upload_from_filename(outfile)
blob.make_public()
imgurl = blob.public_url
googleurl = 'https://www.google.com/searchbyimage?&image_url='
webbrowser.open(googleurl+imgurl)