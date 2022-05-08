var getHeader = null;
function init() {
    var CFURLCreateWithBytes = new NativeFunction(Module.findExportByName('CoreFoundation','CFURLCreateWithBytes'), 'pointer', ['pointer', 'pointer', 'int64', 'int64', 'int64'])
    var CFDictionaryGetCount = new NativeFunction(Module.findExportByName('CoreFoundation','CFDictionaryGetCount'), 'int64', ['pointer'])
    var CFCopyDescription = new NativeFunction(Module.findExportByName('CoreFoundation','CFCopyDescription'), 'pointer', ['pointer'])
    var CFStringGetCStringPtr = new NativeFunction(Module.findExportByName('CoreFoundation','CFStringGetCStringPtr'), 'pointer', ['pointer', 'uint64'])
    var CFStringGetCString = new NativeFunction(Module.findExportByName('CoreFoundation','CFStringGetCString'), 'int8', ['pointer', 'pointer', 'int64', 'int64'])
    var CFStringGetLength = new NativeFunction(Module.findExportByName('CoreFoundation','CFStringGetLength'), 'int64', ['pointer'])
    var CFDictionaryGetCount = new NativeFunction(Module.findExportByName('CoreFoundation','CFDictionaryGetCount'), 'int64', ['pointer'])
    var CFDictionaryGetKeysAndValues = new NativeFunction(Module.findExportByName('CoreFoundation','CFDictionaryGetKeysAndValues'), 'void', ['pointer', 'pointer', 'pointer'])
    var CFDataGetBytePtr = new NativeFunction(Module.findExportByName('CoreFoundation','CFDataGetBytePtr'), 'pointer', ['pointer'])
    var CFDataGetLength = new NativeFunction(Module.findExportByName('CoreFoundation','CFDataGetLength'), 'uint64', ['pointer'])
    
    var readCFStr = (cfs) => {
        var cfslen = CFStringGetLength(cfs)
        var cfsBuf = Memory.alloc(cfslen + 1)
        CFStringGetCString(cfs, cfsBuf, cfslen + 1, 134217984)
        return Memory.readUtf8String(cfsBuf, cfslen)
    }
    
    var readCFDict = (cfdict) => {
        var dictCount = CFDictionaryGetCount(cfdict)
        var dictKeys = Memory.alloc(dictCount * 8)
        var dictValues = Memory.alloc(dictCount * 8)
        CFDictionaryGetKeysAndValues(cfdict, dictKeys, dictValues)
        var ret = {}
        for (var i = 0; i < dictCount; i++) {
            var k = readCFStr(dictKeys.add(8 * i).readPointer())
            var v = readCFStr(dictValues.add(8 * i).readPointer())
            ret[k] = v
        }
        return ret
    }
    
    var readCFData = (cfd) => {
        var cfdlen = CFDataGetLength(cfd)
        var cfdbuf = CFDataGetBytePtr(cfd)
        return cfdbuf.readByteArray(cfdlen)
    }
    
    var itunesBase = Process.enumerateModulesSync()[0].base
    var cfAllocator = itunesBase.add(0x22A8448).readPointer()
    var kbsyncContext = itunesBase.add(0x22A6BBC).readU32()
    var prepareAppleHdrWrap = new NativeFunction(itunesBase.add(0x87FFC0), 'pointer',['pointer','pointer','pointer']);
    var get_cookie_val = new NativeFunction(itunesBase.add(0xBDE500), 'pointer',['pointer']);
    var get_kbsync = new NativeFunction(itunesBase.add(0x74D210), 'pointer',['uint32', 'uint32', 'pointer']);

    getHeader = function (url) {
        var GlobalContext = itunesBase.add(0x22A9B18).readPointer()
        var otpGlobalContext = GlobalContext
        if (!GlobalContext.isNull()) {
            otpGlobalContext = GlobalContext.add(62716).readPointer()
        }
        
        var otpContext = Memory.alloc(128)
        otpContext.writePointer(otpGlobalContext)
        otpContext.add(8).writeU64(0)
        otpContext.add(16).writeU64(0)
        otpContext.add(24).writeU16(1)
        otpContext.add(26).writeU8(0)
        otpContext.add(27).writeU8(1)  // include X-Guid
        otpContext.add(28).writeU8(1)  // include ADIV1 Hdrs
        otpContext.add(32).writeU32(0)
        otpContext.add(36).writeU16(0)
        otpContext.add(40).writeU32(0)
        otpContext.add(48).writeU64(0)
        otpContext.add(64).writeU64(0)
        otpContext.add(72).writeU64(0)
        otpContext.add(84).writeU64(0)
        otpContext.add(112).writeU8(1)
        
        var urlBuf = Memory.allocUtf8String(url)
        var urlData = CFURLCreateWithBytes(cfAllocator, urlBuf, url.length, 0x8000100, 0)

        var kbsync = get_kbsync(kbsyncContext, 1, otpGlobalContext)
        
        var cookieCFStr = get_cookie_val(urlData)
        var hdrDict = prepareAppleHdrWrap(NULL, urlData, otpContext)
        //hdrdesc = CFCopyDescription(hdrDict)
        //console.log(readCFStr(hdrdesc))
        
        var cookieStr = readCFStr(cookieCFStr)
        var hdrOutput = readCFDict(hdrDict)
        hdrOutput['Cookie'] = cookieStr
        
        var kbSyncData = readCFData(kbsync)
        hdrOutput['kbsync'] = [...new Uint8Array(kbSyncData)].map(x => x.toString(16).padStart(2, '0')).join('');
        
        return hdrOutput
    };
}

rpc.exports = {
    getHeader: (url) => {
        if (!getHeader) {
            init()
        }
        return getHeader(url);
    },
};