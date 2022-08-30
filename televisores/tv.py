from televisores.marca import Marca
from televisores.control import Control
class TV:
    
    _numTV: int = 0

    def __init__(self, marca: Marca, estado: bool):
        self._marca: Marca = marca
        self._canal: int = 1
        self._precio: int = 500
        self._estado: bool = estado
        self._volumen: int = 1
        self._control: Control = None
        TV.numTV += 1

    def _canalValido(self, canal: int):
        MAX_CANAL: int = 120
        return self._estado and canal >= 1 and canal <= MAX_CANAL
    
    def _volumenValido(self, volumen: int):
        MAX_VOLUMEN: int = 7
        return self._estado and volumen >= 0 and volumen <= MAX_VOLUMEN


    def getMarca(self):
        return self._marca

    def getControl(self):
        return self._control

    def getPrecio(self):
        return self._precio

    def getVolumen(self):
        return self._volumen

    def getCanal(self):
        return self._canal

    def getNumTV():
        return TV._numTV

    def getEstado(self):
        return self._estado

    def setNumTV(self, numTV):
        TV._numTV = numTV

    def setMarca(self, marca: Marca):
        self._marca = marca

    def setControl(self, control: Control):
        self._control = control

    def setPrecio(self, precio: int):
        self._precio = precio

    def setVolumen(self, volumen: int):
        if self._volumenValido(volumen):
            self._volumen = volumen

    def setCanal(self, canal: int):
        if self._canalValido(canal):
            self._canal = canal

    

    
    def turnOn(self):
        self._estado = True
    
    def turnOff(self):
        self._estado = False

    def canalUp(self):
        nuevoCanal: int = self._canal + 1
        self._canal = self._canal = nuevoCanal if self._canalValido(nuevoCanal) else self._canal

    def canalDown(self):
        nuevoCanal: int = self._canal - 1
        self._canal = self._canal = nuevoCanal if self._canalValido(nuevoCanal) else self._canal

    def volumenUp(self):
        nuevoVolumen: int = self._volumen + 1
        self._volumen = self._volumen = nuevoVolumen if self._volumenValido(nuevoVolumen) else self._volumen

    def volumenDown(self):
        nuevoVolumen: int = self._volumen - 1
        self._volumen = self._volumen = nuevoVolumen if self._volumenValido(nuevoVolumen) else self._volumen

    
        