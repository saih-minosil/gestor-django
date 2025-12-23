import uuid
namespace=uuid.NAMESPACE_X500

def generate_uuid():
    myuuid=uuid.uuid4()
    myuuidstring=str(myuuid)
    print(myuuidstring)
    return myuuidstring
