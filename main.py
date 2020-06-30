#!/bin/python3

from flask import Flask, render_template
import flask
import subprocess
import os
import glob
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('layout.html')

@app.route('/certificate-upload', methods=['POST'])
def crtupload():
    if 'certificate' not in flask.request.files:
        return render_template('layout.html', message="ファイル未指定です")
    # ファイルの保存
    fs = flask.request.files['certificate']
    fs.save('./upload/certificate.crt')
    return render_template('layout.html', message="＊証明書のアップロードが完了しました")

@app.route('/privatekey-upload', methods=['POST'])
def keyupload():
    if 'privatekey' not in flask.request.files:
        return render_template('layout.html', message="ファイル未指定です")
    # ファイルの保存
    fs = flask.request.files['privatekey']
    fs.save('./upload/privatekey.key')
    return render_template('layout.html', message="＊秘密鍵のアップロードが完了しました")

@app.route('/ca-upload', methods=['POST'])
def caupload():
    if 'intermediate' not in flask.request.files:
        return render_template('layout.html', message="ファイル未指定です")
    # ファイルの保存
    fs = flask.request.files['intermediate']
    fs.save('./upload/intermediate.ca')
    return render_template('layout.html', message="＊中間証明書のアップロードが完了しました")

@app.route('/exec-script', methods=['POST'])
def exec():
	res = subprocess.run('./app/cert_check.sh ./upload/certificate.crt ./upload/privatekey.key ./upload/intermediate.ca', shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

	# 一時ファイルを削除
	for tmpfile in glob.glob('./tmp/*'):
		os.remove(tmpfile)
	for crtfile in glob.glob('./upload/*'):
		os.remove(crtfile)

	return res.stdout.decode("utf8")
	

if __name__ == "__main__":
	app.run(host='0.0.0.0')
	
