#!/usr/bin/env python3
"""Bob FAQ Generator Script

This script generates FAQ entries from markdown files using BOB API.
It detects new .md files from git diff and generates FAQ content.
"""

import os
import sys
import json
from pathlib import Path

try:
    import yaml
    import requests
except ImportError:
    print("Error: Required packages not found. Run: pip install pyyaml requests")
    sys.exit(1)

# Configuration from environment variables
BOB_API_URL = os.getenv('BOB_API_URL', 'http://localhost:8000')
BOB_API_KEY = os.getenv('BOB_API_KEY', '')
DOCS_DIR = Path('docs')
FAQ_DIR = Path('faq')

def get_new_files():
    """Get list of new .md files from git diff"""
    try:
        with open('new_files.txt', 'r') as f:
            files = [line.strip() for line in f if line.strip()]
        return files
    except FileNotFoundError:
        return []

def generate_faq_for_file(md_file):
    """Call BOB API to generate FAQ from markdown file"""
    try:
        with open(md_file, 'r') as f:
            content = f.read()
        
        payload = {
            'mode': 'powervs-faq-generator',
            'content': content,
            'source_file': str(md_file)
        }
        
        headers = {'Authorization': f'Bearer {BOB_API_KEY}'}
        
        response = requests.post(
            f'{BOB_API_URL}/api/v1/generate',
            json=payload,
            headers=headers,
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json().get('faq_content')
        else:
            print(f'Error generating FAQ for {md_file}: {response.text}')
            return None
    except Exception as e:
        print(f'Exception while generating FAQ: {str(e)}')
        return None

def save_faq_file(faq_name, faq_content):
    """Save FAQ content to file"""
    faq_file = FAQ_DIR / f'{faq_name}.md'
    FAQ_DIR.mkdir(exist_ok=True)
    
    with open(faq_file, 'w') as f:
        f.write(faq_content)
    
    return faq_file

if __name__ == '__main__':
    print("Starting FAQ generation...")
    files = get_new_files()
    
    if not files:
        print("No new files detected.")
        sys.exit(0)
    
    print(f"Found {len(files)} new file(s) to process.")
    
    for md_file in files:
        print(f'Processing: {md_file}')
        faq_content = generate_faq_for_file(md_file)
        
        if faq_content:
            faq_name = Path(md_file).stem
            save_faq_file(faq_name, faq_content)
            print(f'✓ Generated FAQ: {faq_name}')
        else:
            print(f'✗ Failed to generate FAQ for {md_file}')
    
    print("FAQ generation complete.")
