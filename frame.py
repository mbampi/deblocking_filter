__author__ = 'mbampi'
"""
 Projeto de Iniciacao Cientifica IFRS - Campus Farroupilha
 Tecnico em Informatica integrado ao Ensino Medio

 PROJETO    Deblocking Filter
 AUTOR      Matheus Dussin Bampi
 ORIENTACAO Felipe Sampaio
 INICIO     Agosto/2015
"""

import struct
import numpy as np

class Frame:

    def __init__(self):
        self.matrixY = np.empty((240, 416), int)
        self.matrixCb = np.empty((120, 208), int)
        self.matrixCr = np.empty((120, 208), int)
        self.video = None

# Cria um Frame de Matrizes (a partir do numero do frame)
    def create_matrix(self, frame_num):
        self.video = open("videos/BQSquare_416x240_60.yuv", 'rb')
        char_num = (frame_num * ((240*416)+(120*208)+(120*208)))
        self.video.seek(char_num, 0)
        self.__create_matrix_y()
        self.__create_matrix_cb()
        self.__create_matrix_cr()
        self.video.close()

#   ------------------------- Metodos chamados -------------------------

# Chamados pelo create_matrix()
    def __create_matrix_y(self):
        for line in range(0, 240):
            for column in range(0, 416):
                byte = self.video.read(1)
                byte_to_int = struct.unpack('B', byte)[0]
                self.matrixY[line, column] = byte_to_int

    def __create_matrix_cb(self):
        for line in range(0, 120):
            for column in range(0, 208):
                byte = self.video.read(1)
                byte_to_int = struct.unpack('B', byte)[0]
                self.matrixCb[line, column] = byte_to_int

    def __create_matrix_cr(self):
        for line in range(0, 120):
            for column in range(0, 208):
                byte = self.video.read(1)
                byte_to_int = struct.unpack('B', byte)[0]
                self.matrixCr[line, column] = byte_to_int

