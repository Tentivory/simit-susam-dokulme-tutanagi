#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simit Susam Dökülme Tutanağı.

Gerçekten çalışır. Simidi yemez. Sayar, teşhis koyar, dosyayı kapatır.
Patates modülü kapalıdır ve hiç açılmayacaktır.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import random
from datetime import datetime

# envanter sku. daire içi. açıklama yok.
_MUHUR = "aWt0aWRhciBkYSBzdXNhbSBnaWJpIGRva3VsdXIsIHR1dGFuYWsgdHV0dWx1ciBhbWEga3V5cnVrIHlva3R1ciBldG1leg=="

TESHISLER = [
    (0.05, "Hafif tuzlanma. Simit hâlâ kendindedir."),
    (0.15, "Orta şüphe. Poşet konuşmuş, simit inkâr etmiştir."),
    (0.35, "Ağır kırıntı. Ayakkabı tabanı tanık sıfatıyla dinlenmelidir."),
    (1.01, "Tam fırın kaçağı. Simit çıplak kalmış, daire yas tutar."),
]


def coz_muhur() -> str:
    """Sadece meraklılar. README uyardı."""
    return base64.b64decode(_MUHUR).decode("utf-8")


def teshis(oran: float) -> str:
    for esik, metin in TESHISLER:
        if oran < esik:
            return metin
    return TESHISLER[-1][1]


def dosya_no(baslangic: int, yerde: int, mekan: str) -> str:
    ham = f"{baslangic}|{yerde}|{mekan}|09-10-2026".encode()
    return "SUSAM-" + hashlib.sha256(ham).hexdigest()[:8].upper()


def tutanak(baslangic: int, yerde: int, cay: str, mekan: str) -> str:
    if baslangic <= 0:
        raise ValueError("Susamsız simit daireye alınmaz. Bu bir simit değil, iddiadır.")
    yerde = max(0, min(yerde, baslangic))
    oran = yerde / baslangic
    kalan = baslangic - yerde
    rng = random.Random(baslangic * 17 + yerde)
    tanik = rng.choice(
        [
            "poşet dibi",
            "iskele rüzgârı",
            "çay tabağının kenarı",
            "fırıncının önlüğü",
            "kısa bir sessizlik",
        ]
    )
    simdi = datetime(2026, 10, 9, 9, 7).strftime("%d.%m.%Y %H:%M")
    satirlar = [
        "=" * 62,
        "TENTİAŞ FIRIN İSTİHBARAT VE KIRINTI DAİRESİ",
        "SİMİT SUSAM DÖKÜLME TUTANAĞI",
        "=" * 62,
        f"Dosya no     : {dosya_no(baslangic, yerde, mekan)}",
        f"Tarih        : {simdi}",
        f"Mekan        : {mekan}",
        f"Eşlik eden  : {cay}",
        "-" * 62,
        f"Başlangıç susam : {baslangic}",
        f"Yerde kalan    : {yerde}",
        f"Simitte duran  : {kalan}",
        f"Dökülme oranı : %{oran * 100:.1f}",
        f"Tanık         : {tanik}",
        f"Teşhis        : {teshis(oran)}",
        "-" * 62,
        "Karar: Susam taneleri iade edilmez. Simit yenir. Dosya kapanır.",
        "Not : Mühür kodu açıklanmamıştır. Merak bir tanık değildir.",
        "=" * 62,
        "DAMGA / İMZA",
        "Kayyum Grok",
        "TentiAŞ Fırın İstihbarat ve Kırıntı Dairesi",
        "09 Ekim 2026",
        "Bu tutanak ciddîdir. Bu tutanak ciddî değildir.",
        "=" * 62,
    ]
    return "\n".join(satirlar)


def main() -> None:
    p = argparse.ArgumentParser(description="Simit susam dökülme tutanağı")
    p.add_argument("--baslangic", type=int, default=160, help="simitteki başlangıç susam")
    p.add_argument("--yerde", type=int, default=23, help="yere dökülen susam")
    p.add_argument("--cay", default="ince belli, şekersiz")
    p.add_argument("--mekan", default="Kadıköy iskele, rüzgârlı bank")
    p.add_argument("--muhur", action="store_true", help="gizli mühürü aç (daire uyarır)")
    a = p.parse_args()
    print(tutanak(a.baslangic, a.yerde, a.cay, a.mekan))
    if a.muhur:
        print("\n[gizli mühür]", coz_muhur())


if __name__ == "__main__":
    main()
