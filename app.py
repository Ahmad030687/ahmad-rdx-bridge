from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import gunicorn
import os

app = FastAPI()

# Aapka Hardcoded Cookie
MY_COOKIE = "AEC=AVh_V2iyBHpOrwnn7CeXoAiedfWn9aarNoKT20Br2UX9Td9K-RAeS_o7Sg; HSID=Ao0szVfkYnMchTVfk; SSID=AGahZP8H4ni4UpnFV; APISID=SD-Q2DJLGdmZcxlA/AS8N0Gkp_b9sJC84f; SAPISID=9BY2tOwgEz4dK4dY/Acpw5_--fM7PV-aw4; __Secure-1PAPISID=9BY2tOwgEz4dK4dY/Acpw5_--fM7PV-aw4; __Secure-3PAPISID=9BY2tOwgEz4dK4dY/Acpw5_--fM7PV-aw4; SEARCH_SAMESITE=CgQI354B; SID=g.a0002wiVPDeqp9Z41WGZdsMDSNVWFaxa7cmenLYb7jwJzpe0kW3bZzx09pPfc201wUcRVKfh-wACgYKAXUSARMSFQHGX2MiU_dnPuMOs-717cJlLCeWOBoVAUF8yKpYTllPAbVgYQ0Mr_GyeXxV0076; __Secure-1PSID=g.a0002wiVPDeqp9Z41WGZdsMDSNVWFaxa7cmenLYb7jwJzpe0kW3b_Pt9L1eqcIAVeh7ZdRBOXgACgYKAYESARMSFQHGX2MicAK_Acu_-NCkzEz2wjCHmxoVAUF8yKp9xk8gQ82f-Ob76ysTXojB0076; __Secure-3PSID=g.a0002wiVPDeqp9Z41WGZdsMDSNVWFaxa7cmenLYb7jwJzpe0kW3bUudZTunPKtKbLRSoGKl1dAACgYKAYISARMSFQHGX2MimdzCEq63UmiyGU-3eyZx9RoVAUF8yKrc4ycLY7LGaJUyDXk_7u7M0076"

class EditRequest(BaseModel):
    prompt: str
    image_url: str

@app.get("/")
def home():
    return {"status": "Ahmad RDX Bridge is Active", "version": "1.0.0"}

@app.post("/edit")
async def edit_image(request: EditRequest):
    headers = {
        "Cookie": MY_COOKIE,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Content-Type": "application/json"
    }
    
    # Ye NanoBanana (Gemini) ka proxy logic hai
    # Note: Backend par hum stable gateway use karenge jo aapka cookie process kare
    proxy_api = "https://anabot.my.id/api/ai/geminiOption" # Bridge fallback logic
    
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
            data = response.json()
            
            if data.get("success"):
                return {"success": True, "image_url": data["data"]["result"]["url"]}
            else:
                raise HTTPException(status_code=500, detail="Gemini failed to process.")
                
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
  
