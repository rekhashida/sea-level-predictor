import unittest

import sea_level_predictor


class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        self.assertEqual(self.ax.get_title(), "Rise in Sea Level")

    def test_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Year")
        self.assertEqual(self.ax.get_ylabel(), "Sea Level (inches)")

    def test_plot_has_scatter_points(self):
        scatter_points = self.ax.collections[0].get_offsets()
        self.assertGreater(len(scatter_points), 100)

    def test_plot_has_two_lines(self):
        self.assertEqual(len(self.ax.get_lines()), 2)

    def test_lines_predict_to_2050(self):
        first_line_x = self.ax.get_lines()[0].get_xdata()
        second_line_x = self.ax.get_lines()[1].get_xdata()

        self.assertEqual(first_line_x[-1], 2050)
        self.assertEqual(second_line_x[-1], 2050)


if __name__ == "__main__":
    unittest.main()