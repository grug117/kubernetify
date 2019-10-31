from unittest import TestCase
import kubernetify

class TestString(TestCase):
    def test_string_to_kubernetify(self):
        
        input = kubernetify.string("kubernetes")
        output = "k8s"
        self.assertTrue(input, output)