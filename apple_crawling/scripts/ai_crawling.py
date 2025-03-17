import asyncio
import json

from crawl4ai import AsyncWebCrawler


async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(
            url="https://cellphones.com.vn/mobile/apple.html",
        )
        print(result.markdown)
        
        # Save the result to a JSON file
        with open("json/crawling_result.json", "w") as file:
            # Either use the json method to get serializable data
            json_data = result.json()  # Call the method to get JSON data
            json.dump(json_data, file)

if __name__ == "__main__":
    asyncio.run(main())