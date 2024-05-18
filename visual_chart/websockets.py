import websocket
import time


####### WebSocketによるPUSH配信受信プログラム
def on_message(ws, message):
    pass


def disconnect(ws):
    ws.keep_running = False
    ws.close()


def on_error(ws, error):
    print('--- ERROR --- ')
    print(error)
    disconnect(ws)


def on_close(ws):
    ws.closed = on_close
    print('--- DISCONNECTED --- ')


# 最初の20分間で現在値が取得できなかった場合はエラーを表示して終了
# 20分より後に現在値が取得できなかった場合は5秒待って再度試行
# 現在値を始値として取得→60秒間で0.5秒ごとに高値・安値チェック→現在値を終値として取得→条件が合えば発注→１４分後決済
# 14分間の保有期間に休場して現在値が取得できない場合、保有したまま60秒おきに再度試行し、開場中に合計で１４分保有したら決済する
# 成り行き発注案：datetimeで現在の時分をintで取得し、日中/夜間の判定を行い、日通しではなく、それにより分岐して発注する
def on_open(ws):
    print('--- OPEN ---')
    time.sleep(10)
    print('--- CLOSE ---')
    disconnect(ws)


def websocket_entry():
    url = f'ws://localhost:8080/websocket'
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(url,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.run_forever()

    print('--- ENTRY ---')
    time.sleep(10)
    print('--- CLOSE ---')
    disconnect(ws)
