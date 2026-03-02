#!/usr/bin/env python3
"""TOC YAML Updater Script

This script updates the toc.yaml file to include newly generated FAQ entries.
It maintains the YAML structure and automatically sorts entries.
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("Error: pyyaml package not found. Run: pip install pyyaml")
    sys.exit(1)

TOC_FILE = Path('toc.yaml')
FAQ_DIR = Path('faq')

def get_generated_faqs():
    """Get list of newly generated FAQ files"""
    if FAQ_DIR.exists():
        return sorted([f.stem for f in FAQ_DIR.glob('*.md')])
    return []

def load_toc():
    """Load the toc.yaml file"""
    if not TOC_FILE.exists():
        print(f"Warning: {TOC_FILE} not found. Creating new toc structure.")
        return {'toc': {'entries': []}}
    
    try:
        with open(TOC_FILE, 'r') as f:
            data = yaml.safe_load(f)
        return data or {'toc': {'entries': []}}
    except Exception as e:
        print(f"Error loading toc.yaml: {e}")
        return {'toc': {'entries': []}}

def update_toc(toc_data, faq_name):
    """Add new FAQ entry to TOC"""
    if 'toc' not in toc_data:
        toc_data['toc'] = {'entries': []}
    
    if 'entries' not in toc_data['toc']:
        toc_data['toc']['entries'] = []
    
    entries = toc_data['toc']['entries']
    
    # Check if FAQ entry already exists
    for entry in entries:
        if isinstance(entry, dict) and entry.get('slug') == f'faq-{faq_name}':
            print(f'  (Already in TOC: {faq_name})')
            return toc_data
    
    # Add new FAQ entry
    new_entry = {
        'title': f'{faq_name.replace("-", " ").title()} FAQ',
        'slug': f'faq-{faq_name}',
        'path': f'/faq/{faq_name}.md',
        'category': 'FAQ'
    }
    
    entries.append(new_entry)
    entries.sort(key=lambda x: x.get('title', ''))
    
    return toc_data

def save_toc(toc_data):
    """Save updated toc.yaml file"""
    try:
        with open(TOC_FILE, 'w') as f:
            yaml.dump(toc_data, f, default_flow_style=False, sort_keys=False)
        return True
    except Exception as e:
        print(f"Error saving toc.yaml: {e}")
        return False

if __name__ == '__main__':
    print("Starting TOC update...")
    
    faqs = get_generated_faqs()
    if not faqs:
        print("No FAQ files found.")
        sys.exit(0)
    
    print(f"Found {len(faqs)} FAQ file(s).")
    
    toc = load_toc()
    
    for faq_name in faqs:
        print(f'  Adding: {faq_name}')
        toc = update_toc(toc, faq_name)
    
    if save_toc(toc):
        print("✓ TOC YAML updated successfully")
    else:
        print("✗ Failed to update TOC YAML")
        sys.exit(1)
