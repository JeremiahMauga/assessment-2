import unittest


from interface import Interface

class TestFunctionName(unittest.TestCase) :
      
    def test_mode_1(self) :
        self.assertEqual(Interface.runner(1), parameter)
    
    def test_mode_2(self) :
        self.assertEqual(Interface.runner(2), parameter)
    
    def test_mode_3(self) :
        self.assertEqual(Interface.runner(3), parameter)
    
    def test_mode_4(self) :
        self.assertEqual(Interface.runner(4), parameter)
    
    def test_mode_5(self) :
        self.assertEqual(Interface.runner(5), parameter)

if __name__ == '__main__':
    unittest.main()