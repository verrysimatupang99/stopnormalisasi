#!/usr/bin/env python3
"""
Carousel Generator untuk @stopnormalisasi.id
Generate Instagram carousel post (1080x1080) dari HTML template.

Usage:
    python generate.py --input example.json          # Generate dari JSON config
    python generate.py --input example.json --open    # Generate + buka di browser

Dependensi:
    pip install playwright
    playwright install chromium
"""

import argparse
import json
import os
import sys
from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent / "templates"
OUTPUT_DIR = Path(__file__).parent / "output"

# Slide type mapping
SLIDE_TYPES = {
    "hook": "slide_hook.html",
    "narrative": "slide_narrative.html",
    "cta": "slide_cta.html",
}


def load_template(slide_type: str) -> str:
    """Load HTML template."""
    template_file = SLIDE_TYPES.get(slide_type, "slide_narrative.html")
    template_path = TEMPLATES_DIR / template_file
    
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    
    return template_path.read_text(encoding="utf-8")


def render_hook_slide(html: str, slide_data: dict) -> str:
    """Replace placeholders in hook slide template."""
    hook_text = slide_data.get("text", "")
    # Support <span class="accent"> for highlighted words
    hook_text = hook_text.replace("{{accent:", '<span class="accent">').replace("}}", "</span>")
    
    html = html.replace("{{HOOK_TEXT}}", hook_text)
    return html


def render_narrative_slide(html: str, slide_data: dict, slide_num: int) -> str:
    """Replace placeholders in narrative slide template."""
    html = html.replace("{{SLIDE_NUM}}", str(slide_num))
    html = html.replace("{{SLIDE_LABEL}}", slide_data.get("label", ""))
    
    # Narrative text with highlight support
    narrative = slide_data.get("text", "")
    narrative = narrative.replace("{{highlight:", '<span class="highlight">').replace("}}", "</span>")
    narrative = narrative.replace("{{data:", '<span class="data">').replace("}}", "</span>")
    narrative = narrative.replace("\n", "<br>")
    html = html.replace("{{NARRATIVE_TEXT}}", narrative)
    
    # Meme image
    meme_path = slide_data.get("meme", "")
    if meme_path and os.path.exists(meme_path):
        abs_path = os.path.abspath(meme_path)
        meme_html = f'<img src="file://{abs_path}" alt="meme">'
    else:
        meme_html = '<div class="meme-placeholder">[MEME: tempel di sini]</div>'
    html = html.replace("{{MEME_IMAGE}}", meme_html)
    
    # Meme caption
    html = html.replace("{{MEME_CAPTION}}", slide_data.get("meme_caption", ""))
    
    return html


def render_cta_slide(html: str, slide_data: dict) -> str:
    """Replace placeholders in CTA slide template."""
    cta_text = slide_data.get("text", "")
    cta_text = cta_text.replace("{{accent:", '<span class="accent">').replace("}}", "</span>")
    cta_text = cta_text.replace("\n", "<br>")
    
    html = html.replace("{{CTA_TEXT}}", cta_text)
    html = html.replace("{{HASHTAGS}}", slide_data.get("hashtags", ""))
    return html


def generate_html_slides(config: dict) -> list[tuple[str, str]]:
    """Generate HTML for each slide. Returns list of (filename, html_content)."""
    slides = []
    project_name = config.get("project", "carousel")
    
    for i, slide_data in enumerate(config.get("slides", []), 1):
        slide_type = slide_data.get("type", "narrative")
        template = load_template(slide_type)
        
        if slide_type == "hook":
            html = render_hook_slide(template, slide_data)
        elif slide_type == "cta":
            html = render_cta_slide(template, slide_data)
        else:
            html = render_narrative_slide(template, slide_data, i)
        
        filename = f"{project_name}_slide_{i:02d}_{slide_type}.html"
        slides.append((filename, html))
    
    return slides


def save_html_files(slides: list[tuple[str, str]], output_dir: Path) -> list[Path]:
    """Save HTML files to output directory."""
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    
    for filename, html in slides:
        path = output_dir / filename
        path.write_text(html, encoding="utf-8")
        paths.append(path)
        print(f"  ✓ {filename}")
    
    return paths


def convert_to_png(html_paths: list[Path], output_dir: Path) -> list[Path]:
    """Convert HTML files to PNG using Playwright."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("\n⚠️  Playwright not installed. Run:")
        print("   pip install playwright")
        print("   playwright install chromium")
        print("\nHTML files saved. Convert manually or install Playwright.")
        return []
    
    png_paths = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        
        for html_path in html_paths:
            page = browser.new_page(viewport={"width": 1080, "height": 1080})
            page.goto(f"file://{html_path.absolute()}")
            page.wait_for_timeout(500)
            
            png_path = output_dir / (html_path.stem + ".png")
            page.screenshot(path=str(png_path), type="png")
            png_paths.append(png_path)
            print(f"  ✓ {png_path.name}")
            page.close()
        
        browser.close()
    
    return png_paths


def main():
    parser = argparse.ArgumentParser(description="Generate Instagram carousel for @stopnormalisasi.id")
    parser.add_argument("--input", "-i", required=True, help="JSON config file")
    parser.add_argument("--html-only", action="store_true", help="Only generate HTML, skip PNG conversion")
    parser.add_argument("--open", action="store_true", help="Open first slide in browser after generation")
    
    args = parser.parse_args()
    
    # Load config
    config_path = Path(args.input)
    if not config_path.exists():
        print(f"Error: {config_path} not found")
        sys.exit(1)
    
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    project_name = config.get("project", "carousel")
    output_dir = OUTPUT_DIR / project_name
    
    print(f"\n🎨 Generating carousel: {project_name}")
    print(f"   Slides: {len(config.get('slides', []))}")
    print(f"   Output: {output_dir}\n")
    
    # Generate HTML
    print("📄 HTML files:")
    slides = generate_html_slides(config)
    html_paths = save_html_files(slides, output_dir)
    
    # Convert to PNG
    if not args.html_only:
        print("\n🖼️  PNG conversion:")
        png_paths = convert_to_png(html_paths, output_dir)
        if png_paths:
            print(f"\n✅ Done! {len(png_paths)} PNG files in {output_dir}")
        else:
            print(f"\n⚠️  HTML saved, PNG conversion failed. Check Playwright installation.")
    else:
        print(f"\n✅ Done! {len(html_paths)} HTML files in {output_dir}")
    
    # Open in browser
    if args.open and html_paths:
        import webbrowser
        webbrowser.open(f"file://{html_paths[0].absolute()}")


if __name__ == "__main__":
    main()
