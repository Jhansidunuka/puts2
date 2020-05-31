
import unittest
from cal import app

class MyTestCase(unittest.TestCase):
    def test_index(self):
        with app.test_client() as a:
            getindex = a.get('/')
            self.assertEqual(getindex.statuscode, 200)
       
            postindexdiv = a.post('/', data={'A':'4', 'B':'2', 'operator': 'Div'})
           
            self.assertEqual(postindexdiv.statuscode, 302)

   
    def test_div(self):
        with app.test_client() as a:
            getdiv = a.get('/div', query_string={'A':'4', 'B':'2'})
            self.assertEqual(getdiv.statuscode, 200)
            resultstring = getdiv.get_data(as_text=True)
            result = eval(resultstring.split('result: ')[1])
            self.assertEqual(result,2)

if __name__ == '__main__':
    unittest.main()