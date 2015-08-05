import http.client
import json

class OJClient:
    def __init__(self, config):
        self.config = config
    def getHost(self):
        return self.config["host"];
    def getAPI(self, apiName):
        return "%s/%s" % (self.config["requestpath"], apiName)
    def getPostAPI(self, apiName):
        return "%s/%s?apikey=%s" % (self.config["requestpath"], apiName, self.config["apikey"])
    def getHTTPConnection(self):
        return http.client.HTTPConnection(self.config["host"])

    def getHTTPRequest(self, conn, path, body):
        conn.request("POST", path, body)
        return conn.getresponse()

    def checkHTTPResponse(self, response):
        if(response.status != 200):
            print(response.status)
            print(response.reason)
            exit()

    def closeHTTPConnection(self, conn):
        conn.close()

    def getJSONRequest(self, path, postdata):
        conn = self.getHTTPConnection()
        resp = self.getHTTPRequest(conn, path, postdata)
        self.checkHTTPResponse(resp)
        __data = resp.read()
        self.closeHTTPConnection(conn)
        return json.loads(bytes.decode(__data))

    def getTextRequest(self, path, postdata):
        conn = self.getHTTPConnection()
        resp = self.getHTTPRequest(conn, path, postdata)
        self.checkHTTPResponse(resp)
        __data = resp.read()
        self.closeHTTPConnection(conn)
        return __data

    def Verify(self):
        APIKey = self.config["apikey"]
        path = self.getAPI("verify")
        __data = self.getJSONRequest(path, str.encode(json.dumps({
            "apikey" : APIKey
        })));
        return __data["status"] == "success"

    def GetTask(self):
        APIKey = self.config["apikey"]
        path = self.getPostAPI("task")
        __data = self.getJSONRequest(path, str.encode(json.dumps({
            "type" : "get"
        })));
        return __data

    def GetCode(self, sid):
        APIKey = self.config["apikey"]
        path = self.getPostAPI("code")
        __data = self.getTextRequest(path, str.encode(json.dumps({
            "type" : "get",
            "sid"  : sid
        })));
        return __data

    def GetData(self, pdid, ext):
        APIKey = self.config["apikey"]
        path = self.getPostAPI("data")
        __data = self.getTextRequest(path, str.encode(json.dumps({
            "type" : "get",
            "pdid"  : pdid,
            "ext"   : ext
        })));
        return __data

    def GetDataList(self, pid):
        APIKey = self.config["apikey"]
        path = self.getPostAPI("data")
        __data = self.getJSONRequest(path, str.encode(json.dumps({
            "type" : "list",
            "pid"  : pid
        })));
        return __data

    def PutRet(self, sid, data):
        APIKey = self.config["apikey"]
        path = self.getPostAPI("post/%d" % (sid))
        __data = self.getJSONRequest(path, data);
        return __data

    def PutStatus(self, sid, status, mem, time):
        APIKey = self.config["apikey"]
        path = self.getPostAPI("status")
        __data = self.getJSONRequest(path, str.encode(json.dumps({
            "type"   : "set",
            "sid"    : sid,
            "status" : status,
            "memlimit" : mem,
            "timelimit" : time
        })));
        return __data
