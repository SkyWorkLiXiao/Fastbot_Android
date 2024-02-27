import json
import unittest
from typing import Dict

import websocket
from websocket import create_connection, WebSocket


class TestVote(unittest.TestCase):
    ws = websocket.WebSocket()
    url = ('wss://work-test.singularity-ai.com/dialogue-aggregation/dialogue/aggregation/v2/agent?token=m-syp7koHueyFATYQOeRbL9IYuwq3GELwC80PKlcgts1hrcVYh8gFFo_LaQZCyRLuZgc2RTdAeBXCegW3s4oCPqZ0Cu-RIsMZYlEohecLCsDbc5jFpxulSL2oEo_lcnYsD8BIYty1OtZQzB6-XLRAHC04pa9F9N0OrrM0TxrkXE.cv0&device=Android')
    header = {'k_sso_token':'m-syp7koHueyFATYQOeRbL9IYuwq3GELwC80PKlcgts1hrcVYh8gFFo_LaQZCyRLuZgc2RTdAeBXCegW3s4oCPqZ0Cu-RIsMZYlEohecLCsDbc5jFpxulSL2oEo_lcnYsD8BIYty1OtZQzB6-XLRAHC04pa9F9N0OrrM0TxrkXE.cv0','device_id':'020b09d8-0ad4-465c-a8d2-af27cde0e602'}
    # header = [
    #     'k_sso_token: m-syp7koHueyFATYQOeRbL9IYuwq3GELwC80PKlcgts1hrcVYh8gFFo_LaQZCyRLuZgc2RTdAeBXCegW3s4oCPqZ0Cu-RIsMZYlEohecLCsDbc5jFpxulSL2oEo_lcnYsD8BIYty1OtZQzB6-XLRAHC04pa9F9N0OrrM0TxrkXE.cv0',
    #     'device_id: 020b09d8-0ad4-465c-a8d2-af27cde0e602']
    # @classmethod
    # def setUpClass(cls):
    #     # 前置方法
    #     websocket.enableTrace(True)  # 打开跟踪，查看日志
    #     # cls.ws = create_connection(cls.url,cls.header)  # 创建连接
    #     cls.ws.connect(cls.url,cls.header)
    #     cls.ws.settimeout(10)  # 设置超时时间
    def connect(self):
    # 前置方法
        websocket.enableTrace(True)  # 打开跟踪，查看日志
        # cls.ws = create_connection(cls.url,cls.header)  # 创建连接
        self.ws.connect(self.url,self.header)
        self.ws.settimeout(110)  # 设置超时时间
    # def test_connect_status(self):
    #     """测试连接状态"""
    #     # 断言连接状态
    #     self.assertEqual(101, self.ws.getstatus())

    def test_send_info(self):
        # 第一步：准备参数
        params = {"agent_id": "001", "agent_type": "universal","prompt": {"ask_from": "user", "content": "北京今日的天气", "copilot": False}}
        expected = {'status': "success"}
        # 第二步：发送请求
        self.ws.send(params)
        self.ws.settimeout(300)
        # 获取结果
        result = self.ws.recv()
        res = json.loads(result)
        # 第三步：断言：
        print("接收结果：", res)
        self.assertEqual(expected['status'], res['status'])

    @classmethod
    def tearDownClass(cls):
        cls.ws.close()


if __name__ == '__main__':
    unittest.main()
