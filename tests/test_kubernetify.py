import unittest
from kubernetify.kubernetify import kubernetify

class TestString(unittest.TestCase):
    def test_kubernetify_returns_K8s_from_kubernetes(self):
        expected_output = "K8s"
        actual_output = kubernetify("kubernetes")
        
        self.assertTrue(expected_output, actual_output)

if __name__ == "__main__":
    unittest.main()
