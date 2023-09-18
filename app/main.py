import asyncio
from peer_discovery import PeerDiscovery

async def main():
    # Initialize the PeerDiscovery object
    discovery_node = PeerDiscovery()
    
    # Run the peer discovery mechanism
    await discovery_node.start()

if __name__ == "__main__":
    # Run the main coroutine
    asyncio.run(main())
    