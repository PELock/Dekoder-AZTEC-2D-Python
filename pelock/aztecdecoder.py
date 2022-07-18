#!/usr/bin/env python

#
#
# Dekoder kodow AZTEC 2D z dowodow rejestracyjnych interfejs Web API
#
# Wersja         : AZTecDecoder v1.0
# Jezyk          : Python v3
# Zaleznosci     : requests (https://pypi.python.org/pypi/requests/)
# Autor          : Bartosz Wójcik (support@pelock.com)
# Strona domowa  : https://www.dekoderaztec.pl | https://www.pelock.com
#

import struct
import io
import json

# wymagany pakiet requests - instalacja komenda "pip install requests"
import requests

class AZTecDecoder(object):

    #
    # @var string domyslna koncowka WebApi
    #
    API_URL = "https://www.pelock.com/api/aztec-decoder/v1"

    #
    # @var string klucz WebApi do uslugi AZTecDecoder
    #
    _api_key = ""

    def __init__(self, api_key):
        """Inicjalizacja klasy AZTecDecoder

        :param api_key: Klucz do uslugi WebApi
        """

        self._api_key = api_key

    def decode_text(self, text):
        """Dekodowanie zaszyfrowanej wartosci tekstowej do
           wyjsciowej tablicy w formacie JSON.

        :param text: Odczytana wartosc z kodem AZTEC2D w formie ASCII
        :return Rozkodowana tablica elementow JSON lub None jesli blad
        :rtype object
        """

        # parametry
        params = {"command": "decode-text", "text": text}

        return self.post_request(params)

    def decode_text_from_file(self, text_file_path):
        """Dekodowanie zaszyfrowanej wartosci tekstowej
           ze wskaznego pliku do wyjsciowej tablicy z
           formatu JSON.

        :param text_file_path: Sciezka do pliku z odczytana wartoscia kodu AZTEC2D
        :return Rozkodowana tablica elementow JSON lub None jesli blad
        :rtype object
        """

        with open(text_file_path, 'r') as f:

            text = f.read()

            if text:

                return self.decode_text(text)

        return None

    def decode_image_from_file(self, image_file_path):
        """Dekodowanie zaszyfrowanej wartosci zakodowanej
           w obrazku PNG lub JPG/JPEG do wyjsciowej tablicy
           w formacie JSON.

        :param image_file_path: Sciezka do obrazka z kodem AZTEC2D
        :return Rozkodowana tablica elementow JSON lub None jesli blad
        :rtype object
        """
        # parametry
        params = {"command": "decode-image", "image": image_file_path}

        return self.post_request(params)

    def post_request(self, params_array):
        """Wysyla zapytanie POST do serwera WebApi

        :param params_array: Tablica z parametrami dla zapytania POST
        :return: Rozkodowana tablica elementow JSON lub None jesli blad
        :rtype: object
        """

        # czy jest ustawiony klucz Web API?
        if not self._api_key:

            return None

        # do parametrow dodaj klucz WebAPI
        params_array["key"] = self._api_key

        # ustaw poprawnie element z plikiem
        if "image" in params_array:

            files = {"image": open(params_array["image"], "rb")}
            params_array.pop("image", None)

            response = requests.post(self.API_URL, files=files, data=params_array)

        else:

            response = requests.post(self.API_URL, data=params_array)

        if response and response.ok:

            return json.loads(response.text)

        else:

            return None
