import boto3

from botocore.client import Config
from media.s3_storage import S3MediaStorage

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def upload():
    return render_template('upload_file.html')
@app.route("/upload", methods=["POST"])
def upload_file():
    uploaded_file = request.files['uploaded_media']
    #uploaded_file.save('/home/ec2-user/media-upload/var/files/' + uploaded_file.filename)
    s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))
    media_storage = S3MediaStorage(s3=s3, bucket_name='pkozak')
    media_storage.store(key=uploaded_file.filename, media=uploaded_file)
    return redirect(url_for('upload'))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80, debug=True)
