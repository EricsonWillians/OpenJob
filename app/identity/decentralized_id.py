from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend

class DecentralizedID:
    def __init__(self):
        self.public_key = None
        self.private_key = None

    def generate_keys(self):
        # Generate RSA private/public key pair
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        
        self.public_key = self.private_key.public_key()

    def get_public_key_pem(self):
        if not self.public_key:
            raise Exception("Keys not generated yet")
        
        # Serialize the public key to PEM format
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return pem.decode('utf-8')

    def get_private_key_pem(self):
        if not self.private_key:
            raise Exception("Keys not generated yet")
        
        # Serialize the private key to PEM format
        pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        return pem.decode('utf-8')

    def get_decentralized_id(self):
        # Simple method to generate a DID based on public key (this is just an example)
        # In practice, you'd probably use a more complex method for generating DIDs
        return "did:example:" + self.get_public_key_pem().replace("\n", "")[:15]

if __name__ == "__main__":
    my_did = DecentralizedID()
    my_did.generate_keys()
    
    print(f"Public Key: {my_did.get_public_key_pem()}")
    print(f"Private Key: {my_did.get_private_key_pem()}")
    print(f"Decentralized ID: {my_did.get_decentralized_id()}")
