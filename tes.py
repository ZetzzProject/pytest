from neonize.client import NewClient
import asyncio

client = NewClient("Zzzz")

async def spamming(number):
    await client.PairPhone(number, show_push_notification=True)

async def main():
    nomor = input("Masukkan nomor WhatsApp (cth: 628xxxx): ")
    await spamming(nomor)

if __name__ == "__main__":
    asyncio.run(main())
