import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        run_1 = runner.Runner('Бегун_1')
        for _ in range(10):
            run_1.walk()
        self.assertEqual(run_1.distance, 50)

    def test_run(self):
        run_2 = runner.Runner('Бегун_2')
        for _ in range(10):
            run_2.run()
        self.assertEqual(run_2.distance, 100)

    def test_challenge(self):
        run_1 = runner.Runner('Бегун_1')
        run_2 = runner.Runner('Бегун_2')
        for _ in range(10):
            run_1.walk()
            run_2.run()
        self.assertNotEqual(run_1.distance, run_2.distance)


if __name__ == '__main__':
    unittest.main()
