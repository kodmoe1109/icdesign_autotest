from weakref import WeakValueDictionary
import pytest
import utils
import time



def test_login():
    
    try :
        web = utils.preload()
        # utils.login(web,"A123456789","A123456789")
        # utils.modify_profile(web,"091222234")
        # utils.test_sign_up(web)
        # utils.score_search(web)
        # utils.brief_download(web)
    finally:
        time.sleep(3)
        web.close()
    

def test_login1():
    web = utils.preload()
    try :
        utils.login(web,"A123456789","A123456789")
        utils.modify_profile(web,"091222234")
    finally:
        web.close()
