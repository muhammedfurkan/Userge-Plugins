# by krishna

import asyncio

from userge import userge, Message


@userge.on_cmd("bguy$", about={'header': "say anybody without patience ;-)"})
async def bguy_func(message: Message):
    animation_chars = [
        "WHY", "ARE", "YOU", "A", "BAD⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠", "BOY",
        "PLEASE", "KEEP", "QUITE", "BUDDY"
    ]
    for i in range(10):
        await asyncio.sleep(0.6)
        await message.edit(animation_chars[i])
