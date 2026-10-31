#!/usr/bin/env python3
"""Render the recovered static pages using shared templates. No dependencies."""
from pathlib import Path
from string import Template
from datetime import date
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE_URL = 'https://mscid.github.io'

def template(name):
    return Template((ROOT / 'templates' / name).read_text())

def build():
    version = hashlib.sha256((ROOT / 'personal.css').read_bytes()).hexdigest()[:12]
    pages = sorted((ROOT / 'site-source/pages').rglob('*.json'))
    for source in pages:
        data = json.loads(source.read_text())
        relative = source.relative_to(ROOT / 'site-source/pages').with_suffix('.html')
        url = '/' + str(relative).removesuffix('index.html')
        if url == '/404.html': canonical = ''
        else: canonical = BASE_URL + url
        head = data['head']
        head = re.sub(r'<link\b[^>]*rel="canonical"[^>]*>', '', head)
        if canonical: head += f'\n<link rel="canonical" href="{canonical}">'
        head = re.sub(r'(<meta property="og:url" content=")[^"]*("\s*/?>)', lambda m:m[1]+(canonical or BASE_URL)+m[2], head)
        # Replace exported theme's incorrect page URL advertised as an RSS feed.
        head = re.sub(r'<link\b[^>]*type="application/rss\+xml"[^>]*>', '', head)
        if url in ['/', '/posts/']:
            head += '\n<link rel="alternate" type="application/rss+xml" title="Dinan Mariano" href="/posts/index.xml">'
        content = data['content']
        # Preserve date values, displaying day precision instead of stale timezone labels.
        content = re.sub(r'<time\b[^>]*>(.*?)</time>', format_date, content, flags=re.S)
        links=[]
        for path,label in [('/about/','About'),('/projects/','Projects'),('/posts/','Writing'),('/cv/','CV')]:
            active = url.startswith(path) or (path=='/posts/' and url.startswith(('/tags/','/categories/','/archives/')))
            attrs = ' aria-current="page"' if active else ''
            cls = ' class="nav-cta"' if path=='/cv/' else ''
            links.append(f'<a href="{path}"{cls}{attrs}>{label}</a>')
        result=template('base.html').substitute(head=head,style_version=version,body_class=data['body_class'],main_attributes=data['main_attributes'],content=content,header=template('header.html').substitute(navigation=''.join(links)),footer=template('footer.html').substitute())
        target=ROOT/relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(result)
    # Keep existing sitemap entries and add previously missing public pages.
    ns='http://www.sitemaps.org/schemas/sitemap/0.9'
    ET.register_namespace('',ns)
    sitemap=ROOT/'sitemap.xml'; tree=ET.parse(sitemap); existing={x.text.lower() for x in tree.findall(f'.//{{{ns}}}loc')}
    for path in ['/about/','/projects/','/projects/thesis/','/cv/','/posts/spvm-28th-national-physics-conference/']:
        if (BASE_URL+path).lower() not in existing:
            ET.SubElement(ET.SubElement(tree.getroot(),f'{{{ns}}}url'),f'{{{ns}}}loc').text=BASE_URL+path
    tree.write(sitemap,encoding='utf-8',xml_declaration=True)
    print(f'Rendered {len(pages)} pages; stylesheet version {version}.')

def format_date(match):
    raw=match[1]
    found=re.search(r'\d{4}-\d{2}-\d{2}',raw)
    if not found: return match[0]
    day=found[0]
    label='Updated' if 'modified' in raw.lower() else 'Published'
    return f'<time datetime="{day}">{label} {date.fromisoformat(day):%B %d, %Y}</time>'

if __name__=='__main__': build()
