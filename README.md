# Sistema de Segurança Agrícola baseado em Reconhecimento Facial
**Este Repositório é dedicado à parte prática do projeto, desenvolvido como Trabalho de Graduação da Fatec Pompéia.**

![fatec-pompeia](https://github.com/felipeferrari22/reconhecimento-facial-arduino/assets/78982963/1fb63e74-6dab-411c-98c0-785c219468d0)
## Desenvolvido utilizando
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="35px">  •  **Python** &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="35px">  •  **Flask** &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="35px">  •  **HTML5** &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="35px"> • **CSS3** &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg" height="35px"> • **Arduino** &nbsp;&nbsp;&nbsp;&nbsp;

<br>

## Inicializar o projeto
O circuito do Arduino deve ser montado da seguinte forma: 

![arduino](https://github.com/felipeferrari22/reconhecimento-facial-arduino/assets/78982963/46a2799f-668b-452a-9cda-9f0c178729a8)    ![arduino2](https://github.com/felipeferrari22/reconhecimento-facial-arduino/assets/78982963/7f73a047-eaa8-4821-9cc6-cc02a8a90bb0)

O código no arquivo 'abrir_trava.ino' deve então ser carregado no Arduino por meio do cabo USB.

<strong>Inicialização do Flask</strong>

`flask --app flaskr run --debug`

<strong>Inicialização do Algoritmo de Reconhecimento Facial</strong>

Requisitos:
- `pip install opencv-python`
- `pip install opencv-contrib-python --upgrade` ou `pip install opencv-contrib-python --user.`
- `pip install pySerial`
- `pip install threading`

## Passos
`cmd: python face_taker.py`
1) Tire fotos usando o script `face_taker.py`. Ele salvará 40 imagens do seu rosto, criando a pasta `images` (se ela não existir) após você inserir a sua ID. (DEVE ser int e crescente (1, 2, 3...))

`cmd: python face_train.py`

2) O script `face_train.py` irá treinar um modelo para reconhecer todas as faces das 40 imagens tiradas pelo `face_taker.py`, e salvar o output do treinamento no arquivo `training.yml`.

3) O script `face_recognizer.py` é utilizado para salvar o nome de cada pessoa cujas fotos foram tiradas pelo `face_taker.py`. O programa reconhecerá o rosto de acordo com a ID informada. Se João informou a ID 1, seu nome deve aparecer da seguinte forma `names = [None, 'João'] # mantenha o None e adicione o nome à lista`

`cmd: python start.py`

4) O script `start.py` é o principal do projeto. Ao executá-lo, o threading se iniciará, o que executará ambos o `face_recognizer.py` e o `app.py`, e a conexão com o Arduino se iniciará. A URL do Site será informada no Console, e a janela de Reconhecimento Facial se abrirá.

## Referências Principais
- [Real-Time Face-Recognition, de medsriha](https://github.com/medsriha/real-time-face-recognition/)
- [Trava Elétrica Solenóide, do Portal Vida de Silício](https://portal.vidadesilicio.com.br/trava-eletrica-solenoide/) 
