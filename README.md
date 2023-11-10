# Sistema de Segurança Agrícola baseado em Reconhecimento Facial
**Este Repositório é dedicado à parte prática do projeto, desenvolvido como Trabalho de Graduação da Fatec Pompéia.**

![fatec-pompeia](https://github.com/felipeferrari22/reconhecimento-facial-arduino/assets/78982963/06d287c0-9421-4a0f-a2a1-392c82fe98d8)

[Clique aqui](https://github.com/felipeferrari22/reconhecimento-facial-arduino/blob/0eb0aa6c7cc543b52f1ca6eaf6c628a8b4531593/Artigo/Sistema%20de%20Seguran%C3%A7a%20Agr%C3%ADcola%20baseado%20em%20Reconhecimento%20Facial.pdf) para ler o artigo.

## Desenvolvido utilizando
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="35px">  •  **Python** &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" height="35px">  •  **Flask** &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="35px">  •  **HTML5** &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp; <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="35px"> • **CSS3** &nbsp;&nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp;&nbsp;<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg" height="35px"> • **Arduino** &nbsp;&nbsp;&nbsp;&nbsp;

<br>

## Inicializar o projeto
O circuito do Arduino deve ser montado da seguinte forma: 

![arduino](https://github.com/felipeferrari22/reconhecimento-facial-arduino/assets/78982963/54664eee-e106-4db1-a201-1e43afc2d7ef) ![arduino2](https://github.com/felipeferrari22/reconhecimento-facial-arduino/assets/78982963/b2c1b633-80ac-40ca-bfdb-14abdb77ed9f)



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
