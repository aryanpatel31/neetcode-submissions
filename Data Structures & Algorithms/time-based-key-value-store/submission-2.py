class TimeMap:

    def __init__(self):
        self.data = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.data:
            self.data[key] = [(timestamp, value)]
        else:
            self.data[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
    
        if key not in self.data:
            return ""
   
        myVals = self.data[key]
        l = 0
        r = len(myVals) - 1

        if myVals[0][0] <= timestamp:
            res = myVals[0][1]
        else:
            return ""

        while l <= r:
            m = l + ((r-l) // 2)
            if myVals[m][0] == timestamp:
                return myVals[m][1]
            elif myVals[m][0] < timestamp:
                res = myVals[m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res

        

        
