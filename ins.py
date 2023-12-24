from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest 
from selenium import webdriver


class Instagram(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--user-data-dir=D:\\WorkSpace\\Python\\profile")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.implicitly_wait(30)

    def test_tym_post(self):
        link_post = self.link_post
        self.driver.get(f'https://www.instagram.com/p/{link_post}/')
        self.driver.implicitly_wait(30)
        time.sleep(1)
        checklike = self.driver.find_element("xpath", "//*[@fill='currentColor' and @height='24' and @aria-label='Like' or @aria-label='Unlike']").get_attribute('aria-label')
        time.sleep(5)
        print("Trạng thái:",checklike)
        if checklike.strip() == "Unlike":
            print("Bài viết đã được Like => Kết thúc tiến trình")
            return
        elif checklike.strip() == "Like":
            print("Bài viết chưa được Like => Tiến hành Like")
            self.driver.find_element("xpath", '//span[@class="xp7jhwk"]').click()
            checklike = self.driver.find_element("xpath", "//*[@fill='currentColor' and @height='24' and @aria-label='Like' or @aria-label='Unlike']").get_attribute('aria-label')
            time.sleep(5)
            print("Trạng thái:",checklike)
            if checklike.strip() == "Unlike":
                self.assertEqual(checklike, "Unlike")
                print("Like bài viết thành công => Passed")
                return
            elif checklike.strip() == "Like":
                print("Like bài viết thất bại => Failed")
                return

    def test_cmt_post(self):
        user = self.driver.find_element("xpath", '//div[@class="x1n2onr6"]//a').get_attribute('href').split("/")[3]
        link_post = self.link_post
        content= self.content
        self.driver.implicitly_wait(30)
        self.driver.get(f'https://www.instagram.com/p/{link_post}/')
        self.driver.implicitly_wait(30)
        self.driver.find_element("xpath", "//textarea[contains(@aria-label,'Add a comment…')]").send_keys(f"{content}")
        time.sleep(1)
        self.driver.find_element("xpath", '//div[@class="_aidp"]').click()
        time.sleep(3)
        us = self.driver.find_element("xpath", f'//span[div="{user}"]/div/a/div/div/span').text
        cont = self.driver.find_element("xpath", f'//div[span="{content}"]/span').text
        # lấy all cmt
        a = self.driver.find_element("xpath", '//div[@class="x78zum5 xdt5ytf x1iyjqo2"]').text
        # print(a.split("Reply"))
        for cmt in a.split("Reply"):
            if us in cmt and cont in cmt:
                print(cmt)
                self.assertEqual(cont, content)
                print(f"Tồn tại User: {us} và bình luận: {cont} => Passed")
                return
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    Instagram.link_post = 'C1NnQRxImaU';
    Instagram.content = "Hello bro"
    unittest.main()