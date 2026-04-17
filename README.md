# @stopnormalisasi.id — Brand Repository

> Semua dokumen riset, identitas, teknik konten, dan referensi untuk akun Instagram **@stopnormalisasi.id**.

---

## Tentang Akun

@stopnormalisasi.id adalah akun social commentary Indonesia yang mengungkap hal-hal yang dianggap "normal" padahal bermasalah — dari sistem kerja, pendidikan, budaya, sampai aktivisme palsu. Bukan ceramah, bukan lecture. Lebih kayak temen yang kritis, sarkas tipis-tipis, tapi selalu berbasis data dan empati.

**Tagline:** *"Yang lo anggap normal, belum tentu bener."*

---

## Struktur Dokumen

| File | Isi |
|------|-----|
| `00_MASTER_BRAND_DOCUMENT.md` | Dokumen master lengkap — semua bagian dalam satu file (untuk Gemini Gem / Notion) |
| `01_REFERENSI_AKUN_ANALISIS.md` | Analisis gaya bahasa 8 akun referensi |
| `02_TEKNIK_KONTEN.md` | 7 teknik penulisan konten & komedi |
| `03_IDENTITAS_AKUN.md` | Visi, misi, target audiens, voice guide, meme reference |
| `04_RISET_ISU_SWIPE_FILE.md` | 8 tema campaign + kamus istilah + hook & punchline siap pakai |
| `05_DNA_SYNTHESIS.md` | Satu paragraf yang define akun secara utuh |
| `06_TEMPLATE_CAROUSEL.md` | Template struktur 8 slide baku |
| `07_CONTOH_KONTEN_PERFORMATIVE_ACTIVISM.md` | Contoh carousel lengkap 8 slide |
| `08_RISET_TEMA_UNIK.md` | 6 tema unik + dasar hukum & data |
| `09_LAYOUT_GUIDE.md` | Panduan visual layout infomeme per slide + spec font & warna |
| `10_RIVAL_KOMPETITOR_ANALYSIS.md` | Analisis akun serupa di Indonesia + gap analysis |
| `11_CARA_PAKAI_GENERATOR.md` | Panduan carousel generator: setup, JSON schema, workflow produksi |
| `12_SERIES_KAMUS.md` | Series Kamus Istilah — daftar 15 istilah + status produksi + template |

---

## Carousel Generator

```
carousel-generator/
├── generate.py
├── templates/
│   ├── slide_hook.html
│   ├── slide_narrative.html
│   └── slide_cta.html
└── examples/
    ├── performative-activism.json
    ├── selective-outrage-fhui-lany.json      ← Konten topical April 2026
    └── kamus-selective-outrage.json          ← Series Kamus: Selective Outrage
```

---

## Cara Pakai

**Untuk Gemini Gem / AI assistant:**
Paste isi `00_MASTER_BRAND_DOCUMENT.md` sebagai system prompt atau konteks awal.

**Untuk bikin konten:**
1. Pilih tema dari `04_RISET_ISU_SWIPE_FILE.md` atau `08_RISET_TEMA_UNIK.md`
2. Ambil hook dari swipe file
3. Pakai template dari `06_TEMPLATE_CAROUSEL.md`
4. Cek voice dari `03_IDENTITAS_AKUN.md`
5. Pilih meme dari meme reference sheet
6. Generate PNG: `python3 generate.py --input examples/nama-file.json`

**Untuk Series Kamus:**
Lihat `12_SERIES_KAMUS.md` — pilih istilah yang belum dibuat, gunakan template JSON kamus.

**Untuk review konten sebelum post:**
Cek checklist voice guide (DO's & DON'Ts) di `03_IDENTITAS_AKUN.md` dan `09_LAYOUT_GUIDE.md`.

---

*Last updated: 2026-04-18*
