import os
from get_version import *

def main(args):
    if os.path.exists('curVer.txt'):
        with open('curVer.txt') as f:
            ver = f.read()
        appId, appVer = getAppInfo(args[1], args[0])
        if ver == appVer:
            return 1
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))