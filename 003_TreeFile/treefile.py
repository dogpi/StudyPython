import collections
import os

def getAllDirDeque(path):
    queue = collections.deque()
    queue.append(path)
    while len(queue):
        dirPath = queue.popleft()
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            absPath = os.path.join(dirPath,fileName)
            if os.path.isdir(absPath):
                print("dir:",fileName)
                queue.append(absPath)
            else:
                print("file:",fileName)