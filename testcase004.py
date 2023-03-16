import unittest

# Definir uma função simples para testar
def somar(a, b):
    return a + b

# Definir uma classe de teste
class TestSomar(unittest.TestCase):
    
    # Definir um método de teste
    def test_somar(self):
        self.assertEqual(somar(2, 2), 4)
        self.assertEqual(somar(0, 0), 0)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(3.5, 1.5), 5)
        
# Executar os testes
if __name__ == '__main__':
    unittest.main()
