from libp2p import new_node
from libp2p.peer.peerinfo import info_from_p2p_addr
from multiaddr import Multiaddr
import asyncio

class PeerDiscovery:
    def __init__(self):
        self.host = None
        self.loop = asyncio.get_event_loop()

    async def setup(self):
        # Create a new libp2p node
        self.host = await new_node(transport_opt=["/ip4/0.0.0.0/tcp/0"])

        # Get multiaddress for this node
        multiaddrs = self.host.get_addrs()
        print(f"I am {self.host.get_id().pretty()} listening on {multiaddrs}")

        # Set up stream handler for peer discovery
        self.host.set_stream_handler("/openjob/discovery/1.0.0", self.discovery_handler)

    async def discovery_handler(self, stream):
        peer_id = stream.muxed_conn.peer_id
        print(f"Discovery request from {peer_id}")

        # Reply with our peer ID and addresses
        message = f"{self.host.get_id().pretty()}@{self.host.get_addrs()}"
        await stream.write(message.encode('utf-8'))

    async def discover_peer(self, peer_addr: str, peer_id: str):
        maddr = Multiaddr(peer_addr)
        info = info_from_p2p_addr(maddr)
        await self.host.connect(info)

        stream = await self.host.new_stream(info.peer_id, ["/openjob/discovery/1.0.0"])
        read_bytes = await stream.read()
        print(f"Discovery reply: {read_bytes.decode('utf-8')}")

    async def start(self):
        await self.setup()
        # Simulate connecting to another peer for discovery
        # Replace the address and ID below with those of an actual peer
        await self.discover_peer("/ip4/127.0.0.1/tcp/12345", "QmPeerID12345")

if __name__ == "__main__":
    discovery_node = PeerDiscovery()
    asyncio.get_event_loop().run_until_complete(discovery_node.start())
