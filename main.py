import config
import oj
import ojjudger
import time


def main():
    ojclient = oj.OJClient(config.ojconfig)
    if(ojclient.Verify()):
        while True:
            _task = ojclient.GetTask()
            if(_task["status"] == "success"):
                print("Judger Running...")
                judger = ojjudger.Judger(ojclient, int(_task["sid"]), int(_task["pid"]), int(_task["lang"]))
                judger.run()
            elif(_task["status"] == "idle"):
                print("Judger IDLE~")
            time.sleep(1)
        return 0
    else:
        print("Failed to verify APIKey")
    return 0

main()
