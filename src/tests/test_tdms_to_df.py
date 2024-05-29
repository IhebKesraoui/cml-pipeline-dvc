import unittest
import os

class TestTdmsFiles(unittest.TestCase):

    def test_tdms_file_conditions(self):
        tdms_dir = "data"  # Assuming 'data' is the directory with TDMS files
        
        
        for file_name in os.listdir(tdms_dir):
            tdms_file_path = os.path.join(tdms_dir, file_name)
           
            
            if file_name.endswith(".tdms"):
                

                # Check if the file is not empty
                if os.path.getsize(tdms_file_path) > 0:
                    continue
                else:
                    print(f"{file_name} est vide")
                    self.fail(f"{file_name} est vide")  # Mark test as failed if file is empty
            else:
                print(f"{file_name} n'est pas un fichier TDMS")
                self.fail(f"{file_name} n'est pas un fichier TDMS")  # Mark test as failed if file is not TDMS

if __name__ == '__main__':
    unittest.main()
