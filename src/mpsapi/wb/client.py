from datetime import date

import aiohttp


class WBClient:
    BASE_URL = "https://common-api.wildberries.ru"

    def __init__(self, api_key: str, session: aiohttp.ClientSession | None = None):
        self.api_key = api_key
        self.session = session or aiohttp.ClientSession(headers={"Authorization": self.api_key})

    async def get_seller_info(self):
        url = f"{self.BASE_URL}/api/v1/seller-info"
        params = {}
        async with self.session.get(url, params=params) as resp:
            resp.raise_for_status()
            data = await resp.json()
            return data

    async def get_news(self, dt: date = None):
        url = f"{self.BASE_URL}/api/communications/v2/news"
        dt = dt.isoformat() if dt else date.today().isoformat()
        params = {"from": dt}
        async with self.session.get(url, params=params) as resp:
            resp.raise_for_status()
            data = await resp.json()
            return data

    async def close(self):
        await self.session.close()
