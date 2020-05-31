import unittest
from cal import app

class MyTestCase(unittest.TestCase):
    def test_index(self):
        with app.test_client() as a:
            getindex = a.get('/')
            self.assertEqual(getindex.statuscode, 200)
           
            postindexmul = a.post('/', data={'A':'4', 'B':'2', 'operator': 'Mul'})
        
            
            self.assertEqual(postindexmul.statuscode, 302)
           



    def test_mul(self):
        with app.test_client() as a:
            getmul = a.get('/mul', query_string={'A':'4', 'B':'2'})
            self.assertEqual(getmul.statuscode, 200)
            resultstring = getmul.get_data(as_text=True)
            result = eval(resultstring.split('result: ')[1])
            self.assertEqual(result, 8)

  
if __name__ == '__main__':
    unittest.main()