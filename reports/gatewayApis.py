

def inlocal_server_live ():
    return 'http://213.232.124.169:9017/gateway/livedata/'
def inlocal_local_live ():
    return 'http://localhost:8080/gateway/livedata/'
def inserver_live ():
    return 'http://localhost:8035/gateway/livedata/'

def inlocal_server_getLogs ():
    return 'http://213.232.124.169:9017/gateway/api/getLogs/inPeriod/'
def inlocal_local_getLogs ():
    return 'http://localhost:8080/gateway/api/getLogs/inPeriod/'
def inserver_getLogs ():
    return 'http://localhost:8035/gateway/api/getLogs/inPeriod/'


def inlocal_local_getLogsData () :
    return 'http://localhost:8080/gateway/api/getLogs/inPeriod/data/'