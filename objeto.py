from Criptomonedas import Criptomoneda
ethereum = Criptomoneda("ETH ", 0.0, 454.543)
print(ethereum.mostrarNombre(), ethereum.calcularSaldo("USD"))
bitcoin = Criptomoneda("BTC", 0.34, 5000.00)
print(bitcoin.mostrarNombre())
print(bitcoin.calcularSaldo("USD"))
print(bitcoin.indicarSaldo(0.5))
print(bitcoin.calcularSaldo("USD"))


ripple = Criptomoneda("XPR", 34.93, 0.4785)
print(ripple.mostrarNombre())
print(ripple.indicarNombre("XRP"))
print(ripple.mostrarNombre())
print(ripple.calcularSaldo("USD"))
