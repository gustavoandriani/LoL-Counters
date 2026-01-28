# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['LOLCounters.py'],
    pathex=[],
    binaries=[],
    datas=[('icon.ico', '.'), ('data/lolcounters.json', 'data')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='LOLCounters',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,   # windowed
    icon='icon.ico'  # 👈 ÍCONE AQUI
)
