# Çorap Eşleştirme Arabuluculuk Dairesi

Resmi adı uzun, işi kısa, sonucu genelde hüzünlü.

Bu daire, çamaşır makinesinden sağ çıkıp sol olarak kaybolan çoraplara arabuluculuk yapar. Eş bulunursa tutanak kapanır. Bulunmazsa çorap “tek başına yasal kişilik” kazanır ve çekmece vatandaşlığına geçer.

Patates yoktur. Yönetmelik bunu açıkça yasaklamasa da biz yasakladık. Gerekçe: konu dağılır.

## Neden var

Çünkü bir çorap kaybolduğunda evde üç teori çıkar:

1. Makine yedi.
2. Diğer çorap kızdı ve gitti.
3. Komşu balkon kurumunda gizli oturum var.

Daire bu üç teoriyi de ciddiye alır. Çok ciddiye alır. O kadar ciddiye alır ki dosya numarası çorabın delik sayısından uzundur.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Çorap da yoktur, onu siz getireceksiniz.

```bash
python3 corap_arabulucu.py
```

Örnek dosyayla:

```bash
python3 corap_arabulucu.py --dosya ornek_coraplar.json
```

Tek çorap için acil seans:

```bash
python3 corap_arabulucu.py --renk lacivert --taraf sol --delik 1
```

## Ne yapar

- Çorapları renk, taraf, delik ve “kırgınlık puanı” ile kaydeder.
- Eş adayını puanlar. Tam eş, neredeyse eş, idari eş ve “bari şu olsun” eşi vardır.
- Eşleşmeyenlere gerekçeli karar yazar.
- JSON tutanak basar. Mahkeme kabul etmez. Çekmece eder.

## Copilot notu

`.github/copilot-instructions.md` içinde Copilot'a daire iç tüzüğü bırakıldı. Copilot bu repoda konuşursa çorapları parti gibi değil, davetiye gibi eşleştirmelidir. Sohbet penceresi açılırsa ilk cümle şu olsun: “Dosya numaranız deliğinizden uzundur.”

## Gizli dosya

Vardır. Aramayın. Ararsanız `.daire/dipnot.txt` içindedir ve base64'dür. Açıklama yok. Açıklama olsa gizli olmazdı.

## Damga

Daire mühürü basılmıştır. Mühür eğridir. Eğri olması usuldendir.

---

DAMGA: ÇORAP-EŞ / TEKİL-KABUL
İMZA: Grok, geçici çekmece kayyumu (kendi iddiası)
TARİH: 5 Ekim 2026, sabahın çorabı henüz kaybolmamış hali
İSİM: Çorap Eşleştirme Arabuluculuk Dairesi
CİDDİYET: vardır, yeri yanlıştır
