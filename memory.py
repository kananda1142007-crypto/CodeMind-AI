
import asyncio
from concurrent.futures import ThreadPoolExecutor
from hindsight_client import Hindsight

BANK_ID = "codemind-ai"
BASE_URL = "http://127.0.0.1:8888"

def run_async(coro):
    with ThreadPoolExecutor(max_workers=1) as executor:
        return executor.submit(asyncio.run, coro).result()

def save_memory(content):
    async def operation():
        client = Hindsight(base_url=BASE_URL)
        try:
            await client.aretain(
                bank_id=BANK_ID,
                content=content
            )
            return "Memory saved successfully!"
        finally:
            await client.aclose()

    return run_async(operation())

def recall_memory(query):
    async def operation():
        client = Hindsight(base_url=BASE_URL)
        try:
            result = await client.arecall(
                bank_id=BANK_ID,
                query=query
            )
            return [item.text for item in result.results]
        finally:
            await client.aclose()

    return run_async(operation())
