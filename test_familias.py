import unittest
import familias


class TestCadastroFamilias(unittest.TestCase):

    def setUp(self):
        familias.familias.clear()

    def test_cadastrar_familia(self):
        resultado = familias.cadastrar_familia("Ana", "Centro")
        self.assertEqual(resultado, "Família cadastrada com sucesso!")
        self.assertEqual(len(familias.listar_familias()), 1)

    def test_nome_vazio(self):
        resultado = familias.cadastrar_familia("", "Centro")
        self.assertIn("Erro", resultado)
        self.assertEqual(len(familias.listar_familias()), 0)

    def test_bairro_vazio(self):
        resultado = familias.cadastrar_familia("Ana", "")
        self.assertIn("Erro", resultado)
        self.assertEqual(len(familias.listar_familias()), 0)

    def test_remover_espacos(self):
        familias.cadastrar_familia("  Ana  ", "  Centro  ")
        self.assertEqual(
            familias.listar_familias()[0]["nome"], "Ana"
        )


if __name__ == "__main__":
    unittest.main()
