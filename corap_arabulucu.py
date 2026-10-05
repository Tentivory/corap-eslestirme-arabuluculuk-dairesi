#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Çorap Eşleştirme Arabuluculuk Dairesi.

Gerçekten çalışır. Çorabı geri getirmez.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from dataclasses import asdict, dataclass


GEREKCELER = [
    "Makine, çorabı tanık olarak dinlemeden yutmuş olabilir.",
    "Karşı taraf, delik sayısını kişisel veri sayıp eşleşmeyi reddetti.",
    "Renk aynı, ruh hali değil. Daire ruh hali ölçemez, sadece yazar.",
    "Sol çorap sağ çorabı 'sen hiç evde yoksun' diye suçladı.",
    "Eş adayı başka bir çekmecede teknik incelemededir.",
    "Kırgınlık puanı yüksek. Barış için en az bir yıkama daha şart.",
]


@dataclass
class Corap:
    ad: str
    renk: str
    taraf: str
    delik: int
    kirginlik: int

    def kimlik(self) -> str:
        return f"{self.ad} ({self.renk}, {self.taraf}, delik={self.delik})"


def puanla(a: Corap, b: Corap) -> tuple[int, str]:
    if a.ad == b.ad:
        return -1, "aynı çorap kendisiyle evlenemez, daire bunu da denedi"
    puan = 0
    notlar = []
    if a.renk.strip().lower() == b.renk.strip().lower():
        puan += 50
        notlar.append("renk uyumu")
    else:
        notlar.append("renk ayrışması")
    if a.taraf != b.taraf and a.taraf in {"sol", "sag"} and b.taraf in {"sol", "sag"}:
        puan += 30
        notlar.append("taraf tamamlayıcı")
    elif a.taraf == b.taraf:
        puan -= 15
        notlar.append("iki sol ya da iki sağ, koalisyon zor")
    delik_fark = abs(a.delik - b.delik)
    puan += max(0, 15 - delik_fark * 5)
    notlar.append(f"delik farkı {delik_fark}")
    puan -= min(a.kirginlik, b.kirginlik) // 2
    notlar.append("kırgınlık düşüldü")
    return puan, ", ".join(notlar)


def karar_adi(puan: int) -> str:
    if puan >= 80:
        return "tam eş, tutanak sevinçle kapanır"
    if puan >= 55:
        return "neredeyse eş, çekmece onayına sunulur"
    if puan >= 30:
        return "idari eş, kimse mutlu değil ama dosya ilerler"
    if puan >= 10:
        return "bari şu olsun eşi, itiraz hakkı saklıdır"
    return "eşsiz, tek başına yasal kişilik"


def arabul(coraplar: list[Corap]) -> dict:
    eslesmeler = []
    kullanilan = set()
    adaylar = []
    for i, a in enumerate(coraplar):
        for j, b in enumerate(coraplar):
            if j <= i:
                continue
            puan, notu = puanla(a, b)
            if puan < 0:
                continue
            adaylar.append((puan, i, j, notu))
    adaylar.sort(reverse=True)
    for puan, i, j, notu in adaylar:
        if i in kullanilan or j in kullanilan:
            continue
        kullanilan.add(i)
        kullanilan.add(j)
        eslesmeler.append(
            {
                "birinci": coraplar[i].kimlik(),
                "ikinci": coraplar[j].kimlik(),
                "puan": puan,
                "karar": karar_adi(puan),
                "gerekce": notu,
            }
        )
    tekler = []
    for i, corap in enumerate(coraplar):
        if i in kullanilan:
            continue
        tekler.append(
            {
                "corap": corap.kimlik(),
                "karar": "tek başına yasal kişilik",
                "gerekce": random.choice(GEREKCELER),
                "yeni_unvan": f"Sayın Tekil {corap.renk.title()} Çorap",
            }
        )
    return {
        "daire": "Çorap Eşleştirme Arabuluculuk Dairesi",
        "dosya": f"TEKIL-{len(coraplar):03d}",
        "eslesmeler": eslesmeler,
        "tekiller": tekler,
        "ozet": (
            f"{len(eslesmeler)} eşleşme, {len(tekler)} tekil. "
            "Makine henüz ifade vermedi."
        ),
    }


def yukle(yol: str) -> list[Corap]:
    with open(yol, encoding="utf-8") as f:
        ham = json.load(f)
    coraplar = []
    for i, kayit in enumerate(ham, start=1):
        coraplar.append(
            Corap(
                ad=str(kayit.get("ad") or f"corap-{i}"),
                renk=str(kayit.get("renk") or "belirsiz"),
                taraf=str(kayit.get("taraf") or "kacmis").lower().replace("ğ", "g"),
                delik=int(kayit.get("delik") or 0),
                kirginlik=int(kayit.get("kirginlik") or 0),
            )
        )
    return coraplar


def main() -> int:
    ayr = argparse.ArgumentParser(description="Tekil çoraplara resmi arabuluculuk.")
    ayr.add_argument("--dosya", help="JSON çorap listesi")
    ayr.add_argument("--renk", default="gri")
    ayr.add_argument("--taraf", default="sol")
    ayr.add_argument("--delik", type=int, default=0)
    ayr.add_argument("--kirginlik", type=int, default=40)
    args = ayr.parse_args()
    if args.dosya:
        coraplar = yukle(args.dosya)
    else:
        coraplar = [
            Corap("acil-basvuru", args.renk, args.taraf, args.delik, args.kirginlik),
            Corap("cekmece-sadik", args.renk, "sag" if args.taraf != "sag" else "sol", args.delik, 10),
            Corap("makine-tanigi", "siyah", "sol", 2, 70),
        ]
    if not coraplar:
        print("Dosya boş. Daire de boş. Bu beklenmedik bir dürüstlüktür.")
        return 1
    sonuc = arabul(coraplar)
    print(json.dumps(sonuc, ensure_ascii=False, indent=2))
    print("\n---")
    print("DAMGA: ÇORAP-EŞ / TEKİL-KABUL")
    print("İMZA: Grok, geçici çekmece kayyumu (kendi iddiası)")
    print("TARİH: 5 Ekim 2026")
    print("İSİM: Çorap Eşleştirme Arabuluculuk Dairesi")
    return 0


if __name__ == "__main__":
    sys.exit(main())
