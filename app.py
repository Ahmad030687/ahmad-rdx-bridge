import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import logging

# Logging taake Render logs mein details nazar aayein
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# --- AAPKA UPDATED COOKIE STRING (HARDCODED) ---
# Maine aapke JSON ko standard format mein convert kar diya hai
MY_COOKIE = (
    "_gcl_au=1.1.378371578.1770294559; _ga=GA1.1.44598217.1770294562; "
    "__Secure-BUCKET=CLgH; HSID=AX-zetFyNV00ue4Zj; SSID=ASZhYGIDDxe6FAXFO; "
    "APISID=TXAuWqcLxVqM9gsy/AZfSZ1RADQjbS_qqc; SAPISID=jfGEetuq2LhNFL1O/AFLTbRz0sk_Vmtg7Z; "
    "__Secure-1PAPISID=jfGEetuq2LhNFL1O/AFLTbRz0sk_Vmtg7Z; __Secure-3PAPISID=jfGEetuq2LhNFL1O/AFLTbRz0sk_Vmtg7Z; "
    "SEARCH_SAMESITE=CgQIiaAB; AEC=AaJma5uiFUJWXZiWig8lNlwbEz5-n1yKvjgy7IEBQoZvjwXhGKwxZz9Z-g; "
    "NID=529=DO9W9POXo7TQJ0zInxy4nGPDQRnN2l488gJmQUd1lCbDU5ItKHcf-AbHyy4rW7B7bqQceJ2e-IsHWs82dP9WRZLdxyUGQ6xvy0_GtiiBPRgPpe-Yv6MWKxw5DrjtxHILAL6n6MXSI-2CXHCgak_aEguKbJCd1tE4tHnXZ8MDHomh3gg-Lm9qkaj8Pmlla5EAXahnu2t6g1g79W6md6ka51s2bUw_Hr7zorZztiFlqJdfvY7JBoiJ3RN8IydjWv01TMhgfRSWzPbX8EXfBzSYFItdLWOq1V8LwdLjHn9xIRWD3Ete4FzrAQGKfiA9iyHVKWw3HofjV99828sFX0jUUD4dLGdff7Qb42pdpiCh9BYFqsCJV7ge0cJWaWcWxtB5kVYUqhewxGuccgH8tw7QoyIvGkcrafUFQWS_NKyuwn_M_ZpgcMpi7EXEpYs9Jxm_5-HACVbk_bBXe7TccI49OnE9agy8fDO17lVfLmMDcLjQxS6uYCXmjWrBq9_pZtv4BGe0P1mZfwd0MJpSWZXJlDWy2KJCV9E8O8Qrs_mriiOhl4BiiWTTgamG5NMky3TVJZOAdcoZwMucVjDXB0uCE9wb_fHH6-w6AR5pGhOFCHR64s6xt3S-n8qE3wFSkpAaLDNrJfMgZuupRzwUuPVGilFHQhqA0TErqflc-DvOsHkmMgtunp4_MEwhLl3HgVxtefAfdmwTpO8RykNC_r29HOfs; "
    "SID=g.a0007giwL-r3JvrPOlDUTy7Zgp454GJHwUXp9aD8Y09lTCNYVg8Wf1dYaQFntAcmLy7JYh5gnwACgYKAaMSARMSFQHGX2Mi73x54vdinMkxbSlBdyswchoVAUF8yKplpuzW17PZJ6gMiYtu9Jf40076; "
    "__Secure-1PSID=g.a0007giwL-r3JvrPOlDUTy7Zgp454GJHwUXp9aD8Y09lTCNYVg8WO10GMHljta2HjUUzb2vEDwACgYKAdgSARMSFQHGX2MiexwzUaF4XVPIiUWjUoMOfRoVAUF8yKpsgqbrTUNeDN9HFkBpKVvD0076; "
    "__Secure-3PSID=g.a0007giwL-r3JvrPOlDUTy7Zgp454GJHwUXp9aD8Y09lTCNYVg8WZxx7t4od28-QnBv8-qSDWgACgYKAZASARMSFQHGX2MiRECtCOw9dbcei0Ws7FBLbRoVAUF8yKpyBlki6iPRBb01Ve2PZ3ts0076; "
    "SIDCC=AKEyXzVBHSo9jneDqWNUBH4kgylFLEKIj5eoTr7xrfB1ggNh3wciLRdK6zScQOsWxfX9Um2lL-g; "
    "__Secure-1PSIDCC=AKEyXzXPHVvM3v6-Jl5D36-4FZ6I8cRCxTh8GIlYclHvhNOGT-PiYiZ-6qQlrrqOx-j9Mi4vuQ; "
    "__Secure-3PSIDCC=AKEyXzXlioTjDn4jb7v4U0qDdD235bL-tBuUzk_4GuZEPxDAZBms2ckzyDmaX6lOHbYXsnPmtlI"
)

class EditRequest(BaseModel):
    prompt: str
    image_url: str

@app.get("/")
async def home():
    return {"status": "Ahmad RDX Bridge is Active 🚀", "msg": "Final Cookie Loaded"}

@app.post("/edit")
async def edit_image(request: EditRequest):
    target_api = "https://anabot.my.id/api/ai/geminiOption"
    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            params = {
                "prompt": request.prompt,
                "type": "NanoBanana",
                "imageUrl": request.image_url,
                "cookie": MY_COOKIE,
                "apikey": "freeApikey"
            }
            logger.info(f"Sending request for: {request.prompt}")
            response = await client.get(target_api, params=params)
            
            if response.status_code != 200:
                logger.error(f"Error from engine: {response.text}")
                return {
                    "success": False, 
                    "error": f"Upstream Error {response.status_code}",
                    "details": response.text[:200]
                }
            
            return response.json()
    except Exception as e:
        logger.error(f"Bridge Exception: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
    
