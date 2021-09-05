import pytest as pytest

from libpythonmax.spam.enviador_de_email import Enviador
from libpythonmax.spam.main import EnviadorDeSpam
from libpythonmax.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Max', email='maxwneto.poo@gmail.com'),
            Usuario(nome='Heitor', email='heitorssneto@gmail.com')
        ],
        [
            Usuario(nome='Max', email='maxwneto.poo@gmail.com')

        ]
    ],
)
def test_qde_de_span(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'maxwneto.poo@gmail.com',
        'Programador Python',
        'Estou me tornando um programador Profissional.'
    )
    assert len(usuarios) == enviador.qtd_email_enviados