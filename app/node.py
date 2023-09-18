from libp2p import new_node
from libp2p.peer.peerinfo import info_from_p2p_addr
from libp2p.peer.id import ID
from multiaddr import Multiaddr
import asyncio

class P2PNode:
    def __init__(self):
        self.host = None
        self.loop = asyncio.get_event_loop()

    async def setup(self):
        # Create a new libp2p node
        self.host = await new_node(transport_opt=["/ip4/0.0.0.0/tcp/0"])

        # Get multiaddress for this node
        multiaddrs = self.host.get_addrs()
        print(f"I am {self.host.get_id().pretty()} listenning on {multiaddrs}")

        # Set up stream handling for when another node connects to us
        self.host.set_stream_handler("/openjob/1.0.0", self.stream_handler)

    async def stream_handler(self, stream):
        peer_id = stream.muxed_conn.peer_id
        print(f"Connected to {peer_id}")

        while True:
            read_bytes = await stream.read()
            if read_bytes is not None:
                print(f"Received message: {read_bytes.decode('utf-8')}")
            else:
                break

    async def connect_to_peer(self, peer_addr: str, peer_id: str):
        """
        Connects to a peer given its address and peer ID.
        """
        maddr = Multiaddr(peer_addr)
        info = info_from_p2p_addr(maddr)
        await self.host.connect(info)

    async def send_message(self, peer_id_str: str, message: str):
        """
        Sends a message to a connected peer.
        """
        peer_id = ID(peer_id_str)
        stream = await self.host.new_stream(peer_id, ["/openjob/1.0.0"])
        await stream.write(message.encode('utf-8'))

    async def start(self):
        await self.setup()
        await self.connect_to_peer("/ip4/127.0.0.1/tcp/12345", "QmPeerID12345")
        await self.send_message("QmPeerID12345", "Hello, World!")

if __name__ == "__main__":
    node = P2PNode()
    asyncio.get_event_loop().run_until_complete(node.start())
