# from PocketfulAPI.pocketful import Pocketful
# import json

clientId = ""
access_token = ""


# pocket = Pocketful(clientId, access_token)

# response = pocket.getProfile()
# print(response)
# with open("demoresponse.json", "w") as f:
#     json.dump(response, f, indent=4) 

# data=pocket.getPendingOrder()
# print(data)

# data = pocket.getCompletedOrder()
# print(data)

# data = pocket.getTradeBook()
# print(data)

# data = pocket.getOrderHistory("<oms_order_id>")
# print(data)


# getDematHoldings = pocket.getDematHoldings()
# print(getDematHoldings)

# getPositionsNetwise = pocket.getPositionsNetwise()
# print(getPositionsNetwise)


# getPositionsDaywise = pocket.getPositionsDaywise()
# print(getPositionsDaywise)




# createBasket = pocket.createBasket({"login_id":clientId,"name":"pocketful002","type":"NORMAL","product_type":"ALL","order_type":"ALL"})
# print(createBasket)

# response = pocket.addInstrumentToBasket({
#         "basket_id": "eb3d2244-af73-4f05-a70b-a3518b4d321d",
#         "name": "pocketful001",
#         "order_info": {
#             "client_id": "client id",
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
# print(response)



# fetchBasket=pocket.fetchBasket()
# print(fetchBasket)
# with open("demoresponse.json", "w") as f:
#     json.dump(fetchBasket, f, indent=4) 


# renameBasket=pocket.renameBasket({"basket_id":"6bc753e5-b7d1-4ebb-94ac-36c751cedfbd","name":"yash"})
# print(renameBasket)

# deleteBasket=pocket.deleteBasket({"BasketId":"6bc753e5-b7d1-4ebb-94ac-36c751cedfbd","BasketName":"yash"})
# print(deleteBasket)

## !! Place Buy order
# placeOrder=pocket.placeOrder({
#     "exchange": "NSE",
#     "instrument_token": "13342",
#     "client_id": clientId,
#     "order_type": "MARKET",
#     "amo": True,
#     "price": 0,"quantity": 1,
#     "disclosed_quantity": 0,
#     "validity": "DAY",
#     "product": "CNC",
#     "order_side": "BUY",
#     "device": "WEB",
#     "user_order_id": 10002,
#     "trigger_price": 0,
#     "execution_type": "REGULAR"
#     })
# print(placeOrder)
# with open("demoresponse.json", "w") as f:
#     json.dump(placeOrder, f, indent=4)



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


# ltp=pocket.getLtp("NSE","45827")
# print("ltp ",ltp)


# data=pocket.getMarketdata("NSE","3045") 
# print(data)

# data=pocket.getClosePrice("NSE","3045")
# print(data)

# data=pocket.getOptionChain("instrument-token","numnber of options", "ltp")
# print(data)





# ## <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< WebSocket >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

"""
In the below example we have shown how a client can access live market feeds, you can use this live market feed for your strategies.
"""

# from PocketfulAPI.pocketfulwebsocket import PocketfulSocket
# import time

# clientId = ""
# access_token = ""

# conn = PocketfulSocket(clientId, access_token)

# ws_status = conn.run_socket()

# exchange_code = {
#     "NSE" : 1,
#     "NFO" : 2,
#     "CDS" : 3,
#     "MCX" : 4,
#     "BSE" : 6,
#     "BFO" : 7
# }


# marketdata_payload= {'exchangeCode': 1, 'instrumentToken': 14366}
# conn.subscribe_detailed_marketdata(marketdata_payload)

# i =0
# flag = 1
# while flag:
#     time.sleep(0.5)
#     detailed_market_data = conn.read_detailed_marketdata()
#     print("detailed_market_data -----", detailed_market_data)

#     i = i + 1
#     print("==================================")
#     if i > 5:
#         print("unsubscribed marketdata")
#         conn.unsubscribe_detailed_marketdata(marketdata_payload)
#         flag = 0
