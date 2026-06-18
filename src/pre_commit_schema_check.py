#!/usr/bin/env python3
import os
import re
import sys

def check_file(file_path):
    errors = []
    warnings = []
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        lines = content.splitlines()

    seen_urls = set()
    
    for line_num, line in enumerate(lines, 1):
        # 1. Check section titles (H2-H6) for Emojis, Special Characters, and Ampersands (Mandate 32)
        if line.startswith("#"):
            header_level = len(line) - len(line.lstrip('#'))
            if 2 <= header_level <= 6:
                title_text = line.lstrip('#').strip()
                # Check for ampersand
                if "&" in title_text:
                    errors.append(f"Line {line_num}: Title contains ampersand '&': '{title_text}' (replace with 'and')")
                
                # Check for emojis or special characters
                for char in title_text:
                    # Allow alphanumeric, spaces, hyphens, colons, parentheses, commas, periods, quotes
                    if ord(char) > 0x2000 and ord(char) not in (0x2013, 0x2014, 0x2018, 0x2019, 0x201c, 0x201d):
                        errors.append(f"Line {line_num}: Title contains emojis or special characters: '{char}' in '{title_text}'")
        
        # 2. Check for Markdown link rules (Mandate 33)
        # Match [ Link ](URL) - space at start or end of brackets
        if re.search(r'\[\s+[^\]]*\]\(', line) or re.search(r'\[[^\]]*\s+\]\(', line):
            errors.append(f"Line {line_num}: Link text contains leading or trailing spaces inside brackets: '{line.strip()}'")
            
        # 3. Extract and validate URLs
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', line)
        for link_text, url in links:
            url = url.strip()
            if url.startswith("http://") or url.startswith("https://"):
                if url.startswith("https:/") and not url.startswith("https://"):
                    errors.append(f"Line {line_num}: Corrupted protocol prefix: '{url}'")
                elif url.startswith("http:/") and not url.startswith("http://"):
                    errors.append(f"Line {line_num}: Corrupted protocol prefix: '{url}'")
                    
                # Check for duplicates in this category file
                if os.path.basename(file_path) not in ["index.md", "about.md"]:
                    # Normalize URL to check duplicate
                    clean_url = url.split("?")[0].split("#")[0].lower().rstrip('/')
                    if clean_url in seen_urls:
                        # Report as warning rather than blocking error
                        warnings.append(f"Line {line_num}: Duplicate URL found in this file: '{url}'")
                    else:
                        seen_urls.add(clean_url)
            
            # Check year tag if present
            match_year = re.search(r'\*\*\(([0-9]{4})\)\*\*', line)
            if match_year:
                year = int(match_year.group(1))
                if not (1990 <= year <= 2030):
                    errors.append(f"Line {line_num}: Year tag '{year}' is outside reasonable bounds: '{line.strip()}'")

    # Global multi-line check for link text line breaks
    if re.search(r'\[[^\]]*\n[^\]]*\]\(', content):
        errors.append("Global: Found a link with a line break inside the link text brackets.")

    return errors, warnings

def main():
    docs_dir = "docs"
    if not os.path.exists(docs_dir):
        print(f"Directory {docs_dir} not found.")
        sys.exit(0)

    total_errors = 0
    total_warnings = 0
    
    for root, dirs, files in os.walk(docs_dir):
        if "images" in root or "static" in root:
            continue
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                errors, warnings = check_file(path)
                if errors:
                    print(f"❌ {path}:")
                    for err in errors:
                        print(f"  {err}")
                    total_errors += len(errors)
                if warnings:
                    # By default do not flood output with duplicate warnings unless verbose
                    if "--verbose" in sys.argv:
                        print(f"⚠️ {path}:")
                        for warn in warnings:
                            print(f"  {warn}")
                    total_warnings += len(warnings)

    print(f"\nScan complete: Found {total_errors} errors and {total_warnings} warnings in markdown files.")
    if total_errors > 0:
        sys.exit(1)
    else:
        print("All Markdown files passed the schema check successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
