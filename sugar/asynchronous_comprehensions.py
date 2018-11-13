import asyncio
async def ticker(delay, to):
    """Yield numbers from 0 to *to* every *delay* seconds."""
    for i in range(to):
        yield i
        await asyncio.sleep(delay)
async def main():
    mylist = []
    async for x in  ticker(1,10):
        print(mylist)
        mylist.append(x)
        
    print (mylist)
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())