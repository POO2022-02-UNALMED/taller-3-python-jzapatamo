class Control:
    
    def __init__(self):
        self._tv = None


    def _validarEnlazado(self):
        return self._tv != None

    def getTv(self):
        return self._tv

    def setTv(self, tv):
        self._tv = tv

    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)

    def turnOn(self):
        if self._validarEnlazado():
            self._tv.turnOn()
    
    def turnOff(self):
        if self._validarEnlazado():
            self._tv.turnOff()

    def canalUp(self):
        if self._validarEnlazado():
            self._tv.canalUp()

    def canalDown(self):
        if self._validarEnlazado():
            self._tv.canalDown()

    def volumenUp(self):
        if self._validarEnlazado():
            self._tv.volumenUp()

    def volumenDown(self):
        if self._validarEnlazado():
            self._tv.volumenDown()

    def setCanal(self, canal: int):
        if self._validarEnlazado():
            self._tv.setCanal(canal)