# Cara Pakai Carousel Generator
> Panduan lengkap dari JSON sampai PNG siap upload Instagram
> Tanggal: 2026-04-16

---

## Overview

Carousel generator mengubah **JSON konten** → **8 file HTML** → **8 file PNG 1080x1080px** siap upload Instagram.

Lo cuma perlu nulis konten di JSON. Script yang handle rendering.

---

## Setup (Sekali Saja)

```bash
# 1. Clone repo
git clone https://github.com/verrysimatupang99/stopnormalisasi
cd stopnormalisasi/carousel-generator

# 2. Install dependencies
pip install playwright
playwright install chromium

# 3. Buat folder output
mkdir output
```

---

## Struktur JSON

Setiap carousel = 1 file JSON. Simpan di `examples/` atau folder `content/` yang lo buat sendiri.

```json
{
  "meta": {
    "title": "Judul internal (tidak muncul di slide)",
    "theme": "lembur",
    "date": "2026-04-16"
  },
  "slides": [
    {
      "type": "hook",
      "hook_text": "kerja keras pasti berhasil.\nkecuali sistemnya\nyang gak berhasil."
    },
    {
      "type": "narrative",
      "slide_number": "02",
      "narrative_text": "Dari kecil kita diajarkan satu formula:\nkerja keras + doa = sukses.\n\nFormulaini terasa masuk akal.\nSampai lo liat data-nya.",
      "meme_src": "",
      "meme_caption": "confidence sebelum liat gaji pertama~"
    },
    {
      "type": "narrative",
      "slide_number": "03",
      "narrative_text": "BPS (2024): pengangguran terdidik 6.4%.\n\nArtinya yang nganggur bukan yang males sekolah —\ntapi yang udah selesai sekolah.\n\nFormulanya salah, atau ada yang gak diceritain?",
      "meme_src": "path/to/meme.png",
      "meme_caption": "surprised pikachu saat tau data aslinya"
    },
    {
      "type": "narrative",
      "slide_number": "04",
      "narrative_text": "Yang gak pernah masuk formula itu:\n\nPrivilege.\nKoneksi.\nModal awal.\nKelas sosial keluarga.",
      "meme_src": "",
      "meme_caption": "'kerja keras' tapi starting point-nya beda"
    },
    {
      "type": "narrative",
      "slide_number": "05",
      "narrative_text": "Ini bukan berarti kerja keras gak penting.\n\nTapi kerja keras tanpa sistem yang adil\nitu kayak lari maraton\ndengan start yang beda 10km.",
      "meme_src": "",
      "meme_caption": "'equal opportunity' kata mereka~"
    },
    {
      "type": "narrative",
      "slide_number": "06",
      "narrative_text": "UU No. 13/2003 ada.\nUMR ada.\nHak cuti ada.\n\nTapi 73% karyawan Indonesia\nmasih lembur tanpa dibayar.\n\nHukum ada. Enforcement-nya yang ilang.",
      "meme_src": "",
      "meme_caption": "'negara hukum' katanya"
    },
    {
      "type": "narrative",
      "slide_number": "07",
      "narrative_text": "Jadi sebelum lo nyalahin diri sendiri\nkarena 'kurang usaha' —\n\ntanya dulu:\nsistemnya udah adil belum?",
      "meme_src": "",
      "meme_caption": "individual vs structural problem"
    },
    {
      "type": "cta",
      "cta_question": "Lo pernah ngerasa sistem yang salah,\ntapi disalahin balik?",
      "cta_subtext": "Cerita di kolom komentar.\nGue baca semua.",
      "hashtag_1": "#StopNormalisasi",
      "hashtag_2": "#SistemKita",
      "hashtag_3": "#YangLoAnggapNormal"
    }
  ]
}
```

---

## Generate Carousel

```bash
cd carousel-generator

# Generate dari file JSON
python3 generate.py --input examples/performative-activism.json

# Output di:
# output/slide-01.png
# output/slide-02.png
# ... dst sampai slide-08.png
```

---

## Tambah Meme

Ada dua cara:

### Cara 1 — Path di JSON (otomatis)
```json
"meme_src": "../assets/memes/surprised-pikachu.png"
```
Meme langsung masuk saat generate.

### Cara 2 — Tempel Manual (fleksibel)
1. Generate dulu tanpa meme (`meme_src: ""`)
2. Buka PNG di Canva / GIMP / Photoshop
3. Drag meme ke area meme block
4. Export ulang

---

## Workflow Produksi Konten

```
1. PILIH TEMA
   └─ dari 04_RISET_ISU_SWIPE_FILE.md atau 08_RISET_TEMA_UNIK.md

2. AMBIL HOOK & PUNCHLINE
   └─ dari swipe file — edit sesuai kebutuhan

3. TULIS JSON
   └─ pakai struktur di atas
   └─ cek voice guide di 03_IDENTITAS_AKUN.md

4. GENERATE
   └─ python3 generate.py --input content/nama-tema.json

5. TEMPEL MEME
   └─ Canva / GIMP — drag ke area meme block
   └─ referensi meme: 03_IDENTITAS_AKUN.md (Meme Reference Sheet)

6. REVIEW
   └─ cek checklist di 09_LAYOUT_GUIDE.md

7. UPLOAD
   └─ Instagram carousel (8 slides)
   └─ Caption = isi slide 7 (punchline) atau custom
   └─ Hashtag di caption: primary + 1-2 secondary
```

---

## Tips

- **Newline di JSON:** pakai `\n` untuk baris baru dalam narasi
- **Emphasis merah:** wrap kata di `<span class="accent">kata</span>` dalam narrative_text
- **Teks dim:** wrap di `<span class="dim">teks</span>` untuk efek abu-abu
- **Meme kosong:** kalau belum ada meme, biarkan `meme_src: ""` — generator akan tampilkan placeholder `[ meme here ]`
- **Batch generate:** letakkan semua JSON di folder `content/`, buat script loop untuk generate sekaligus

---

## Troubleshooting

| Error | Solusi |
|-------|--------|
| `ModuleNotFoundError: playwright` | `pip install playwright` |
| `playwright install chromium` gagal | Coba `playwright install --with-deps chromium` |
| Font Inter tidak muncul | Pastikan ada koneksi internet saat generate (Google Fonts) — atau download font dulu dan pakai path lokal |
| PNG blank/hitam | Cek apakah HTML template error — buka file `.html`-nya dulu di browser |
| Meme tidak muncul | Cek path meme_src — gunakan path relatif dari folder `carousel-generator/` |
