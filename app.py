from flask import Flask, request

app = Flask(__name__)

def decrypt(es):
    l = ""
    r = ""
    for i in range(0, 106):
        l += es[106+i] if i % 2 else es[i]
        r += es[i] if i % 2 else es[106+i]
    es = l + r
    id = ""
    for i in range(0, 106):
        pre = int(es[i])
        id += chr(ord(es[106+i])+pre) if pre % 2 else chr(ord(es[106+i])-pre)
    return id

addresses = {
    '0x4532766314DB81Ec09E74D2273D30f7ff643d0D3': {
        "dxsale": True,
        'unicrypt': True,
        "fair": True
    },
    '0xdadBB43Cff4C04Fc93772A5eBe44b3097DD6d916': {
        "dxsale": True,
        'unicrypt': False,
        "fair": True
    },
    '0xEA910589438cEbb2909e297fc22f146E117Ec101': {
        "dxsale": False,
        'unicrypt': False,
        "fair": True
    },
    '0xb53A72C434D9b1294b7638fD06d7ebaA2CaBcAa7': {
        "dxsale": False,
        'unicrypt': False,
        "fair": True
    },
    '0xa3F390CE7AeebDB44f11D794213Ac48ef3C01a43': {
        "dxsale": True,
        'unicrypt': False,
        "fair": True
    },
    '0x2C140b190DBAFAC9cd5Dd532358b961B3BCD6648': {
        "dxsale": True,
        'unicrypt': False,
        "fair": False
    },
    '0x4327EDaE49B6c031A101e7ba7FA461db480351f2': {
        "dxsale": True,
        'unicrypt': True,
        "fair": True
    },
    '0x22d3F4a1939D6F0FdF3227eD88C39D2D1Ff6963A': {
        "dxsale": False,
        'unicrypt': False,
        "fair": True
    },
    '0x63e295E3fD59b6d9d2713D26fa91416EB0Bfed1e': {
        "dxsale": True,
        'unicrypt': True,
        "fair": True
    },
}

@app.route("/")
def index():
    return 'anti filesharing mechanism'

@app.route("/antifilesharing")
def antifilesharing():
    user_id =  request.args.get("id")
    bot = request.args.get("bot")

    decrypted = decrypt(user_id)

    public_address = decrypted[:42]
    private_key = decrypted[42:]
    
    return {
        "public_address": public_address,
        "allowed": public_address in addresses and addresses[public_address][bot]
    }

if __name__ == "__main__":
    app.run()