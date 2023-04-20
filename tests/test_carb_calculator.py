import pytest
from utils import utils

@pytest.mark.usefixtures("test_setup", "log_on_failure")
class TestCarbCalc():
    """
    This class contains tests for carbohydrate calculator
    """

    def test_correct_results_with_miffin_st_joer_formula(self):
        """
        This test verifies that the calculator displays correct results for male using Mifflin St Jeor formula.
        """
        self.driver.get(utils.URL)
        self.calculator.click_metric_units_tab(self.driver)
        self.calculator.input_age(self.driver, 25)
        self.calculator.select_gender(self.driver, 'male')
        self.calculator.input_height(self.driver, 180)
        self.calculator.input_weight(self.driver, 80)
        self.calculator.select_activity(self.driver, 'light')
        self.calculator.click_calculate_button(self.driver)
        assert self.calculator.check_results_visible(self.driver) == True

        expected_table_data = {
            'Weight Maintenance': ['2,482 Calories', '265 grams', '364 grams', '430 grams', '496 grams'],
            'Lose 0.5 kg/week': ['1,982 Calories', '211 grams', '291 grams', '344 grams', '396 grams'],
            'Lose 1 kg/week': ['1,482 Calories', '158 grams', '217 grams', '257 grams', '296 grams'],
            'Gain 0.5 kg/week': ['2,982 Calories', '318 grams', '437 grams', '517 grams', '596 grams'],
            'Gain 1 kg/week': ['3,482 Calories', '371 grams', '511 grams', '604 grams', '696 grams']
        }
        table_data = self.calculator.get_result(self.driver)

        assert expected_table_data == table_data

    @pytest.mark.parametrize("age", [18, 80])
    def test_car_calculator_with_valid_boundary_age_value(self, age):
        """
        This test verifies that the calculator displays results with valid age boundary values
        """
        self.driver.get(utils.URL)
        self.calculator.click_metric_units_tab(self.driver)
        self.calculator.input_age(self.driver, age)
        self.calculator.select_gender(self.driver, 'male')
        self.calculator.input_height(self.driver, 180)
        self.calculator.input_weight(self.driver, 80)
        self.calculator.select_activity(self.driver, 'light')
        self.calculator.click_calculate_button(self.driver)
        assert self.calculator.check_results_visible(self.driver) == True

    @pytest.mark.parametrize("age", [17, 81])
    def test_car_calculator_with_invalid_boundary_age_value(self, age):
        """
        This test verifies that the calculator displays error message with in valid age boundary values
        """
        self.driver.get(utils.URL)
        self.calculator.click_metric_units_tab(self.driver)
        self.calculator.input_age(self.driver, age)
        self.calculator.select_gender(self.driver, 'male')
        self.calculator.input_height(self.driver, 180)
        self.calculator.input_weight(self.driver, 80)
        self.calculator.select_activity(self.driver, 'light')
        self.calculator.click_calculate_button(self.driver)
        assert self.calculator.check_error_visible(self.driver) == True
