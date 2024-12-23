from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import unittest 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Instagram(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--user-data-dir=D:\\WorkSpaces\\Learn\\Testing\\UnitTest\\profile") #change path to folder profile
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://www.instagram.com/")
        self.driver.implicitly_wait(30)

    def test_tym_post(self):
        link_post = self.link_post
        self.driver.get(f'https://www.instagram.com/p/{link_post}/')
        self.driver.implicitly_wait(30)
        time.sleep(1)
        checklike = self.driver.find_element("xpath", "//*[@fill='currentColor' and @height='24' and @aria-label='Like' or @aria-label='Unlike']").get_attribute('aria-label')
        time.sleep(5)
        print("Trạng thái:", checklike)
        if checklike.strip() == "Unlike":
            print("Bài viết đã được Like => Kết thúc tiến trình")
            return
        elif checklike.strip() == "Like":
            print("Bài viết chưa được Like => Tiến hành Like")
            btnLike = self.driver.find_element("xpath", '//span[@class="xp7jhwk"]')
            btnLike.click()
            btnLike.click()
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
        user = self.user
        link_post = self.link_post
        content= self.content
        self.driver.implicitly_wait(30)
        self.driver.get(f'https://www.instagram.com/p/{link_post}/')
        self.driver.implicitly_wait(30)
        self.driver.find_element("xpath", "//textarea[contains(@aria-label,'Add a comment…')]").send_keys(f"{content}")
        clickable_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[text()="Post"]'))
        )
        clickable_element.click()
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
    Instagram.link_post = 'DC9o_1QxzHL';
    Instagram.content = "Hello bro"
    Instagram.user = "abgsaw"
    unittest.main()
