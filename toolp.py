import pandas as pd
import openpyxl
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Đường dẫn đến file Excel
excel_file_path = './hieu.xlsx'
chrome_driver_path = 'https://www.google.com/'

# Mở file Excel
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active

# Khởi tạo trình duyệt web (ví dụ: Chrome)
driver = webdriver.Chrome()

# Điều hướng đến trang đăng ký
driver.get('https://metahome.digital/sign-in')

# Lặp qua từng hàng trong dữ liệu Excel và nhập thông tin đăng ký
for row in sheet.iter_rows(min_row=2, values_only=True):  # Bắt đầu từ hàng thứ 2 (hàng đầu tiên chứa tiêu đề)
    username, email, password, phone, code = row[:5]
    
    # Tìm các phần tử input và nhập thông tin tương ứng
    # driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="email"]').send_keys(email)
    # driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="password"]').send_keys(password)
    # driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="confirmPassword"]').send_keys(password)
    # driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="referralCode"]').send_keys(code)

    # # Tìm và kiểm tra checkbox bằng ID
    # checkbox = driver.find_element(By.ID, 'fullAgreement')

    # # Kiểm tra xem checkbox đã được chọn hay chưa
    # if not checkbox.is_selected():
    # # Nếu chưa chọn, thì chọn checkbox
    #     checkbox.click()

    # time.sleep(2)
    # # Thực hiện đăng ký (ví dụ: nhấn nút đăng ký)
    # driver.find_element(By.CSS_SELECTOR, "#signUp .box form button[type='submit']").click()

    # Thực hiện đăng ký 
    # driver.find_element_by_class('btn_signup').click()
    # Sử dụng WebDriverWait để đợi cho đến khi trang sign-in xuất hiện
    wait = WebDriverWait(driver, 10)  # 10 là thời gian tối đa bạn muốn đợi (có thể thay đổi)
    wait.until(EC.presence_of_element_located((By.ID, 'logIn')))  # Đợi cho đến khi thấy phần tử sign-in

    element_to_click  = driver.find_element(By.CSS_SELECTOR, '.btn_wait_kr')
    # Điều hướng đến trang đăng nhập 
    driver.execute_script("arguments[0].scrollIntoView();", element_to_click)
    # driver.get('https://metahome.digital/sign-in')

    # Nhập email và mật khẩu để đăng nhập
    driver.find_element(By.CSS_SELECTOR, '#logIn form input[name="email"]').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, '#logIn form input[name="password"]').send_keys(password)


    # Thực hiện đăng nhập
    driver.find_element(By.CSS_SELECTOR, "#logIn form button[type='submit']").click()
    
    time.sleep(5)
    driver.get('https://metahome.digital/mypage')
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_add')))  

    element_to_click  = driver.find_element(By.CSS_SELECTOR, '.btn_add')

    # driver.find_element(By.CSS_SELECTOR, ".secu_cer .box form button[type='submit']").click()
# Kết thúc phiên làm việc
# driver.quit()