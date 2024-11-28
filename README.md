# Pocketfulapi-Python Library

Pocketfulapi-python is a Python library designed for traders and investors who want to streamline their workflow by automating or programmatically handling their trading activities on Pocketful. This library offers all the methods required for interacting with the trading APIs, and includes various features such as placing orders, fetching market data, and perform various other tasks crucial for managing a stock portfolio.


## Features
1. Place Orders: Easily place buy and sell orders for different instruments.
2. Fetch Holdings: Retrieve current holdings in the portfolio.
3. Fetch Positions: Get an overview of positions.
4. Check Funds: Check the available balance in your trading account.
5. Websockets: Fetch real-time data for different instruments


## Installation
You can clone the repository using the below commands, make sure you have python installed on your system to use this library.

```bash
git clone https://github.com/pocketful-tech/Pocketfulapi-python.git
cd Pocketfulapi-python
pip install -r requirements.txt
```

### Usage
Here’s a basic example of how to use the library, we have added this file in the repository:

```python
from PocketfulAPI.pocketful import Pocketful

clientId = "<clientId>"            # pocketful account Client Id
accessToken = "<accessToken>"    # generate your access token from "https://api.pocketful.in/login"


# Create an Instance of Pocketful class, with that instance you can call all the methods required for trading, see pocketful docs for detailed documentation
pocket=Pocketful(clientId, accessToken)

data=pocket.getProfile()
print(data)

# Comment and uncomment the code accordingly to understand all the methods properly

# data=pocket.getPendingOrder()
# print(data)

# data=pocket.getCompletedOrder()
# print(data)

# data=pocket.getTradeBook()
# print(data)

# data = pocket.getOrderHistory("<oms_order_id>")
# print(data)


# getDematHoldings=pocket.getDematHoldings()
# print(getDematHoldings)

# getPositionsNetwise=pocket.getPositionsNetwise()
# print(getPositionsNetwise)


# getPositionsDaywise=pocket.getPositionsDaywise()
# print(getPositionsDaywise)




# createBasket=pocket.createBasket({"login_id":clientId,"name":"pocketful001","type":"NORMAL","product_type":"ALL","order_type":"ALL"})
# print(createBasket)

# data = pocket.addInstrumentToBasket({
#         "basket_id": "eb3d2244-af73-4f05-a70b-a3518b4d321d",
#         "name": "pocketful001",
#         "order_info": {
#             "client_id": "<client id>",
#             "disclosedQuantity": 0,
#             "exchange": "NSE",
#             "execution_type": "REGULAR",
#             "instrument_token": 14366,
#             "order_side": "BUY",
#             "order_type": "MARKET",
#             "price": 0,
#             "product": "MIS",
#             "quantity": 1,
#             "series": "EQ",
#             "trading_symbol": "IDEA-EQ",
#             "trigger_price": 0,
#             "underlying_token": "14366",
#             "validity": "DAY",
#             "user_order_id": 10002
#         }
#      }
# )



# fetchBasket=pocket.fetchBasket()
# print(fetchBasket)

# renameBasket=pocket.renameBasket({"basket_id":"6bc753e5-b7d1-4ebb-94ac-36c751cedfbd","name":"yash"})
# print(renameBasket)

# deleteBasket=pocket.deleteBasket({"BasketId":"6bc753e5-b7d1-4ebb-94ac-36c751cedfbd","BasketName":"yash"})
# print(deleteBasket)

## !! Place Buy order
# placeOrder=pocket.placeOrder({
#     "exchange": "NSE",
#     "instrument_token": "14366",
#     "client_id": clientId,
#     "order_type": "MARKET",
#     "amo": True,
#     "price": 13,"quantity": 1,
#     "disclosed_quantity": 0,
#     "validity": "DAY",
#     "product": "CNC",
#     "order_side": "BUY",
#     "device": "WEB",
#     "user_order_id": 10002,
#     "trigger_price": 0,
#     "execution_type": "AMO"
#     })
# print(placeOrder)



# !! SELL order
# placeOrder=pocket.placeOrder({

#     "exchange": "NSE",
#     "instrument_token": "10666",
#     "client_id": "clintId",
#     "order_type": "MARKET",
#     "amo": False,
#     "price": 34.8,
#     "quantity": 1,
#     "disclosed_quantity": 0,
#     "validity": "DAY",
#     "product": "MIS",
#     "order_side": "SELL",
#     "device": "WEB",
#     "user_order_id": 10002,
#     "trigger_price": 0,
#     "execution_type": "REGULAR"

#     })
# print(placeOrder)


# # 



# # !! Condition BO  ordering

# conditional_order=pocket.placeConditionalOrder( {
#     "client_id": "clintId",
#     "device": "WEB",
#     "disclosed_quantity": 0,
#     "exchange": "NSE",
#     "execution_type": "CO",
#     "instrument_token": "10666",
#     "is_trailing": True,
#     "order_side": "BUY",
#     "order_type": "LIMIT",
#     "price": 77.9,
#     "product": "MIS",
#     "quantity": 1,
#     "square_off_value": 1,
#     "stop_loss_value": 1,
#     "trailing_stop_loss": "0.05",
#     "trigger_price": 0,
#     "user_order_id": 10002,
#     "validity": "DAY"
# })

# print(conditional_order)

# sellconditional_order=pocket.placeConditionalOrder( {
#     "client_id": "clintId",
#     "device": "WEB",
#     "disclosed_quantity": 0,
#     "exchange": "NSE",
#     "execution_type": "BO",
#     "instrument_token": "10666",
#     "is_trailing": True,
#     "order_side": "SELL",
#     "order_type": "LIMIT",
#     "price": 77.9,
#     "product": "MIS",
#     "quantity": 1,
#     "square_off_value": 1,
#     "stop_loss_value": 1,
#     "trailing_stop_loss": "0.05",
#     "trigger_price": 0,
#     "user_order_id": 10002,
#     "validity": "DAY"
# })

# print(sellconditional_order)


# modifyConditionalOrder=pocket.modifyConditionalOrder( {"exchange":"NSE","instrument_token":10666,"client_id":"","order_type":"LIMIT","price":80.9,"quantity":1,"disclosed_quantity":0,"validity":"DAY","product":"MIS","oms_order_id":"20231211-1762","exchange_order_id":"1200000019706097","filled_quantity":0,"remaining_quantity":1,"last_activity_reference":1386762580344098300,"trigger_price":0,"stop_loss_value":1,"square_off_value":"2","trailing_stop_loss":0,"is_trailing":False,"execution_type":"BO"})

# print(modifyConditionalOrder)


# cancelConditionalOrder=pocket.cancelConditionalOrder({"oms_order_id":"20231211-1897","execution_type":"BO","exchange_order_id":"1200000022379287","leg_order_indicator":"ENTRY","status":"MODIFY_CONFIRMED","client_id":clientId})
# print(cancelConditionalOrder)



# data=pocket.getFunds()
# print(data)


# data=pocket.getMarketdata("NFO","45835")   
# print(data)

# data=pocket.getFNOdata("NFO","45835")   
# print(data)


# ltp=pocket.getLtp("BFO",845835)
# print("ltp ",ltp)

# ltp=pocket.getLtp("NSE","45827")
# print("ltp ",ltp)


# data=pocket.getMarketdata("NSE","3045") 
# print(data)

# data=pocket.getClosePrice("NSE","3045")
# print(data)

# data=pocket.getOptionChain(3045,6,data["data"])
# print(data)





# ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< WebSocket >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# from PocketfulAPI.pacefinwebsocket import PocketfulSocket
# import time


# client_id = "<client_id>"
# access_token = "<access_Token>"

# conn = PocketfulSocket(client_id,access_token)

# ws_status = conn.run_socket()


# exchange_code = {
#     "NSE" : 1,
#     "NFO" : 2,
#     "CDS" : 3,
#     "MCX" : 4,
#     "BSE" : 6,
#     "BFO" : 7
# }


# marketdata_payload= {'exchangeCode': 4, 'instrumentToken': 428177}
# conn.subscribe_detailed_marketdata(marketdata_payload)

# snapquotedata_payload = {'exchangeCode': 1, 'instrumentToken': 3045}
# conn.subscribe_snapquote_data(snapquotedata_payload,)


# # For subscribe Multiple token 
# # For subscribe Multiple token 
# conn.subscribe_multiple_detailed_marketdata(
#         [

#             {'exchangeCode': 2, 'instrumentToken': 35648},
#             {'exchangeCode': 2, 'instrumentToken': 35649},
#             {'exchangeCode': 2, 'instrumentToken': 35650},
#             {'exchangeCode': 2, 'instrumentToken': 35651},


#         ]
#     )



# i =0
# while True:
#     time.sleep(1)
#     detailed_market_data = conn.read_detailed_marketdata()
#     print("detailed_market_data ", detailed_market_data)

    

#     # print("multiple channels subscribed ....")

#     detailed_market_data = conn.read_multiple_detailed_marketdata()
#     print( detailed_market_data )


#     # snapquote_data = conn.read_snapquote_data()
#     # print(detailed_market_data)
#     i = i + 1
#     print("==================================")
#     if i > 5:
#         print("unsubscribe marketdata")
#         conn.unsubscribe_detailed_marketdata(marketdata_payload)
#         print("unsubscribe snapquote")
#         conn.unsubscribe_detailed_marketdata(snapquotedata_payload)

```

