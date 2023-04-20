from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CarbCalcPage:
    '''This class has all the locators and action methods for the elements of the carbohydrate calulate page only'''

    def __init__(self):
        self.age_text_box = "//input[@id='cage']"
        self.height_text_box = "//input[@id='cheightmeter']"
        self.weight_text_box = "//input[@id='ckg']"
        self.metric_units_tab = "//a[contains(text(), 'Metric Units')]"
        self.male_radio_button = "//label[@for='csex1']"
        self.activity_drop_down = "cactivity"
        self.caclulate_button = "//input[@alt='Calculate']"
        self.result_table = "//table[@class='cinfoT']//tbody"
        self.result_header = "//h2[@class='h2result']"
        self.error_message = "//div/font[contains(text(), 'Please provide an age between 18 and 80.')]"

    def click_metric_units_tab(self, driver):
        driver.find_element(By.XPATH, self.metric_units_tab).click()

    def input_age(self, driver, age):
        driver.find_element(By.XPATH, self.age_text_box).clear()
        driver.find_element(By.XPATH, self.age_text_box).send_keys(age)

    def input_height(self, driver, height):
        driver.find_element(By.XPATH, self.height_text_box).clear()
        driver.find_element(By.XPATH, self.height_text_box).send_keys(height)

    def input_weight(self, driver, weight):
        driver.find_element(By.XPATH, self.weight_text_box).clear()
        driver.find_element(By.XPATH, self.weight_text_box).send_keys(weight)

    def select_gender(self, driver, gender):
        if gender == 'male':
            driver.find_element(By.XPATH, self.male_radio_button).click()

    def select_activity(self, driver, activity_type):
        dropdown_element = driver.find_element(By.NAME, self.activity_drop_down)
        dropdown = Select(dropdown_element)
        if activity_type == 'light':
            dropdown.select_by_value("1.375")
        elif activity_type == 'moderate':
            dropdown.select_by_value("1.465")

    def check_results_visible(self, driver):
        return driver.find_element(By.XPATH, self.result_header).is_displayed()

    def check_error_visible(self, driver):
        return driver.find_element(By.XPATH, self.error_message).is_displayed()

    def get_result(self, driver):
        table_data = {}
        
        for i in range(2, 7):
            sub_data = []
            data_for = driver.find_element(By.XPATH, self.result_table + f"//tr[{i}]//td[{1}]").text
            for j in range(2, 7):
                data = driver.find_element(By.XPATH, self.result_table + f"//tr[{i}]//td[{j}]").text
                sub_data.append(data)
                table_data[data_for] = sub_data
        return table_data

    def click_calculate_button(self, driver):
        driver.find_element(By.XPATH, self.caclulate_button).click()
