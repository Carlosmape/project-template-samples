import unittest import #{MODULE}

class #{MODULE}_test(unittest.TestCase):

    @staticmethod
    def run_all():
        """Run all tests in the module"""
        unittest.main()

    def test(self):
        """Sample test, some module tests could be called from this one"""
        self.assertTrue(True)
        #mytestclass.run_all()


if __name__ == '__main__':
    #{MODULE}_test.run_all()
