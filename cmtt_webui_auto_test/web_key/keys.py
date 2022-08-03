from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


#构造浏览器对象
def open_browser(type_):
    try:
        driver = getattr(webdriver, type_)()
    except:
        driver = webdriver.Chrome()
    return driver

class keys:

    action = ActionChains(webdriver)

    #构造函数
    def __init__(self, type_):
        self.driver = open_browser(type_)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def open_url(self, url):
        self.driver.get(url)

    def locate(self, by , value):
        return self.driver.find_element(by, value)

    def input(self, by, value, txt):
        self.locate(by, value).send_keys(txt)

    def click(self,by, value):
        self.locate(by, value).click()

    def sleep(self, time_):
        time.sleep(int(time_))

    def quit(self):
        self.driver.quit()

    def mouse_hold(self, by, value):
        self.action.move_to_element(self.locate(by, value)).perform()

    def mouse_doubleclick(self, by, value):
        self.action.double_click((self.locate(by,value)).perform())

    def mouse_rightclick(self, by, value):
        self.action.context_click(self.locate(by, value)).perform()

    def switch_handle(self, status=1):
        handles = self.driver.window_handles
        if status == 1:
            self.driver.close()
        self.driver.switch_to_window(handles[1])

    def assert_text(self, by, value, expect):
        try:
            reality = self.locate(by, value).text
            assert expect == reality, '{0}与{1}不相等'.format(expect, reality)
            return True
        except:
            return False
        # except Exception as e:
        #     print("断言失败，{}".format(e))

    def assert_almost_equal(self, by, value, expected):
        try:
            reality = self.locate(by, value).text
            assert expected in reality, '{0}不在{1}的范围内'.format(expected, reality)
            return True
        except:
            return False
    # def assert_



# class Excelread:
#     def getdata(self):
#         workbook = openpyxl.load_workbook("xxxx")
#         sh1 = workbook.get_sheet_by_name("xxxx")
#         rows = sh1.max_row
#         cols = sh1.max_colnum
#         datalist = []
#         for x in range(2,rows+1):
#             dict1 = {}
#             for y in range(1,cols+1):
#                 value = sh1.cell(x,y).value
#                 dict1[sh1.cell(1,y).value]=value
#             datalist.append(dict1)
#         return datalist


