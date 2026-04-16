# Carousel Generator @stopnormalisasi.id

Generate Instagram carousel post (1080x1080) dari HTML/CSS template.

## Cara Pakai

### 1. Install dependency
```bash
pip install playwright
playwright install chromium
```

### 2. Buat JSON config
```bash
cp examples/performative-activism.json my-carousel.json
# Edit my-carousel.json dengan konten lo
```

### 3. Generate
```bash
# Generate HTML + PNG
python generate.py --input my-carousel.json

# Generate HTML only (tanpa PNG)
python generate.py --input my-carousel.json --html-only

# Generate + buka di browser
python generate.py --input my-carousel.json --open
```

### 4. Output
PNG files ada di `output/<project-name>/`
Upload ke Instagram sebagai carousel.

## Format JSON

```json
{
  "project": "nama-proyek",
  "slides": [
    {
      "type": "hook",                    // Slide 1
      "text": "teks hook..."
    },
    {
      "type": "narrative",               // Slide 2-7
      "label": "SETUP",                  // Label di atas
      "text": "narasi teks...",          // Konten utama
      "meme": "path/to/meme.png",        // Opsional: gambar meme
      "meme_caption": "caption meme"     // Caption di bawah meme
    },
    {
      "type": "cta",                     // Slide 8
      "text": "ajakan...",
      "hashtags": "#hashtag1 #hashtag2"
    }
  ]
}
```

## Highlight Syntax

Di dalam `text`, pakai syntax berikut untuk styling:

- `{{highlight:teks}}` → teks merah (#E63946), bold
- `{{data:angka}}` → angka merah, lebih besar
- `<br>` → line break

Contoh:
```json
"text": "penelitian dari {{highlight:Harvard (2021)}} nemu bahwa {{data:67%}} pekerja..."
```

## Templates

| Template | File | Untuk |
|----------|------|-------|
| Hook | `templates/slide_hook.html` | Slide 1 (teks only) |
| Narrative | `templates/slide_narrative.html` | Slide 2-7 (narasi + meme) |
| CTA | `templates/slide_cta.html` | Slide 8 (ajakan + hashtag) |

## Customisasi

Edit template HTML untuk ganti:
- Warna brand (background, aksen, teks)
- Font family
- Layout spacing
- Ukuran slide (default 1080x1080)

## Meme Images

Untuk slide dengan meme:
1. Simpan gambar meme di folder manapun
2. Set `"meme": "path/to/meme.png"` di JSON
3. Generator akan embed otomatis

Kalau gak ada meme, muncul placeholder "[MEME: tempel di sini]".
Bisa edit manual di HTML atau tempel di Canva/Figma setelah generate.
