
# Fix misterPos: ultima slide wrong icon/title
path = '/Users/alessiomariani/siti_web/mister_up_new_v2/site/misterPos.html'
content = open(path, encoding='utf-8').read()

import re

# Fix the broken last slide in aboutMpos-swiper
# Find article containing "Personalizzare" and fix icon + title
def fix_article(m):
    block = m.group(0)
    if 'Personalizzare' in block:
        block = re.sub(r'linearicons-[\w-]+', 'linearicons-settings', block, count=1)
        block = re.sub(r'<div>(Igiene e sicurezza|Igiene)</div>', '<div>Personalizzazione</div>', block)
    return block

new = re.sub(r'<article class="counter-minimal[^>]*>.*?</article>', fix_article, content, flags=re.DOTALL)

if new != content:
    open(path, 'w', encoding='utf-8').write(new)
    print('OK misterPos')
else:
    print('SKIP misterPos - no change')

# Fix totem: header still says "Mister POS" and M4 description
path2 = '/Users/alessiomariani/siti_web/mister_up_new_v2/site/totem.html'
c2 = open(path2, encoding='utf-8').read()

# Fix product title
c2 = c2.replace(
    '<h3 class="section-title">Mister POS</h3>\n\n                    <h5 class="text-muted mb-3">\n                        Gestione Retail "in Cloud"\n                    </h5>',
    '<h3 class="section-title">Mister Totem</h3>\n\n                    <h5 class="text-muted mb-3">\n                        Il totem pubblicitario e gestionale per il tuo punto vendita\n                    </h5>'
)

# Fix product description (old M4 text)
c2 = c2.replace(
    "La cassa automatica rendi-resto <b>M4</b> è l'ideale per\n                        gestire in tranwuillità i pagamenti in medio/piccoli esercizi\n                        commerciali, laddove quotidianamente ci sia una buona affluenza\n                        di clientela e una buona mole di denaro in entrata ed uscita!",
    "Il <b>Mister Totem</b> è la soluzione digitale avanzata per il tuo punto vendita: gestionale, display pubblicitario e sistema di cassa integrati in un unico dispositivo touch, ideale per esercizi commerciali moderni."
)

# Fix typo "chiusurre"
c2 = c2.replace('chiusurre di cassa', 'chiusure di cassa')

# Fix "Cosa permette Mister POS" -> "Cosa permette Mister Totem" in totem
c2 = c2.replace(
    '<span class="wow slideInUp">Cosa permette Mister POS</span>',
    '<span class="wow slideInUp">Cosa permette Mister Totem</span>'
)
c2 = c2.replace(
    "<p style=\"font-size:20px;font-weight:200\">Caratteristiche più importanti del gestionale</p>",
    '<p style="font-size:20px;font-weight:200">Funzionalità principali</p>'
)

open(path2, 'w', encoding='utf-8').write(c2)
print('OK totem')
