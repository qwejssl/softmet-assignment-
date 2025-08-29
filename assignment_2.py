import unittest
import json
from collections import defaultdict

from selenium import webdriver
from selenium.webdriver.common.by import By

ORIGINAL_URL = 'https://en.wikipedia.org/wiki/Software_metric'
CYCLES = 10


class TestGetPerformance(unittest.TestCase):
    def setUp(self):
        self.url = ORIGINAL_URL
        self.cycles = CYCLES

    def test_performance(self):
        # Dictionary to store performance data for each URL
        url_performance_data = defaultdict(list)

        for _ in range(self.cycles):
            opts = webdriver.ChromeOptions()
            opts.add_argument("--incognito")
            driver = None
            try:
                driver = webdriver.Chrome(options=opts)
                driver.get(self.url)
                title = driver.find_element(By.CSS_SELECTOR, "#firstHeading > span")
                self.assertIn('Software metric', title.text)
                script = "return window.performance.getEntries().map(x => [x.name, x.duration])"
                performance_data = driver.execute_script(script)
                if performance_data:
                    for url, duration in performance_data:
                        url_performance_data[url].append(duration)
            finally:
                if driver:
                    driver.quit()

        # Ensure there are 10 performance records for the first URL
        if url_performance_data:
            self.assertEqual(len(url_performance_data[next(iter(url_performance_data))]), self.cycles)

        # Save the raw performance data to a file
        with open("./raw_performance_data.json", 'w', encoding='utf8') as file:
            json.dump(url_performance_data, file, indent=4)

        # Test calculation of averages with sample data
        sample_data = [1, 2, 3, 4, 5]  # Average should be 3
        filtered_data = list(filter(lambda x: x != 0, sample_data))
        calculated_average = sum(filtered_data) / len(filtered_data)
        self.assertAlmostEqual(calculated_average, 3)

        # Calculate average performance for each URL
        average_performance_data = defaultdict(list)
        for url, durations in url_performance_data.items():
            filtered_data = list(filter(lambda x: x != 0, durations))
            if len(filtered_data) == 0:
                average_performance_data[url].append(0)
            else:
                average_performance_data[url].append(sum(filtered_data) / len(filtered_data))

        # Ensure there is only one average value per URL
        if average_performance_data:
            self.assertEqual(len(average_performance_data[next(iter(average_performance_data))]), 1)

        # Save the processed average performance data to a file
        with open("./average_performance_data.json", 'w', encoding='utf8') as file:
            json.dump(average_performance_data, file, indent=4)

    def tearDown(self) -> None:
        print("done")


if __name__ == "__main__":
    unittest.main()
