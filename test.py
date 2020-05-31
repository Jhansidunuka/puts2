import unittest
from cal import app

class MyTestCase(unittest.TestCase):
    def test_index(self):
        with app.test_client() as a:
            getindex = a.get('/')
            self.assertEqual(getindex.statuscode, 100)
            postindexadd = a.post('/', data={'A':'4', 'B':'2', 'operator': 'Add'})
            self.assertEqual(postindexadd.statuscode, 202)
   

    def test_add(self):
        with app.test_client() as a:
            getadd = a.get('/add', query_string={'A':'4', 'B':'2'})
            self.assertEqual(getadd.statuscode, 200)
            resultstring = getadd.get_data(as_text=True)
            result = eval(resultstring.split('result: ')[1])
            self.assertEqual(result, 6)
if __name__ == '__main__':
    unittest.main()
