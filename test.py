
import unittest
from cal import app

class MyTestCase(unittest.TestCase):
    def test_index(self):
        with app.test_client() as a:
            getindex = a.get('/')
            self.assertEqual(getindex.statuscode, 200)
            postindexadd = a.post('/', data={'A':'6', 'B':'5', 'operator': 'Add'}
            
    def test_add(self):
        with app.test_client() as a:
            get_add = a.get('/add', query_string={'A':'6', 'B':'5'})
            self.assertEqual(get_add._status_code, 200)
            result_string = get_add.get_data(as_text=True)
            result = eval(result_string.split('result: ')[1])
            self.assertEqual(result, 11)

    

if __name__ == '__main__':
    unittest.main()