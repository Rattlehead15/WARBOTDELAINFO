# Copyright (c) 2015–2016 Molly White
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import tweepy
from secrets import *
from time import gmtime, strftime


# ====== Individual bot configuration ==========================
bot_username = ''
logfile_name = bot_username + ".log"

# ==============================================================

from secrets import *
import time
import random
from jinja2 import Template
import imgkit

class personaje:
    def __init__(self, nombre, vivo = True):
        self.nombre = nombre
        self.vivo = vivo
    def __eq__(self, other):
        return self.nombre == other.nombre


if __name__ == "__main__":
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    famosos = list(map(lambda x: x.strip(), open("contendientes.txt", encoding='utf-8').readlines()))
    famososConEstado = list(map(lambda x: personaje(x), famosos))
    mensajes = open("asesinatos.txt", encoding='utf-8').readlines()

    template = Template(open("template.html", encoding='utf-8').read())
    while len(famosos) >= 2:
        print("Voy a decir la nword")
        seVanACagarAPiñas = random.sample(famosos, 2)
        mensaje = random.sample(mensajes, 1)[0]
        mensajeParaTweetear = mensaje.replace("UNO", seVanACagarAPiñas[0]).replace("DOS", seVanACagarAPiñas[1])
        famososConEstado[famososConEstado.index(personaje(seVanACagarAPiñas[1]))].vivo = False
        famosos.remove(seVanACagarAPiñas[1])
        mensajes.remove(mensaje)
        html = template.render(personajes=famososConEstado)
        imgkit.from_string(html, 'out.jpg')
        api.update_with_media('out.jpg', status=mensajeParaTweetear)
        time.sleep(10)

    api.update_status("Gano el picante de " + famosos[0])