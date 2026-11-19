import unittest
from unittest.mock import AsyncMock, Mock, patch

import rastreo


class RastreoTest(unittest.IsolatedAsyncioTestCase):
    async def test_originales_no_se_rastrean_ni_escriben(self):
        originales = [s for s in rastreo.SITIOS if s.get('original')]
        self.assertEqual({s['slug'] for s in originales}, {'crix', 'launchkit', 'cauce'})
        for sitio in originales:
            with self.subTest(slug=sitio['slug']), patch.object(rastreo, 'RAIZ') as raiz:
                nav, sem = Mock(), AsyncMock()
                await rastreo.uno(nav, sitio, sem)
                sem.__aenter__.assert_not_called()
                nav.new_context.assert_not_called()
                raiz.__truediv__.assert_not_called()

    async def test_webs_publicas_siguen_entrando_al_crawl(self):
        for sitio in ({'slug': 'ejemplo'}, {'slug': 'ejemplo', 'original': False}):
            with self.subTest(sitio=sitio):
                sem = AsyncMock()
                sem.__aenter__.side_effect = RuntimeError('entrada al crawl')
                with self.assertRaisesRegex(RuntimeError, 'entrada al crawl'):
                    await rastreo.uno(Mock(), sitio, sem)
                sem.__aenter__.assert_awaited_once()


if __name__ == '__main__':
    unittest.main()
