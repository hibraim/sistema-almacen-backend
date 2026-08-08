import os
import uuid
from PIL import Image
from fastapi import UploadFile, HTTPException

UPLOAD_DIR = "static/uploads"
THUMB_DIR = "static/thumbnails"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(THUMB_DIR, exist_ok=True)

async def guardar_imagen_webp(file: UploadFile) -> dict:
    if file.content_type not in ["image/jpeg", "image/png", "image/webp"]:
        raise HTTPException(status_code=400, detail="Formato no permitido (Solo JPG, PNG o WebP)")
    
    filename = f"{uuid.uuid4().hex}.webp"
    main_path = os.path.join(UPLOAD_DIR, filename)
    thumb_path = os.path.join(THUMB_DIR, filename)
    
    try:
        image = Image.open(file.file)
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
            
        # Imagen Principal (Max 1000px)
        image.thumbnail((1000, 1000), Image.Resampling.LANCZOS)
        image.save(main_path, "WEBP", quality=80, optimize=True)
        
        # Miniatura (300px)
        thumb = image.copy()
        thumb.thumbnail((300, 300), Image.Resampling.LANCZOS)
        thumb.save(thumb_path, "WEBP", quality=70, optimize=True)
        
        return {
            "url_principal": f"/static/uploads/{filename}",
            "url_thumbnail": f"/static/thumbnails/{filename}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error procesando imagen: {str(e)}")
