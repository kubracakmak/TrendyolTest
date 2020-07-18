import unittest
from trendyolProject.Login import loginPage
from trendyolProject.tabCheck import tabControl
from trendyolProject.UrunGorseli import UrunGorseli

class Main(loginPage,tabControl,UrunGorseli):

    def __init__(self):
        loginPage.__init__(self,driver="Chrome")


if __name__ == '__main__':
    testCases = Main()
    testCases.test_openWebPage()
    testCases.test_loginInfo()
    testCases.test_Kadin()
    testCases.test_Cocuk()
    testCases.test_EvYasam()
    testCases.test_Supermarket()
    testCases.test_Kozmetik()
    testCases.test_AyakkabiSapka()
    testCases.test_SaatAksesuar()
    testCases.test_Elektronik()
    testCases.test_CheckImagesInButik()
    testCases.test_DetailsSepet()