"""
[JAWABAN ASSIGNMENT WEEK 07]

Aturan pengisian:
- Implementasikan fungsi q01()..q12() sesuai soal di assignments/w07/quiz.qmd
- Jangan ubah nama fungsi.

Format jawaban:
- T/F     -> bool  (True=Benar, False=Salah)
- MC      -> str   ("A"/"B"/"C"/"D")
- Numeric -> int/float (desimal pakai '.')
"""

from __future__ import annotations

def q01() -> bool:
    """
    [T/F] Total luas di bawah kurva fungsi padat probabilitas (PDF) selalu sama dengan 1.
    """
    raise NotImplementedError

def q02() -> bool:
    """
    [T/F] Distribusi Normal Standar memiliki mean 0 dan variansi 1.
    """
    raise NotImplementedError

def q03() -> bool:
    """
    [T/F] Pada distribusi kontinu, P(X <= x) selalu sama dengan P(X < x).
    """
    raise NotImplementedError

def q04() -> str:
    """
    [MC] Nilai Z yang bersesuaian dengan nilai X pada distribusi N(mu, sigma^2) adalah:
     A) (X-mu)/sigma
     B) (X+mu)/sigma
     C) sigma/(X-mu)
     D) X-mu
    """
    raise NotImplementedError

def q05() -> str:
    """
    [MC] Distribusi mana yang sering digunakan untuk memodelkan waktu antar kejadian dalam proses Poisson?
     A) Binomial.
     B) Normal.
     C) Eksponensial.
     D) Uniform.
    """
    raise NotImplementedError

def q06() -> str:
    """
    [MC] Sekitar 95% data dalam distribusi Normal berada dalam rentang:
     A) mu ± sigma
     B) mu ± 2sigma
     C) mu ± 3sigma
     D) 0 ± 1
    """
    raise NotImplementedError

def q07() -> str:
    """
    [MC] Jika lambda = 0,5 pada distribusi Eksponensial, maka nilai harapannya adalah:
     A) 0,5
     B) 2,0
     C) 1,0
     D) 0,25
    """
    raise NotImplementedError

def q08() -> float:
    """
    [Numeric] Jika Z ~ N(0,1), berapakah P(Z <= 0)?
    """
    raise NotImplementedError

def q09() -> float:
    """
    [Numeric] Sebuah komponen memiliki rata-rata waktu hidup 100 jam (Eksponensial). Berapakah parameter lambda-nya?
    """
    raise NotImplementedError

def q10() -> float:
    """
    [Numeric] Nilai Z untuk probabilitas kumulatif 0,975 adalah sekitar... (Gunakan 2 desimal)
    """
    raise NotImplementedError

def q11() -> float:
    """
    [Numeric] Jika X ~ N(10, 4), berapakah nilai skor-Z untuk X = 12?
    """
    raise NotImplementedError

def q12() -> float:
    """
    [Numeric] Pada distribusi Normal Standar, berapakah nilai P(Z > 3) mendekati? (Gunakan 4 desimal)
    """
    raise NotImplementedError
