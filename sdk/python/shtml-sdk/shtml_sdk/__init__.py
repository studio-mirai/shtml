from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
DOWNLOADS_DIR = ROOT_DIR / "downloads"

DOWNLOADS_DIR.mkdir(exist_ok=True)

MIRAIFS_GATEWAY_HOSTNAME = "miraifs.sm.xyz"
PACKAGE_ID = "0xdae8d3692ee83d84eef0869c061825300dbd217f00c800580741dd9493190725"
