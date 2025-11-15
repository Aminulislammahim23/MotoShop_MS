import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from api.api import MotoShopAPI

api = MotoShopAPI()
print(api.users)
print(api.inventory)
print(api.sales)
