from django.test import TestCase
from datetime import datetime
from l2l.templatetags.l2l_extras import l2l_dt


class TemplateFilterTests(TestCase):
    def test_l2l_dt_string(self):
        date_string = "2024-05-05T17:00:00"
        filtered_date = l2l_dt(date_string)
        expected_date = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
        
        self.assertEqual(filtered_date, expected_date)

    def test_l2l_dt_datetime(self):
        date_time_obj = datetime(2024, 5, 5, 17, 0, 0)
        filtered_date = l2l_dt(date_time_obj)        
        expected_date = date_time_obj.strftime("%Y-%m-%d %H:%M:%S")
        
        self.assertEqual(filtered_date, expected_date)
        
    def test_l2l_dt_float(self):
        filtered_date = l2l_dt(3.14)
        
        expected_date = ""
        self.assertEqual(filtered_date, expected_date)
        
    def test_l2l_dt_bool(self):
        filtered_date = l2l_dt(True)
        
        expected_date = ""
        self.assertEqual(filtered_date, expected_date)
    
    def test_l2l_dt_empty_filter(self):    
        filtered_date = l2l_dt("")
        
        expected_date = ""
        self.assertEqual(filtered_date, expected_date)
        
    def test_l2l_dt_invalid_date(self):
        invalid_date_string = "2024-13-32T25:70:99" 
        with self.assertRaises(ValueError):
            l2l_dt(invalid_date_string)

