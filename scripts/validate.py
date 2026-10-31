#!/usr/bin/env python3
"""Check all current-site outputs and the preservation manifest, offline."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib,json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):
  super().__init__(); self.links=[];self.ids=[];self.mains=0;self.inside=False;self.words=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='main':self.mains+=1;self.inside=True
  if a.get('id'):self.ids.append(a['id'])
  for key in ('src','href'):
   if a.get(key):self.links.append(a[key])
 def handle_endtag(self,tag):
  if tag=='main':self.inside=False
 def handle_data(self,s):
  if self.inside:self.words.append(s)
def normalized(page):
 s=' '.join(' '.join(page.words).split())
 s=re.sub(r'Published on \d{4}-\d{2}-\d{2} [\d:]+ IST','DATE',s)
 s=re.sub(r'Published \w+ \d+, \d{4}','DATE',s)
 s=re.sub(r'last modified \d{4}-\d{2}-\d{2} [\d:]+ IST\.', 'UPDATED',s)
 return re.sub(r'Updated \w+ \d+, \d{4}','UPDATED',s)
def missing(page):
 result=set()
 for link in page.links:
  u=urlsplit(link)
  if u.scheme or u.netloc or not u.path.startswith('/'):continue
  target=ROOT/unquote(u.path).lstrip('/')
  if target.is_dir():target=target/'index.html'
  if not target.exists():result.add(link)
 return result
if __name__=='__main__':
 manifest=json.loads((ROOT/'site-source/preservation.json').read_text()); errors=[];known=[]
 for path in manifest['original_paths']:
  if not (ROOT/path).is_file(): errors.append('Removed file: '+path)
 for path,expected in manifest['unchanged'].items():
  if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=expected:errors.append('Changed protected asset/feed/redirect: '+path)
 approved=json.loads((ROOT/'site-source/approved-content-changes.json').read_text()) if (ROOT/'site-source/approved-content-changes.json').exists() else {}
 pages=dict(manifest['pages'])
 for source in (ROOT/'site-source/pages').rglob('*.json'):
  path=source.relative_to(ROOT/'site-source/pages').with_suffix('.html').as_posix()
  if path not in pages:
   data=json.loads(source.read_text()); original=Page();original.feed('<main>'+data['content']+'</main>')
   pages[path]={'text':normalized(original),'missing':[]}
 for path,baseline in pages.items():
  p=Page();p.feed((ROOT/path).read_text())
  if normalized(p)!=approved.get(path,baseline)['text']:errors.append('Content changed: '+path)
  if p.mains!=1:errors.append('Expected one main: '+path)
  if len(p.ids)!=len(set(p.ids)):errors.append('Duplicate IDs: '+path)
  for link in missing(p):
   (known if link in baseline['missing'] else errors).append(path+': '+link)
  if 'Site built on:' in (ROOT/path).read_text():errors.append('Build timestamp: '+path)
 for p in ROOT.rglob('*.xml'):ET.parse(p)
 figures=ROOT/'site-source/thesis-figures.json'
 if figures.exists():
  for path,figure in json.loads(figures.read_text())['originals'].items():
   if not (ROOT/path).exists() or hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=figure['sha256']:errors.append('Changed scientific source figure: '+path)
 print(f"Checked {len(pages)} pages, {len(manifest['original_paths'])} original paths, {len(manifest['unchanged'])} protected files.")
 print('Errors:',len(errors));print('\n'.join(errors))
 print('Pre-existing missing paths:',len(known));print('\n'.join(known))
 raise SystemExit(bool(errors))
