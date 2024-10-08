import requests
import json
from threading import Thread 
from PocketfulAPI.wsclient import socket_connect, get_compact_marketdata, get_detailed_marketdata, get_snapquotedata, send_message, get_ws_connection_status, unsubscribe_update, get_order_update, get_trade_update, get_multiple_detailed_marketdata, get_multiple_compact_marketdata, get_multiple_snapquotedata
import sys
import time


class PocketfulSocket(object):
    base_url = "https://trade.pocketful.in"
    
    def __init__(self, client_id,access_token):
        self.headers = {'Content-type': 'application/json'}
        self.access_token = access_token
        self.login_id = ""
        self.base_url=self.base_url
        self.client_id = client_id
        url = ""
        if "https" in self.base_url:
            url = self.base_url.replace("https", "wss")
        else:
            url = self.base_url.replace("http", "ws")
        self.websocket_url = url



    def print_access_token(self):
        return self.access_token

    def set_access_token(self, access_token):
        self.access_token = access_token

    def get_request(self, url, params):
        headers = self.headers
        headers['Authorization'] = f'Bearer {self.access_token}'
        res = requests.get(f'{self.base_url}{url}' , params=params, headers=headers)
        return res.json()

    def post_request(self, url, data):
        headers = self.headers
        headers['Authorization'] = f'Bearer {self.access_token}'
        res = requests.post(f'{self.base_url}{url}', headers=headers, data=json.dumps(data))
        print(res)
        return res.json()

    def put_request(self, url, data):
        headers = self.headers
        headers['Authorization'] = f'Bearer {self.access_token}'
        res = requests.put(f'{self.base_url}{url}', headers=headers, data=json.dumps(data))
        print(res)
        return res.json()

    def delete_request(self, url, params):
        headers = self.headers
        headers['Authorization'] = f'Bearer {self.access_token}'
        res = requests.delete(f'{self.base_url}{url}' , params=params, headers=headers)
        return res.json()

    

    def run_socket(self):
        client_id = self.client_id
        access_token = self.access_token
        websocket_url = self.websocket_url
        print(websocket_url)
        th_websocket = Thread(target=socket_connect, args=(client_id, access_token, websocket_url,))
        th_websocket.start()
        counter = 0
        while True:
            status = get_ws_connection_status()
            if status == True:
                return True
            time.sleep(1)
            counter = counter + 1
            if counter > 5:
                return False


    def subscribe_detailed_marketdata(self, detailedmarketdata_payload):
        subscription_pkt = [[detailedmarketdata_payload['exchangeCode'], detailedmarketdata_payload['instrumentToken']]]
        th_detailed_marketdata = Thread(target=send_message, args=('DetailedMarketDataMessage', subscription_pkt))
        th_detailed_marketdata.start()

    def read_detailed_marketdata(self):
        data = get_detailed_marketdata()
        return data

    def unsubscribe_detailed_marketdata(self, detailedmarketdata_payload):
        unsubscription_pkt = [[detailedmarketdata_payload['exchangeCode'], detailedmarketdata_payload['instrumentToken']]]
        th_detailed_marketdata = Thread(target=unsubscribe_update, args=('DetailedMarketDataMessage', unsubscription_pkt))
        th_detailed_marketdata.start()


    def subscribe_compact_marketdata(self, compactmarketdata_payload):
        subscription_pkt = [[compactmarketdata_payload['exchangeCode'], compactmarketdata_payload['instrumentToken']]]
        th_compact_marketdata = Thread(target=send_message, args=('CompactMarketDataMessage', subscription_pkt))
        th_compact_marketdata.start()

    def unsubscribe_compact_marketdata(self, compactmarketdata_payload):
        unsubscription_pkt = [[compactmarketdata_payload['exchangeCode'], compactmarketdata_payload['instrumentToken']]]
        th_compact_marketdata = Thread(target=unsubscribe_update, args=('CompactMarketDataMessage', unsubscription_pkt))
        th_compact_marketdata.start()
    
    def read_compact_marketdata(self):
        data = get_compact_marketdata()
        return data

    def subscribe_snapquote_data(self, snapquotedata_payload):
        subscription_pkt = [[snapquotedata_payload['exchangeCode'], snapquotedata_payload['instrumentToken']]]
        th_snapquote = Thread(target=send_message, args=('SnapquoteDataMessage', subscription_pkt))
        th_snapquote.start()
    
    def unsubscribe_snapquote_data(self, snapquotedata_payload):
        unsubscription_pkt = [[snapquotedata_payload['exchangeCode'], snapquotedata_payload['instrumentToken']]]
        th_snapquote = Thread(target=unsubscribe_update, args=('SnapquoteDataMessage', unsubscription_pkt))
        th_snapquote.start()

    def read_snapquote_data(self):
        data = get_snapquotedata()
        return data

    def subscribe_order_update(self, orderupdate_payload):
        subscription_pkt = [orderupdate_payload['client_id'], "web"]
        th_order_update = Thread(target=send_message, args=('OrderUpdateMessage', subscription_pkt))
        th_order_update.start()
    
    def unsubscribe_order_update(self, orderupdate_payload):
        unsubscription_pkt = [orderupdate_payload['client_id'], "web"]
        th_order_update = Thread(target=unsubscribe_update, args=('OrderUpdateMessage', unsubscription_pkt))
        th_order_update.start()

    def read_order_update_data(self):
        data = get_order_update()
        return data
    




    def subscribe_trade_update(self, tradeupdate_payload):
        subscription_pkt = [tradeupdate_payload['client_id'], "web"]
        th_trade_update = Thread(target=send_message, args=('TradeUpdateMessage', subscription_pkt))
        th_trade_update.start()
    
    def unsubscribe_trade_update(self, tradeupdate_payload):
        unsubscription_pkt = [tradeupdate_payload['client_id'], "web"]
        th_trade_update = Thread(target=unsubscribe_update, args=('OrderUpdateMessage', unsubscription_pkt))
        th_trade_update.start()

    def read_trade_update_data(self):
        data = get_trade_update()
        return data











    def subscribe_multiple_detailed_marketdata(self, detailedmarketdata_payload):
        subscription_pkt = []
        for payload in detailedmarketdata_payload:
            pkt = [payload['exchangeCode'], payload['instrumentToken']]
            subscription_pkt.append(pkt)
        th_detailed_marketdata = Thread(target=send_message, args=('DetailedMarketDataMessage', subscription_pkt))
        th_detailed_marketdata.start()

    def unsubscribe_multiple_detailed_marketdata(self, detailedmarketdata_payload):
        unsubscription_pkt = []
        for payload in detailedmarketdata_payload:
            pkt = [payload['exchangeCode'], payload['instrumentToken']]
            unsubscription_pkt.append(pkt)
        th_detailed_marketdata = Thread(target=unsubscribe_update, args=('DetailedMarketDataMessage', unsubscription_pkt))
        th_detailed_marketdata.start()

    def read_multiple_detailed_marketdata(self):
        data = get_multiple_detailed_marketdata()
        return data

    def subscribe_multiple_compact_marketdata(self, compactmarketdata_payload):
        subscription_pkt = []
        for payload in compactmarketdata_payload:
            pkt = [payload['exchangeCode'], payload['instrumentToken']]
            subscription_pkt.append(pkt)
        th_compact_marketdata = Thread(target=send_message, args=('CompactMarketDataMessage', subscription_pkt))
        th_compact_marketdata.start()

    def unsubscribe_multiple_compact_marketdata(self, compactmarketdata_payload):
        unsubscription_pkt = []
        for payload in compactmarketdata_payload:
            pkt = [payload['exchangeCode'], payload['instrumentToken']]
            unsubscription_pkt.append(pkt)
        th_compact_marketdata = Thread(target=unsubscribe_update, args=('CompactMarketDataMessage', unsubscription_pkt))
        th_compact_marketdata.start()

    def read_multiple_compact_marketdata(self):
        data = get_multiple_compact_marketdata()
        return data

    def subscribe_multiple_snapquote_data(self, snapquotedata_payload):
        subscription_pkt = []
        for payload in snapquotedata_payload:
            pkt = [payload['exchangeCode'], payload['instrumentToken']]
            subscription_pkt.append(pkt)
        th_snapquotetdata = Thread(target=send_message, args=('SnapquoteDataMessage', subscription_pkt))
        th_snapquotetdata.start()

    def unsubscribe_multiple_snapquote_data(self, snapquotedata_payload):
        unsubscription_pkt = []
        for payload in snapquotedata_payload:
            pkt = [payload['exchangeCode'], payload['instrumentToken']]
            unsubscription_pkt.append(pkt)
        th_snapquotetdata = Thread(target=unsubscribe_update, args=('SnapquoteDataMessage', unsubscription_pkt))
        th_snapquotetdata.start()

    def read_multiple_snapquote_data(self):
        data = get_multiple_snapquotedata()
        return data


