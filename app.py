from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import logging

# Logging enable taake Render logs mein error nazar aaye
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# AAPKA PROVIDED COOKIE (Hardcoded)
MY_COOKIE = "AEC=AVh_V2iyBHpOrwnn7CeXoAiedfWn9aarNoKT20Br2UX9Td9K-RAeS_o7Sg; HSID=Ao0szVfkYnMchTVfk; SSID=AGahZP8H4ni4UpnFV; APISID=SD-Q2DJLGdmZcxlA/AS8N0Gkp_b9sJC84f; SAPISID=9BY2tOwgEz4dK4dY/Acpw5_--fM7PV-aw4; __Secure-1PAPISID=9BY2tOwgEz4dK4dY/Acpw5_--fM7PV-aw4; __Secure-3PAPISID=9BY2tOwgEz4dK4dY/Acpw5_--fM7PV-aw4; SEARCH_SAMESITE=CgQI354B; SID=g.a0002wiVPDeqp9Z41WGZdsMDSNVWFaxa7cmenLYb7jwJzpe0kW3bZzx09pPfc201wUcRVKfh-wACgYKAXUSARMSFQHGX2MiU_dnPuMOs-717cJlLCeWOBoVAUF8yKpYTllPAbVgYQ0Mr_GyeXxV0076; __Secure-1PSID=g.a0002wiVPDeqp9Z41WGZdsMDSNVWFaxa7cmenLYb7jwJzpe0kW3b_Pt9L1eqcIAVeh7ZdRBOXgACgYKAYESARMSFQHGX2MicAK_Acu_-NCkzEz2wjCHmxoVAUF8yKp9xk8gQ82f-Ob76ysTXojB0076; __Secure-3PSID=g.a0002wiVPDeqp9Z41WGZdsMDSNVWFaxa7cmenLYb7jwJzpe0kW3bUudZTunPKtKbLRSoGKl1dAACgYKAYISARMSFQHGX2MimdzCEq63UmiyGU-3eyZx9RoVAUF8yKrc4ycLY7LGaJUyDXk_7u7M0076"

class EditRequest(BaseModel):
    prompt: str
    image_url: str

@app.get("/")
async def home():
    return {"status": "Ahmad RDX Bridge is Online 🚀", "mode": "Python Gunicorn"}

@app.post("/edit")
async def edit_image(request: EditRequest):
    logger.info(f"Processing prompt: {request.prompt}")
    
    # Bridge Gateway
    proxy_api = "https://anabot.my.id/api/ai/geminiOption"
    
    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            params = {
                "prompt": request.prompt,
                "type": "NanoBanana",
                "imageUrl": request.image_url,
                "cookie": MY_COOKIE,
                "apikey": "freeApikey"
            }
            response = await client.get(proxy_api, params=params)
            
            if response.status_code != 200:
                logger.error(f"Upstream Error: {response.text}")
                raise HTTPException(status_code=502, detail="Upstream API issue")
                
            data = response.json()
            if data.get("success"):
                return {"success": True, "image_url": data["data"]["result"]["url"]}
            else:
                return {"success": False, "error": "AI failed to generate image"}
                
    except Exception as e:
        logger.error(f"Server Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
        
