from server import Server
from config import vk_api_token, vk_group_id

server1 = Server(vk_api_token, vk_group_id, "BruhBot")

server1.start()
