import unittest
from plot_drawer import PlotDrawer

class TestPlotDrawer(unittest.TestCase):
    def test_draw_plots(self):
        drawer = PlotDrawer()
        plots = drawer.draw_plots('deviation.json')
        # Проверяем, что хотя бы один график был создан
        self.assertTrue(len(plots) > 0)

if __name__ == '__main__':
    unittest.main()
