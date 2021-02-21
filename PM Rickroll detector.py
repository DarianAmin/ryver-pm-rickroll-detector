from asyncio import get_event_loop
from pyryver import Ryver
import pyryver
import asyncio
import requests
from pyryver.objects import Creator


creator = Creator(
    name="Rickroll Detector",
    avatar="https://m.media-amazon.com/images/M/MV5BOTIyODY1OTYtZjAzNS00ZGQ2LWFhNmItMTJkYTc0MDNkYTk0XkEyXkFqcGdeQXVyODg3NTgyODQ@._V1_UY100_CR39,0,100,100_AL_.jpg",
    )

async def main():
    async with Ryver("Org_Name", "Username", "Password") as ryver:
        await ryver.load_users()
        async with ryver.get_live_session() as session:

            @session.on_chat
            async def on_chat(msg):
                to_user = ryver.get_user(jid=msg.to_jid)
                from_user = ryver.get_user(jid=msg.from_jid)
                me= ryver.get_user(username="Username")
                if to_user:
                    if "http" in msg.text:
                        to_user = ryver.get_user(jid=msg.to_jid)
                        from_user = ryver.get_user(jid=msg.from_jid)
                
                        
                        url= msg.text
                        
                        headers = {'User-Agent': '<yourUserAgent>'}
                        #Keywords
                        keywords = ['Rick','Astley','Rick Astley - Never Gonna Give You Up (Video)','Official Rick Astley','Never gonna give you up','Never gonna let you down','Never gonna run around and desert you','Never gonna make you cry','Never gonna say goodbye','Never gonna tell a lie and hurt you','Stick Bugged','Get Stick Bugged Lol']
                        response = requests.get(url, headers=headers)

                        found_keywords = 0
                        #checks to see if the message contains any keywords
                        for el in keywords:
                            if el.lower() in str(response.content).lower():
                                #Output
                                await me.send_message("Looks like a troll link! This was from "+from_user.get_username(),creator)
                                break
                    
            await session.run_forever()


get_event_loop().run_until_complete(main())
