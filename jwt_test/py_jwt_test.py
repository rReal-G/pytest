import datetime
import json
from time import sleep
import jwt 
from jose import jws, jwe, constants

key = 'symmetric secret key'
algo = 'HS256'
object = {
    'payload': 'dataxx',
    'name': 'topG'
}
# encoded = jwt.encode(object, key, algo)
# print(encoded)

# decoded = jwt.decode(encoded, key, [algo])
# print(decoded)

# header = jwt.get_unverified_header(encoded)
# print(header)

# x = jwt.get_algorithm_by_name('HS256')
# print(x)

from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding

# Loading the Private Key
with open("private_key.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None  # Add your password here if the key is password-protected
    )

# Loading the Public Key
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read()
    )

public_bytes = public_key.public_bytes(
                               encoding=serialization.Encoding.PEM, 
                               format=serialization.PublicFormat.SubjectPublicKeyInfo
                               )
private_bytes = private_key.private_bytes(
                               encoding=serialization.Encoding.PEM, 
                               format=serialization.PrivateFormat.TraditionalOpenSSL, 
                               encryption_algorithm=serialization.NoEncryption()
                               )



# cipher = public_key.encrypt(b'top G never sleeps', padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None  # Can add labeling data if needed
#     ))
# print(cipher)

# plain = private_key.decrypt(
#     cipher,
#     padding.OAEP(
#         mgf=padding.MGF1(algorithm=hashes.SHA256()),
#         algorithm=hashes.SHA256(),
#         label=None 
#     )
# )
# print(plain)



# encoded_rs256 = jwt.encode(object, private_bytes, 'RS256',
#                            headers={'kid': 'lmao3333'})
# print(encoded_rs256)

# decoded_rs256 = jwt.decode(encoded_rs256, public_bytes, ['RS256'],
#                            )
# print(decoded_rs256)




# jwt_payload = jwt.encode(
#     {
#         "exp": datetime.datetime.now(tz=datetime.timezone.utc) \
#         + datetime.timedelta(seconds=2),
#         'iss': 'topG_issuer',
#         'aud': 'topG_audience'    
#     },
#     "secret",
# )
# # sleep(3)
# z = jwt.decode(jwt_payload, "secret", 
#                leeway=2, algorithms=["HS256"],
#                audience='topG_audience',
#                issuer='topG_issuer')
# print(z)



# signed = jws.sign({'a': 'b'}, 'secret', algorithm='HS256')
# print(signed)
# decoded = jwt.decode(signed, 'secret', ['HS256'])
# print(decoded)




with open('aes_192_key.bin', 'rb') as file:
    aes_192_bin = file.read()

payload = json.dumps({"some_data": "This is confidential"})  
jwe_token = jwe.encrypt(
    payload,
    #public_bytes,  # Recipient's public key for encryption
    aes_192_bin, # key wrap with same symmetrix key
    encryption=constants.ALGORITHMS.A128CBC_HS256, # enc can be whatever
    algorithm=constants.ALGORITHMS.A192KW, #alg must follow the key
    kid='lmaohehe'
)
jwe_string = jwe_token.decode()
print(jwe_string)

decrypted_payload = jwe.decrypt(
    jwe_string, 
    # private_bytes
    aes_192_bin # key wrap with same symmetrix key
    )
if decrypted_payload:
    data = json.loads(decrypted_payload.decode()) 
    print("Decrypted Payload:", data) 