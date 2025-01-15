import unittest

from entities.Consolidado import Consolidado
from services.dataframeService import gerar_dataframe


class TestConsolidadoComDadosReais(unittest.TestCase):
    def setUp(self):
        # Inicialize o Consolidado com um DataFrame real
        self.dataframe = gerar_dataframe(r"C:\Users\Lucas Martins\Downloads\50200709000109_Estoque_MOOVPAY FIDC - SUBORDINADA.zip")
        self.consolidado = Consolidado(self.dataframe)

    def test_valores_consolidados_movpay(self):
        # Valores esperados fornecidos
        valores_esperados = {
            "a_vencer": 8554149.79,
            "vencido": 4597256.46,
            "total": 13151406.25,
            "pdd": 4085168.30,
            "ticket_medio_aquisicao_a_vencer": 32.16,
            "ticket_medio_aquisicao_vencido": 40.45,
            "ticket_medio_aquisicao_total": 34.58,
            "ticket_medio_atual_a_vencer": 35.35,
            "ticket_medio_atual_vencido": 46.03,
            "ticket_medio_atual_total": 38.47,
            "ticket_medio_nominal_a_vencer": 39.95,
            "ticket_medio_nominal_vencido": 46.03,
            "ticket_medio_nominal_total": 41.72,
            "ultima_quinzena_ticket_medio_aquisicao_a_vencer": 33.16,
            "ultima_quinzena_ticket_medio_aquisicao_vencido": 120.39,
            "ultima_quinzena_ticket_medio_aquisicao_total": 33.33,
            "ultima_quinzena_ticket_medio_atual_a_vencer": 34.17,
            "ultima_quinzena_ticket_medio_atual_vencido": 146.91,
            "ultima_quinzena_ticket_medio_atual_total": 34.39,
            "ultima_quinzena_ticket_medio_nominal_a_vencer": 40.47,
            "ultima_quinzena_ticket_medio_nominal_vencido": 146.91,
            "ultima_quinzena_ticket_medio_nominal_total": 40.68,
            "quantidade_titulos_a_vencer": 241982,
            "quantidade_titulos_vencido": 99885,
            "quantidade_titulos_total": 341867,
            "total_cedentes": 1,
            "total_sacados": 47604,
            "a_vencer_ate_15": 3228042.67,
            "a_vencer_16_a_30": 1318812.43,
            "a_vencer_31_a_60": 2432365.05,
            "a_vencer_61_a_90": 1146127.45,
            "a_vencer_91_a_120": 305713.25,
            "a_vencer_121_a_150": 76001.23,
            "a_vencer_151_a_180": 46319.91,
            "a_vencer_181_a_365": 767.80,
            "a_vencer_acima_365": None,  # Ou qualquer valor esperado.
            "vencido_ate_15": 786144.91,
            "vencido_16_a_30": 595713.56,
            "vencido_31_a_60": 803123.17,
            "vencido_61_a_90": 287177.89,
            "vencido_91_a_120": 231561.15,
            "vencido_121_a_150": 498363.55,
            "vencido_151_a_180": 456672.49,
            "vencido_181_a_365": 938499.74,
            "vencido_acima_365": None,  # Ou qualquer valor esperado.
        }
        # Verificações
        self.assertEqual(round(self.consolidado.a_vencer,2),  valores_esperados["a_vencer"], "Erro em 'a_vencer'")
        self.assertEqual(round(self.consolidado.vencido,2), valores_esperados["vencido"], "Erro em 'vencido'")
        self.assertEqual(round(self.consolidado.total,2), valores_esperados["total"], "Erro em 'total'")
        self.assertEqual(round(self.consolidado.pdd, valores_esperados["pdd"],2), "Erro em 'pdd'")
        self.assertEqual(self.consolidado.ticket_medio_aquisicao_a_vencer,valores_esperados["ticket_medio_aquisicao_a_vencer"],"Erro em 'ticket_medio_aquisicao_a_vencer'")
        self.assertEqual(self.consolidado.ticket_medio_aquisicao_vencido,valores_esperados["ticket_medio_aquisicao_vencido"],"Erro em 'ticket_medio_aquisicao_vencido'")
        self.assertEqual(self.consolidado.ticket_medio_aquisicao_total,valores_esperados["ticket_medio_aquisicao_total"], "Erro em 'ticket_medio_aquisicao_total'")
        self.assertEqual(self.consolidado.ticket_medio_atual_a_vencer, valores_esperados["ticket_medio_atual_a_vencer"],"Erro em 'ticket_medio_atual_a_vencer'")
        self.assertEqual(self.consolidado.ticket_medio_atual_vencido, valores_esperados["ticket_medio_atual_vencido"],"Erro em 'ticket_medio_atual_vencido'")
        self.assertEqual(self.consolidado.ticket_medio_atual_total, valores_esperados["ticket_medio_atual_total"],"Erro em 'ticket_medio_atual_total'")
        self.assertEqual(self.consolidado.ticket_medio_nominal_a_vencer,valores_esperados["ticket_medio_nominal_a_vencer"], "Erro em 'ticket_medio_nominal_a_vencer'")
        self.assertEqual(self.consolidado.ticket_medio_nominal_vencido,valores_esperados["ticket_medio_nominal_vencido"], "Erro em 'ticket_medio_nominal_vencido'")
        self.assertEqual(self.consolidado.ticket_medio_nominal_total, valores_esperados["ticket_medio_nominal_total"],"Erro em 'ticket_medio_nominal_total'")
        self.assertEqual(self.consolidado.ultima_quinzena_ticket_medio_aquisicao_a_vencer,valores_esperados["ultima_quinzena_ticket_medio_aquisicao_a_vencer"],"Erro em 'ultima_quinzena_ticket_medio_aquisicao_a_vencer'")
        self.assertEqual(self.consolidado.ultima_quinzena_ticket_medio_aquisicao_vencido,valores_esperados["ultima_quinzena_ticket_medio_aquisicao_vencido"],"Erro em 'ultima_quinzena_ticket_medio_aquisicao_vencido'")
        self.assertEqual(self.consolidado.ultima_quinzena_ticket_medio_aquisicao_total,valores_esperados["ultima_quinzena_ticket_medio_aquisicao_total"],"Erro em 'ultima_quinzena_ticket_medio_aquisicao_total'")
        self.assertEqual(self.consolidado.ultima_quinzena_ticket_medio_atual_a_vencer,valores_esperados["ultima_quinzena_ticket_medio_atual_a_vencer"],"Erro em 'ultima_quinzena_ticket_medio_atual_a_vencer'")
        self.assertEqual(self.consolidado.ultima_quinzena_ticket_medio_atual_vencido,valores_esperados["ultima_quinzena_ticket_medio_atual_vencido"],"Erro em 'ultima_quinzena_ticket_medio_atual_vencido'")
        self.assertEqual(self.consolidado.ultima_quinzena_ticket_medio_atual_total,valores_esperados["ultima_quinzena_ticket_medio_atual_total"],"Erro em 'ultima_quinzena_ticket_medio_atual_total'")
        self.assertEqual(self.consolidado.ultima_quinzena_ticket_medio_nominal_a_vencer,valores_esperados["ultima_quinzena_ticket_medio_nominal_a_vencer"],"Erro em 'ultima_quinzena_ticket_medio_nominal_a_vencer'")
        self.assertEqual(self.consolidado.ultima_quinzena_ticket_medio_nominal_vencido,valores_esperados["ultima_quinzena_ticket_medio_nominal_vencido"],"Erro em 'ultima_quinzena_ticket_medio_nominal_vencido'")
        self.assertEqual(self.consolidado.ultima_quinzena_ticket_medio_nominal_total,valores_esperados["ultima_quinzena_ticket_medio_nominal_total"],"Erro em 'ultima_quinzena_ticket_medio_nominal_total'")
        self.assertEqual(self.consolidado.quantidade_titulos_a_vencer, valores_esperados["quantidade_titulos_a_vencer"],"Erro em 'quantidade_titulos_a_vencer'")
        self.assertEqual(self.consolidado.quantidade_titulos_vencido, valores_esperados["quantidade_titulos_vencido"],"Erro em 'quantidade_titulos_vencido'")
        self.assertEqual(self.consolidado.quantidade_titulos_total, valores_esperados["quantidade_titulos_total"],"Erro em 'quantidade_titulos_total'")
        self.assertEqual(self.consolidado.total_cedentes, valores_esperados["total_cedentes"],"Erro em 'total_cedentes'")
        self.assertEqual(self.consolidado.total_sacados, valores_esperados["total_sacados"], "Erro em 'total_sacados'")
        self.assertEqual(self.consolidado.a_vencer_ate_15, valores_esperados["a_vencer_ate_15"],"Erro em 'a_vencer_ate_15'")
        self.assertEqual(self.consolidado.a_vencer_16_a_30, valores_esperados["a_vencer_16_a_30"],"Erro em 'a_vencer_16_a_30'")
        self.assertEqual(self.consolidado.a_vencer_31_a_60, valores_esperados["a_vencer_31_a_60"],"Erro em 'a_vencer_31_a_60'")
        self.assertEqual(self.consolidado.a_vencer_61_a_90, valores_esperados["a_vencer_61_a_90"],"Erro em 'a_vencer_61_a_90'")
        self.assertEqual(self.consolidado.a_vencer_91_a_120, valores_esperados["a_vencer_91_a_120"],"Erro em 'a_vencer_91_a_120'")
        self.assertEqual(self.consolidado.a_vencer_121_a_150, valores_esperados["a_vencer_121_a_150"],"Erro em 'a_vencer_121_a_150'")
        self.assertEqual(self.consolidado.a_vencer_151_a_180, valores_esperados["a_vencer_151_a_180"],"Erro em 'a_vencer_151_a_180'")
        self.assertEqual(self.consolidado.a_vencer_181_a_365, valores_esperados["a_vencer_181_a_365"],"Erro em 'a_vencer_181_a_365'")
        self.assertEqual(self.consolidado.vencido_ate_15, valores_esperados["vencido_ate_15"],"Erro em 'vencido_ate_15'")
        self.assertEqual(self.consolidado.vencido_16_a_30, valores_esperados["vencido_16_a_30"],"Erro em 'vencido_16_a_30'")
        self.assertEqual(self.consolidado.vencido_31_a_60, valores_esperados["vencido_31_a_60"],"Erro em 'vencido_31_a_60'")

    if __name__ == "__main__":
        unittest.main()