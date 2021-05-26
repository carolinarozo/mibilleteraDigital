from datetime import datetime

a = []
b = datetime.now()
print(b)
a.append(b.strftime("%A %d de %B del %Y hora %H:%M:%S"))
print(a)
c = datetime.now()
