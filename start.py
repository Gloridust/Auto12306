from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 输入用户信息
username = input("请输入12306用户名: ")
password = input("请输入12306密码: ")
from_station = input("请输入出发站: ")
to_station = input("请输入目的站: ")
date = input("请输入出发日期 (格式: 2023-09-30): ")
train_number = input("请输入车次: ")

# 初始化浏览器
driver = webdriver.Chrome()

try:
    # 打开12306网站
    driver.get("https://www.12306.cn/index/")

    # 点击登录链接
    login_link = driver.find_element_by_link_text("登录")
    login_link.click()
    time.sleep(1)

    # 输入用户名和密码
    username_input = driver.find_element_by_id("J-userName")
    username_input.clear()
    username_input.send_keys(username)

    password_input = driver.find_element_by_id("J-password")
    password_input.clear()
    password_input.send_keys(password)
    
    # 等待一段时间，手动完成验证码验证
    input("请手动完成验证码验证后，按 Enter 键继续...")

    # 点击登录按钮
    login_submit = driver.find_element_by_id("J-login")
    login_submit.click()
    time.sleep(2)

    # 查询车票
    driver.get("https://kyfw.12306.cn/otn/leftTicket/init")

    from_station_input = driver.find_element_by_id("fromStationText")
    from_station_input.clear()
    from_station_input.send_keys(from_station)
    from_station_input.send_keys(Keys.RETURN)

    to_station_input = driver.find_element_by_id("toStationText")
    to_station_input.clear()
    to_station_input.send_keys(to_station)
    to_station_input.send_keys(Keys.RETURN)

    date_input = driver.find_element_by_id("train_date")
    date_input.clear()
    date_input.send_keys(date)
    date_input.send_keys(Keys.RETURN)

    search_btn = driver.find_element_by_id("query_ticket")
    search_btn.click()
    time.sleep(2)

    # 选择车次并提交订单
    choose_btn = driver.find_element_by_link_text(train_number)
    choose_btn.click()
    time.sleep(2)

    submit_btn = driver.find_element_by_link_text("预订")
    submit_btn.click()
    time.sleep(2)

    # 确认购票信息
    confirm_btn = driver.find_element_by_id("submitOrder_id")
    confirm_btn.click()
    time.sleep(2)

    # 提交订单
    submit_order_btn = driver.find_element_by_link_text("提交订单")
    submit_order_btn.click()
    time.sleep(2)

    print("抢票成功！请在限定时间内完成支付。")

except Exception as e:
    print("抢票过程中出现错误:", str(e))

finally:
    # 关闭浏览器
    driver.quit()
