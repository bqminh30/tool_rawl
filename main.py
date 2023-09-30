import os
import openpyxl
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

# Đường dẫn đến file Excel
excel_file_path = './mmmm.xlsx'

# Mở file Excel
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active
options = webdriver.ChromeOptions()
options.add_experimental_option(
    "excludeSwitches", ['enable-automation'])
exceptions_list = []
count = 1
driver = webdriver.Chrome(
        options
)
for row in sheet.iter_rows(min_row=415, values_only=True): 
    username, email, password, phone, code = row[:5]
    # Khởi tạo trình duyệt web (ví dụ: Chrome)
    
    # Điều hướng đến trang đăng ký
    driver.switch_to.new_window()
    # Điều hướng đến trang đăng ký
    driver.get('https://metahome.digital/sign-up')
    
    count = count+1
    print('đang chạy ở hàng',count)
    
    # Tìm các phần tử input và nhập thông tin tương ứng
    driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="email"]').send_keys(email)
    time.sleep(0.2)
    driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="password"]').send_keys(password)
    time.sleep(0.2)
    driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="confirmPassword"]').send_keys(password)
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="referralCode"]').send_keys(code)
    element_to_click  = driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="referralCode"]')
    # Điều hướng đến trang đăng ký 
    driver.execute_script("arguments[0].scrollIntoView();", element_to_click)
    time.sleep(1)
    # # Tìm và kiểm tra checkbox bằng ID
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#fullAgreement")))
    element.click()
    time.sleep(1)
    #Thực hiện đăng ký
    driver.find_element(By.CSS_SELECTOR, "#signUp .box form button.btn_signup").click()
    time.sleep(1)

    try:
        time.sleep(1)
        element_to  = driver.find_element(By.CSS_SELECTOR, '.btn_wait_kr')
        # Điều hướng đến trang đăng nhập 
        driver.execute_script("arguments[0].scrollIntoView();", element_to)
        # Nhập email và mật khẩu để đăng nhập
        driver.find_element(By.CSS_SELECTOR, '#logIn form input[name="email"]').send_keys(email)
        driver.find_element(By.CSS_SELECTOR, '#logIn form input[name="password"]').send_keys(password)
        # # Thực hiện đăng nhập
        driver.find_element(By.CSS_SELECTOR, "#logIn .box form button[type=submit]").click()

        time.sleep(2)
        driver.get('https://metahome.digital/mypage')
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_add')))

        try:
            li_element = driver.find_element(By.XPATH, '//*[@id="myPage"]/section[2]/div/div/div/ul/li[2]/div/button').click()
            time.sleep(1)
            popup_element = driver.find_element(By.CSS_SELECTOR, '.register_phone form input[name="name"]').send_keys(username)
            popup_element = driver.find_element(By.CSS_SELECTOR, '.register_phone form input[name="phoneNumber"]').send_keys(phone)
            
            driver.find_element(By.CSS_SELECTOR, ".register_phone form button[type='submit']").click()

            time.sleep(1)
            driver.delete_all_cookies()
            
            driver.close()
            time.sleep(45)
            
        except:
            print(count)
            driver.delete_all_cookies()
            driver.close()
            
    # except:
        
        
    except WebDriverException as e:
        exceptions_list.append(str(count))
        with open("except1.txt", "a") as file:
            file.write(str(exceptions_list) + "\n")  # Ghi lỗi vào tệp văn bản
        driver.delete_all_cookies()
        driver.close()
        time.sleep(45)
        print(f"Có lỗi khi truy cập URL: {e}")
    finally:
        driver.quit() 