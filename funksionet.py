'''
Funksionet në Python:

Në Python, një funksion është një bllok me emër i kodit që kryen një detyrë të caktuar. Funksionet na lejojnë të organizojmë kodin tonë në pjesë më të vogla dhe të përdorshme, duke e bërë më të lehtë leximin, kuptimin dhe mirëmbajtjen. Ato mund të marrin inpute, të quajtura argumente ose parametra, dhe mund të kthejnë rezultate.

Këtu është sintaksa e përgjithshme e përcaktimit të një funksioni në Python:

'''
def emri_i_funksionit(parametrat):
    # blloku i kodit
    return rezultati

'''
Le të shpjegojmë secilën pjesë të sintaksës së mësipërme:

- `def`: Kjo fjalë kyçe përdoret për të treguar fillimin e përcaktimit të një funksioni.
- `emri_i_funksionit`: Emri i dhënë funksionit, i cili ndjek konventën e emërimit në Python.
- `parametrat`: Këto janë inpute (të dhëna hyrëse) të dobishme që funksioni mund të pranojë. Ato janë të mbyllura me thonjëza dhe mund të përdoren brenda trupit të funksionit.
- `:`: Një pikëpresje përdoret në fund të së rreshti për të treguar fillimin e trupit të funksionit.
- `blloku i kodit`: Grupi i deklaratave që ekzekutohen kur funksioni thirret. Këto deklarata duhet të jenë të renditura me të njëjtin nivel kryerradhe.
- `return`: Kjo fjalë kyçe specifikon vlerën (rezultatin) që duhet të prodhojë funksioni dhe mbyll ekzekutimin e funksionit. Është e papërmbajtur dhe nëse nuk përmendet, funksioni do të kthejë `None`.

Pas përcaktimit të një funksioni, ne mund ta thërrasim atë më vonë në kodin tonë duke përdorur emrin e tij të pasuar nga thonjëzat. Nëse funksioni ka parametra, jepim vlerat e nevojshme për ato parametra brenda parantezave.

Këtu është një shembull i një funksioni të thjeshtë që shton dy numra:

'''
def shto_numrat(numri1, numri2):
    shuma = numri1 + numri2
    return shuma

rezultati = shto_numrat(3, 4)
print(rezultati)  # Output: 7

'''
Në kodin e mësipërm, përcaktojmë funksionin `shto_numrat` që merr dy parametra `numri1` dhe `numri2`. Brenda funksionit, llogarisim shumën e dy numrave dhe kthejmë rezultatin.

Pastaj thirrim funksionin `shto_numrat` me argumentet `3` dhe `4`, që cakton shumën e kthyer te variabla `rezultati`. Së fundi, printojmë vlerën e `rezultati`, që jep rezultatin `7`.
'''
