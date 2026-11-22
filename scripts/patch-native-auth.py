#!/usr/bin/env python3
"""Patch the existing Salary Pro index.html without changing its UI/design."""
from pathlib import Path

p = Path("www/index.html")
if not p.exists():
    raise SystemExit("ERROR: www/index.html was not found. Run this from the repository root.")

s = p.read_text(encoding="utf-8")
old = "function getNativeFirebaseAuth(){if(!isNativeCapacitor())return null;if(!nativeFirebaseAuth&&typeof window.Capacitor.registerPlugin==='function')nativeFirebaseAuth=window.Capacitor.registerPlugin('FirebaseAuthentication');return nativeFirebaseAuth}"
new = "function getNativeFirebaseAuth(){if(!isNativeCapacitor())return null;return window.FirebaseAuthentication||null}"

if old in s:
    s = s.replace(old, new, 1)
elif new not in s:
    raise SystemExit("ERROR: Could not find the expected getNativeFirebaseAuth() code. No changes made.")

tag = '<script src="./native-auth.js"></script>'
if tag not in s:
    marker = "<script>\nconst DEFAULTS="
    if marker not in s:
        raise SystemExit("ERROR: Could not find the app's main inline script. No changes made.")
    s = s.replace(marker, tag + "\n" + marker, 1)

p.write_text(s, encoding="utf-8")
print("Patched www/index.html. Existing UI and other app code were preserved.")
