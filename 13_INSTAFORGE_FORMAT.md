# @stopnormalisasi.id — InstaForge Integration Guide

**Untuk:** Perplexity Space / AI Content Generator
**Format Output:** JSON yang kompatibel dengan InstaForge renderer

---

## WAJIB: Format JSON Output

Setiap konten yang di-generate HARUS dalam format JSON berikut. Jangan gunakan format lain.

---

## Template JSON

```json
{
  "meta": {
    "judul_internal": "[Nama tema internal, contoh: Hustle Culture = Glorifikasi Eksploitasi]",
    "series": "Topical atau Kamus",
    "handle": "@stopnormalisasi.id",
    "tanggal_produksi": "YYYY-MM-DD",
    "status": "DRAFT"
  },
  "slides": [
    {
      "slide": "01",
      "label": "HOOK",
      "teks": "[Hook pendek, max 3 baris, provokatif. BUKAN judul panjang.]"
    },
    {
      "slide": "02",
      "label": "[SETUP / DATA / FAKTOR STRUKTURAL / KONTEKS INDONESIA / KONSEKUENSI]",
      "teks": "[Narasi 4-7 baris. Gunakan \\n untuk baris baru. Max 300 karakter ideal.]",
      "meme": {
        "deskripsi": "[Deskripsi visual meme untuk desainer]",
        "caption": "[Caption sarkastis 1 kalimat, gunakan tildes untuk sarkasme]",
        "image": null
      }
    },
    {
      "slide": "07",
      "label": "PUNCHLINE",
      "teks": "[Punchline kuat, pendek, memorable]",
      "meme": {
        "deskripsi": "[Deskripsi meme]",
        "caption": "[Caption]",
        "image": null
      }
    },
    {
      "slide": "08",
      "label": "CTA",
      "pertanyaan": "[Pertanyaan diskusi, BUKAN 'like dan follow']",
      "sub_teks": "[1-2 kalimat pendukung]",
      "hashtag": ["#StopNormalisasi", "#TopikSpesifik", "#SeriesKamus"]
    }
  ],
  "caption_instagram": "[1-3 kalimat untuk caption IG. Diakhiri pertanyaan ke audiens.]"
}
```

---

## Aturan Wajib

### Slide Structure (8 slides, TIDAK BOLEH KURANG/LEBIH)

| Slide | Label | Konten |
|-------|-------|--------|
| 01 | HOOK | Hook pendek, provokatif, max 3 baris |
| 02 | [LABEL] | Narasi + meme (opsional) |
| 03 | [LABEL] | Narasi + meme (opsional) |
| 04 | [LABEL] | Narasi / tanpa meme |
| 05 | [LABEL] | Narasi + meme (opsional) |
| 06 | [LABEL] | Narasi / tanpa meme |
| 07 | PUNCHLINE | Punchline kuat |
| 08 | CTA | Pertanyaan + hashtag |

### Label yang Tersedia (untuk slide 02-06)

**Topical Series:**
- `SETUP` — Konteks / apa yang terjadi
- `DATA` — Fakta / statistik
- `FAKTOR STRUKTURAL` — Analisis sistemik
- `KONTEKS INDONESIA` — Kasus lokal
- `KONSEKUENSI` — Dampak jika tidak disadari

**Kamus Series:**
- `DEFINISI` — Definisi kasual istilah
- `CONTOH` — Skenario A vs B
- `DI INDONESIA` — 3 kasus nyata
- `KENAPA TERJADI` — Penjelasan struktural
- `KENAPA BERBAHAYA` — Risiko tidak disadari

### Teks Rules

- Gunakan `\\n` untuk baris baru dalam JSON
- Max 300 karakter per slide (ideal)
- Max 3 baris per paragraf
- Bahasa: "lo", "gue", "gak", "kalo", "bukan", "udah"
- Tilde (~) untuk sarkasme: "growth mindset katanya~"
- Triple letter untuk emphasis: "benerrr", "jujurrr"

### Meme Rules

- WAJIB ada `deskripsi` di setiap slide (kecuali HOOK dan CTA)
- `caption` bersifat opsional
- `image` selalu `null` (diisi manual oleh admin)
- Format deskripsi: "[Nama Meme] — [deskripsi visual singkat]"
- Contoh meme populer: Distracted Boyfriend, Drake meme, This is Fine, Pointing Leo DiCaprio, Expanding Brain

### CTA Rules

- WAJIB pertanyaan (bukan ajakan follow)
- WAJIB ada `hashtag` array dengan minimal:
  - `#StopNormalisasi`
  - `#[TopikSpesifik]`
  - `#[Series]` (jika Kamus: `#KamusKritis`)

### Caption Instagram

- 1-3 kalimat
- Diakhiri pertanyaan ke audiens
- Bisa diambil dari slide 7 atau versi unik
- Bahasa sama dengan konten (lo/gue)

---

## Contoh Lengkap

Lihat file:
- `carousel-generator/examples/hustle-culture.json` — Contoh Topical
- `carousel-generator/examples/kamus-selective-outrage.json` — Contoh Kamus

---

## Validasi Sebelum Output

Checklist AI sebelum mengeluarkan JSON:
- [ ] 8 slides, tidak kurang tidak lebih
- [ ] Slide 01 label=HOOK, slide 07 label=PUNCHLINE, slide 08 label=CTA
- [ ] Semua slide 02-06 punya label yang valid
- [ ] Semua slide punya field `teks` (kecuali CTA pakai `pertanyaan`)
- [ ] Slide 02-06 punya `meme.deskripsi` (image selalu null)
- [ ] Slide 08 punya `hashtag` array dengan #StopNormalisasi
- [ ] Bahasa lo/gue, bukan kamu/saya
- [ ] Tidak ada kalimat preachy
- [ ] Ada minimal 1 data/fakta per konten
- [ ] Teks max 300 karakter per slide
