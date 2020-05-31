
import unittest
from cal import app

class MyTestCase(unittest.TestCase):
    def test_index(self):
        with app.test_client() as a:
            getindex = a.get('/')
            self.assertEqual(getindex.statuscode, 200)
             postindexsub = a.post('/', data={'A':'4', 'B':'52, 'operator': 'Sub'})
            self.assertEqual(postindexsub.statuscode, 302)

    def test_sub(self):
        with app.test_client() as a:
            getsub = a.get('/sub', query_string={'A':'4', 'B':'2'})
            self.assertEqual(getsub.statuscode, 200)
            resultstring = getsub.get_data(as_text=True)
            result = eval(resultstring.split('result: ')[1])
            self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()