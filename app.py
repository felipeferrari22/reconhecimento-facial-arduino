from flask import Flask, render_template, Response, request, redirect, url_for
import os
import serial

while True: #Loop para a conexão com o Arduino
    try:  #Tenta se conectar, se conseguir, o loop se encerra
        arduino = serial.Serial('COM5', 9600)
        print('Arduino conectado')
        break
    except:
        pass

def abrir():
    arduino.write('a'.encode())

app = Flask(__name__)

img = os.path.join('static', 'Images')

@app.route('/')
def index():
    file = os.path.join(img, 'Desconhecido.jpg')
    return render_template('index.html', image=file)

@app.route('/abrir/', methods=['POST'])
def abrirTrava():
    file = os.path.join(img, 'Desconhecido.jpg')
    abrir()
    return render_template('index.html', image=file) 

if __name__ == '__main__':
    app.debug = True
    app.run()