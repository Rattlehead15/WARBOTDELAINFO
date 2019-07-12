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
if __name__ == "__main__":
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    famosos = ["Marcos", "Bachur", "Gony", "LUCIO BOTTI"]

    while(True):
        print("Voy a decir la nword")
        seVanACagarAPiñas = random.sample(famosos, 2)
        api.update_status(seVanACagarAPiñas[0] + " destruyó a " + seVanACagarAPiñas[1] + " y le dabeó en la cara")
        famosos.remove(seVanACagarAPiñas[1])
        time.sleep(10)