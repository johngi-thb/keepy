from kee import FileExplorer
import os
import unittest
#project path: C:/Users/gilbe/OneDrive/Desktop/keepy
class TestFileExplorer(unittest.TestCase):
    def setUp(self):
        if not os.path.isdir('C:/test'):
            os.mkdir('C:/test')
        if not os.path.isdir('C:/test/first'):
            os.mkdir('C:/test/first')
        self.fe = FileExplorer('/e')
    
    def tearDown(self):
        os.rmdir('C:/test/first')
        os.rmdir('C:/test')
    
    def test_directory_not_found(self):
        self.assertIn('test', self.fe.directory)
    
    def test_directory_found(self):
        self.fe.update_directory('C:/test')
        self.assertIn('first', self.fe.directory)
    
    def test_update_directory_path_not_found_raises_error(self):
        self.assertRaises(FileNotFoundError, self.fe.update_directory,'/does/not/exist')
            
    def test_update_directory_path_not_found_goes_back_to_home_path(self):
        self.fe.update_directory('/does/not/exist')
        self.assertIn('test', self.fe.directory)




if __name__ == '__main__':
    unittest.main()