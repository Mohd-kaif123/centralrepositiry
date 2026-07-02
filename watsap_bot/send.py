import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# ================= CONFIG =================
EXCEL_FILE = "contacts.xlsx"
NUMBER_COLUMN = "Number"
COUNTRY_CODE = "91"
TEST_MESSAGE = "Hii"
GAP_SECONDS = 5
CHROME_PROFILE_PATH = "/mnt/d/python_practise/centralrepositiry/watsap_bot/chrome_profile"
# ============================================

df = pd.read_excel(EXCEL_FILE)
raw_numbers = df[NUMBER_COLUMN].astype(str).str.strip().tolist()

numbers = []
for n in raw_numbers:
    n = n.replace(".0", "")
    if not n.startswith(COUNTRY_CODE):
        n = COUNTRY_CODE + n
    numbers.append(n)

print(f"Total {len(numbers)} numbers mile:", numbers)

chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="149.0.7827.114").install()), options=chrome_options)
driver.get("https://web.whatsapp.com")

print("\n>>> Agar QR code dikh raha hai to ABHI scan karein.")
print(">>> Jab tak WhatsApp ki chat list screen par na dikhe, tab tak wait karo, phir yahan Enter dabao.")
input(">>> Login ho jaye to Enter dabao...")

wait = WebDriverWait(driver, 30)

for number in numbers:
    try:
        driver.get(f"https://web.whatsapp.com/send?phone={number}")
        time.sleep(7)

        # Check karo invalid number popup to nahi hai
        try:
            invalid_popup = driver.find_element(By.XPATH, '//div[contains(text(), "Phone number shared via url is invalid")]')
            print(f"⚠️ {number} - Invalid WhatsApp number, skip kar raha hu")
            continue
        except:
            pass  # popup nahi mila, matlab number sahi hai, aage badho

        # Message box dhoondo - multiple selectors try karo
        message_box = None
        selectors = [
            '//div[@contenteditable="true"][@data-tab="10"]',
            '//div[@contenteditable="true"][@aria-label="Type a message"]',
            '//footer//div[@contenteditable="true"]'
        ]
        for sel in selectors:
            try:
                message_box = wait.until(EC.presence_of_element_located((By.XPATH, sel)))
                if message_box:
                    break
            except:
                continue

        if not message_box:
            raise Exception("Message box nahi mila")

        message_box.click()
        time.sleep(1)
        message_box.send_keys(TEST_MESSAGE)
        time.sleep(1)
        message_box.send_keys(Keys.ENTER)

        print(f"✅ Sent 'Hii' to {number}")

    except Exception as e:
        print(f"❌ Failed for {number}: {e}")
        # Screenshot lekar dikhao kya screen par tha
        screenshot_path = f"error_{number}.png"
        driver.save_screenshot(screenshot_path)
        print(f"   📸 Screenshot saved: {screenshot_path}")

    time.sleep(GAP_SECONDS)

print("\nSab ko test message chala gaya. Enter dabao browser band karne ke liye.")
input()
driver.quit()