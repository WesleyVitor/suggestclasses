import django
django.setup()
from core.bo.discentes import get_discentes, get_discente_by_matricula, get_discentes_ativos
from core.tests.povoar_testes import criar_dados, remover_dados

from django.test import TestCase


class ATests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        print('\nTeste A')
        criar_dados()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        remover_dados()

    def test_get_discentes_by_matricula(self):
        discente = get_discente_by_matricula(20209876543)
        self.assertIsNotNone(discente, 'Discente não é None?')
        discentes = get_discentes_ativos()
        self.assertTrue(len(discentes) > 0, 'Existe pelo menos um discente')
