import ssl

import anyio
from anyio.abc import SocketAttribute


async def main():
    # These two steps are only required for certificates that are not trusted by the
    # installed CA certificates on your machine, so you can skip this part if you use
    # a recognized certificate vendor
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    context.load_verify_locations(cafile='cert.pem')

    async with await anyio.connect_tcp('localhost', 1234, ssl_context=context) as client:
        print('Connected to', client.extra(SocketAttribute.remote_address))
        await client.send(b'Client\n')
        response = await client.receive()
        print(response)


anyio.run(main)
