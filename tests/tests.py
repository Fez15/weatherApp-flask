from app import app
import unittest
import xmlrunner


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    # Ensure that page loads correctly
    def test_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Get weather' in response.data)
    
    # Ensure correct result appears
    def test_weather_result(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(city="Las Vegas"), follow_redirects = True)
        self.assertTrue(b'US' in response.data)
        self.assertFalse(b'AU' in response.data)
    
    


if __name__ == '__main__':
    #unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
    unittest.main()
