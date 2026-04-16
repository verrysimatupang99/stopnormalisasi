# Layout Guide — Infomeme Carousel @stopnormalisasi.id
> Panduan visual layout per slide
> Tanggal: 2026-04-16
> Updated: 2026-04-16 (redesign visual + tambah spec font & warna final)

---

## Design Language

**Konsep:** Dark editorial. Serius tapi tidak dingin. Tegas tapi tidak arogan.

**Inspirasi visual:** Majalah editorial underground + UI dark mode modern.

**Prinsip:**
1. Slide 1 selalu teks only — hook harus kuat berdiri sendiri, tanpa visual
2. Slide 2-7: narasi di atas, meme di bawah — dipisah garis tipis merah-ke-transparan
3. Teks TIDAK pernah di-overlay di atas meme — keduanya blok terpisah
4. Meme punya caption sendiri — 1 kalimat, italic, abu-abu gelap
5. Slide 8 (CTA) teks only — kembali ke format teks murni

---

## Palet Warna

| Elemen | Kode | Keterangan |
|--------|------|------------|
| Background | `#0D0D0D` | Hitam sedikit warm, bukan pure black |
| Teks utama | `#F0F0F0` | Off-white, lebih nyaman dari pure white |
| Teks sekunder | `#E8E8E8` | Narasi body text |
| Teks dim | `#888888` | Informasi sekunder, sumber data |
| Teks ghost | `#444444` — `#333333` | Watermark, counter |
| Aksen utama | `#E63946` | Merah — untuk kata kunci, divider, accent bar |
| Background symbol | `#1a1a1a` | Untuk elemen dekoratif background (CTA slide) |

---

## Tipografi

| Elemen | Font | Weight | Size |
|--------|------|--------|------|
| Hook text (slide 1) | Inter | 900 (Black) | 58px |
| Label / tag | Inter | 600 | 13px |
| Slide counter | Inter | 700 | 12-13px |
| Narrative body | Inter | 400 | 30px |
| Narrative emphasis | Inter | 700 | 30px |
| CTA headline | Inter | 800 | 44px |
| CTA subtext | Inter | 400 | 24px |
| Hashtag | Inter | 400 | 18px |
| Meme caption | Inter | 400 italic | 18px |
| Watermark | Inter | 600 | 13-18px |

**Google Fonts link:**
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
```

---

## Elemen Desain Berulang

### Accent Bar (kiri)
Garis vertikal 4-5px di sisi kiri. Gradient merah ke transparan. Ada di semua slide sebagai brand consistency.

### Slide Counter
Format: `01 / 08` (angka aktif merah, total abu-abu). Posisi: pojok kiri bawah.

### Watermark
`@stopnormalisasi.id` — pojok kanan bawah, warna sangat gelap (`#2a2a2a` hingga `#444`). Selalu ada, tidak mengganggu.

### Label Tag
Teks kecil uppercase di pojok kiri atas (`STOP NORMALISASI`, `DISKUSI`, dll). Warna merah atau abu-abu gelap.

### Red Divider
Garis pendek 48px, height 4px, rounded. Dipakai setelah hook dan di CTA slide sebagai separator.

---

## Layout Per Slide

### SLIDE 1 — HOOK (teks only)
```
┌─────────────────────────────┐
│ [label: STOP NORMALISASI]   │  ← top-left, 13px merah
│                    [●]      │  ← corner dot merah, top-right
│                             │
│                             │
│  [HOOK TEXT]                │  ← left-aligned, 58px bold
│  max 3 baris                │
│                             │
│  [━━━━]                     │  ← red divider 48px
│                             │
│ 01 / 08    @stopnormalisasi │
└─────────────────────────────┘
  ↑ accent bar kiri (gradient)
```

### SLIDE 2-7 — NARASI + MEME
```
┌─────────────────────────────┐
│ [02 / 08]                   │  ← 12px merah, top-left
│                             │
│  [NARASI]                   │  ← 30px, line-height 1.7
│  4-7 baris                  │
│                             │
│ ━━━━━━━━━━━━━━━━━━━ →      │  ← separator merah-ke-transparan
│                             │
│      [MEME IMAGE]           │  ← max 580px wide, centered
│                             │
│   "caption meme italic"     │  ← 18px italic, abu-abu
│                             │
│                @stopnorm..  │
└─────────────────────────────┘
```

### SLIDE 8 — CTA
```
┌─────────────────────────────┐
│ [label: diskusi]            │  ← top-left, abu-abu
│                          ?  │  ← giant background ?, #1a1a1a
│                             │
│  [CTA QUESTION]             │  ← 44px bold
│                             │
│  [━━━━]                     │  ← red divider
│                             │
│  [sub text]                 │  ← 24px, abu-abu
│                             │
│  #tag1 #tag2 #tag3          │  ← 18px, merah
│                             │
│ @stopnormalisasi.id  08/08  │
└─────────────────────────────┘
```

---

## Spesifikasi Teknis (Instagram)

| Elemen | Nilai |
|--------|-------|
| Rasio | 1:1 (square) |
| Dimensi | 1080 × 1080px |
| Format output | PNG |
| Margin luar | 100px kiri/kanan, 60-70px atas/bawah |
| Meme max width | 580px |
| Meme max height | 280px |
| Meme border radius | 8px |

---

## Checklist Sebelum Export

- [ ] Slide 1: teks only, tidak ada gambar atau meme
- [ ] Setiap slide ada accent bar di kiri
- [ ] Setiap slide ada watermark @stopnormalisasi.id
- [ ] Setiap slide ada slide counter (01/08 dst)
- [ ] Narasi di atas, meme di bawah — bukan terbalik
- [ ] Caption meme tidak lebih dari 1 kalimat
- [ ] Slide 8: ada hashtag, ada handle, big ? background
- [ ] Data/angka di slide 3 ada sumber (kasual: "kata BPS")
- [ ] Tone check: provokatif tapi tidak agresif?
- [ ] DON'Ts check: preachy? elitist? clickbait?
