from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure

import os
from dotenv import load_dotenv
load_dotenv()

USER = os.getenv('MONGO_USER')
PWD = os.getenv('MONGO_PWD')


'''
xác minh chứng chỉ SSL
tạm thời ở dev thêm vào url `&tlsAllowInvalidCertificates=true`
hoặc bỏ qua bằng cách thêm option: ssl_cert_reqs=ssl.CERT_NONE # Bỏ qua kiểm tra chứng chỉ
ở production cần Đảm bảo cập nhật chứng chỉ CA hợp lệ và kiểm tra lại cấu hình mạng
'''
uri = f"mongodb+srv://{USER}:{PWD}@davidapi.jhhu4ml.mongodb.net/?retryWrites=true&w=majority&appName=davidAPI&tlsAllowInvalidCertificates=true"

# Create a new client and connect to the server
conn = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    conn.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except ConnectionFailure as fail:
    print(fail)
except Exception as e:
    print(e)

client = conn