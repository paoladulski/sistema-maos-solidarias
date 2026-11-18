
# Protótipo inicial do cadastro de famílias
# Sistema Mãos Solidárias

familias = []

def cadastrar_familia(nome, bairro):
    if not nome.strip() or not bairro.strip():
        return "Erro: nome e bairro são obrigatórios."

    familia = {
        "nome": nome.strip(),
        "bairro": bairro.strip()
    }

    familias.append(familia)
    return "Família cadastrada com sucesso!"


def listar_familias():
    return familias
