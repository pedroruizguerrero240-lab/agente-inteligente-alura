import os
print("¿La llave está cargada?:", os.environ.get("GOOGLE_API_KEY") is not None)