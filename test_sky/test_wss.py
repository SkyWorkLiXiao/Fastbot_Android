import ssl
import websocket
import _thread as thread


class WebsocketClient(object):
    """docstring for WebsocketClient"""
    ws = websocket.WebSocket()
    def __init__(self, address, send_message,send_header):
        super(WebsocketClient, self).__init__()
        self.address = address
        self.header = send_header
        self.send_message = send_message
        self.recv = None

    def on_message(self, ws, message):
        self.recv = message
        print("on_client_message:", self.recv)

    def on_error(self, ws, error):
        print("### error:", error)

    def on_close(self, ws,send_header):
        self.header=send_header
        print("### closed ###")

    def on_open(self, ws):
        print("on open")

    def run(self,*args):
        self.ws.send(self.send_message)
        print(self.send_message)
        # self.ws.close()

    thread.start_new_thread(run, ())

    def get_message(self):
        return self.recv

    def run(self):
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp(self.address,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


if __name__ == '__main__':
    ws_client = WebsocketClient('wss://work-test.singularity-ai.com/dialogue-aggregation/dialogue/aggregation/v2/agent?token=m-syp7koHueyFATYQOeRbL9IYuwq3GELwC80PKlcgts1hrcVYh8gFFo_LaQZCyRLuZgc2RTdAeBXCegW3s4oCPqZ0Cu-RIsMZYlEohecLCsDbc5jFpxulSL2oEo_lcnYsD8BIYty1OtZQzB6-XLRAHC04pa9F9N0OrrM0TxrkXE.cv0&device=Android', {"agent_id": "001", "agent_type": "universal","prompt": {"ask_from": "user", "content": "北京今日的天气", "copilot": False}},{'k_sso_token':'m-syp7koHueyFATYQOeRbL9IYuwq3GELwC80PKlcgts1hrcVYh8gFFo_LaQZCyRLuZgc2RTdAeBXCegW3s4oCPqZ0Cu-RIsMZYlEohecLCsDbc5jFpxulSL2oEo_lcnYsD8BIYty1OtZQzB6-XLRAHC04pa9F9N0OrrM0TxrkXE.cv0','device_id':'020b09d8-0ad4-465c-a8d2-af27cde0e602'})
    ws_client.run()
    print(ws_client.get_message())
    # header={'k_sso_token':'m-syp7koHueyFATYQOeRbL9IYuwq3GELwC80PKlcgts1hrcVYh8gFFo_LaQZCyRLuZgc2RTdAeBXCegW3s4oCPqZ0Cu-RIsMZYlEohecLCsDbc5jFpxulSL2oEo_lcnYsD8BIYty1OtZQzB6-XLRAHC04pa9F9N0OrrM0TxrkXE.cv0','device_id':'020b09d8-0ad4-465c-a8d2-af27cde0e602'}
    com.singularity.tiangong / com.singularity.tiangong.MainActivity