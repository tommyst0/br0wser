## DuckDuckGo
```py
from br0wser.duckduckgo import *

base = DuckDuckGo()

for i, link in enumerate(base.searcher_links("bolacha", 5), 1):
    print(f'{i}. {link}');
```
```
1. https://en.wikipedia.org/wiki/Bolo_de_bolacha
2. https://mariascookbook.com/bolo-de-bolacha/
3. https://www.homemadeinterest.com/bolo-de-bolacha-portuguese-biscuit-cake/
4. https://www.196flavors.com/portugal-bolo-de-bolacha/
5. https://pt.wikipedia.org/wiki/Bolacha
```

## MOJEEK
```py
from br0wser.mojeek import *

base = Mojeek()
base.searcher("bolacha")

print("Título:", base.title)
print("Subtítulo:", base.subtitle)
print("Texto:", base.text)
```
```
Título: Bolacha
Subtítulo: Bolo chato e seco de farinha, de diversas formas e tamanhos. Pode ser doce ou salgada
Texto: right|thumb|250px|Bolachas tipo cracker.|alt=Biscoito tipo craker Bolacha é um bolo chato e seco de farinha de diversas formas e tamanhos. Pode ser consumida de diversas maneiras, doce, com recheios, salgada ou acompanhada de especiarias e/ou patês.
```

## BRAVE
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
