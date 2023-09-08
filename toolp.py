import openpyxl
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Đường dẫn đến file Excel
excel_file_path = './hieuha.xlsx'
chrome_driver_path = 'https://www.google.com/'

# Mở file Excel
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active

exceptions_list = []
count = 1

for row in sheet.iter_rows(min_row=2, values_only=True):  # Bắt đầu từ hàng thứ 2 (hàng đầu tiên chứa tiêu đề)
    username, email, password, phone, code = row[:5]
    # Khởi tạo trình duyệt web (ví dụ: Chrome)
    driver = webdriver.Chrome()
    # Điều hướng đến trang đăng ký
    driver.get('https://metahome.digital/sign-up')
    count = count+1
    time.sleep(30)
    # Tìm các phần tử input và nhập thông tin tương ứng
    driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="email"]').send_keys(email)
    driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="password"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="confirmPassword"]').send_keys(password)
    driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="referralCode"]').send_keys(code)
    element_to_click  = driver.find_element(By.CSS_SELECTOR, '#signUp .box form input[name="referralCode"]')
    # Điều hướng đến trang đăng ký 
    driver.execute_script("arguments[0].scrollIntoView();", element_to_click)

    time.sleep(1)
    # # Tìm và kiểm tra checkbox bằng ID
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#fullAgreement")))
    element.click()
        
    #Thực hiện đăng ký
    driver.find_element(By.CSS_SELECTOR, "#signUp .box form button.btn_signup").click()
    time.sleep(3)

    try:
        element_to_click  = driver.find_element(By.CSS_SELECTOR, '.btn_wait_kr')
        # Điều hướng đến trang đăng nhập 
        driver.execute_script("arguments[0].scrollIntoView();", element_to_click)
        # Nhập email và mật khẩu để đăng nhập
        driver.find_element(By.CSS_SELECTOR, '#logIn form input[name="email"]').send_keys(email)
        driver.find_element(By.CSS_SELECTOR, '#logIn form input[name="password"]').send_keys(password)
        # # Thực hiện đăng nhập
        driver.find_element(By.CSS_SELECTOR, "#logIn .box form button[type=submit]").click()

        time.sleep(5)
        driver.get('https://metahome.digital/mypage')
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.btn_add')))

        try:
            li_element = driver.find_element(By.XPATH, '//*[@id="myPage"]/section[2]/div/div/div/ul/li[2]/div/button').click()
            time.sleep(1)
            popup_element = driver.find_element(By.CSS_SELECTOR, '.register_phone form input[name="name"]').send_keys(username)
            popup_element = driver.find_element(By.CSS_SELECTOR, '.register_phone form input[name="phoneNumber"]').send_keys(phone)
            
            driver.find_element(By.CSS_SELECTOR, ".register_phone form button[type='submit']").click()

            time.sleep(2)
            driver.find_element(By.XPATH, ".v-card-title button[type='button']").click()
        except:
            print(count)
    except:
        exceptions_list.append(str(count))
        with open("exceptions.txt", "a") as file:
            file.write(str(exceptions_list) + "\n")  # Ghi lỗi vào tệp văn bản
    # Kết thúc
    driver.quit()

