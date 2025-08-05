# BRAVE
```py
from br0wser.brave import *

base = Brave()
base.searcher("bolacha")

print("Título:", base.title)
print("Subtítulo:", base.subtitle)
print("Texto:", base.text)
print("Subtexto:", base.subtext)
print("Ficha:", base.ficha)
print("Subficha:")
for item in base.subficha:
    print(" -", item)
```
```
Título: Bolacha
Subtítulo: Bolo chato e seco de farinha, de diversas formas e tamanhos. Pode ser doce ou salgada
Texto: Bolacha é um bolo chato e seco de farinha de diversas formas e tamanhos. Pode ser consumida de diversas maneiras, doce, com recheios, salgada ou acompanhada de especiarias e/ou patês. O termo …
Subtexto: Wikipedia
Ficha:  Ficha de dados
Subficha:
 - Caractere unicode 🍪
```
