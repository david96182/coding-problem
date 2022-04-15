import unittest

from incident import Incident
from store import Store


class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store()

    def test_get_number_of_open_cases(self):
        test_incident_1 = Incident("solved", "test_inc_1", "2022-04-11 09:00:00", "2022-04-11 10:00:00")
        test_incident_2 = Incident("open", "test_inc_2", "2022-04-10 05:00:00")
        test_incident_3 = Incident("open", "test_inc_3", "2022-04-12 12:00:00")

        self.store.add_incident(test_incident_1)
        self.store.add_incident(test_incident_2)
        self.store.add_incident(test_incident_3)

        expected_result = 2
        self.assertEqual(self.store.incident_status("2022-04-11 09:00:00", "2022-04-12 12:00:00")['open_cases'],
                         expected_result)

    def test_get_solved_cases(self):
        test_incident_1 = Incident("solved", "test_inc_1", "2022-04-11 00:00:00", "2022-04-11 11:00:00")
        test_incident_2 = Incident("open", "test_inc_2", "2022-04-10 05:00:00")
        test_incident_3 = Incident("open", "test_inc_3", "2022-04-12 12:00:00")

        self.store.add_incident(test_incident_1)
        self.store.add_incident(test_incident_2)
        self.store.add_incident(test_incident_3)

        expected_result = 1
        self.assertEqual(self.store.incident_status("2022-04-10 04:00:00", "2022-04-12 03:00:00")['closed_cases'],
                             expected_result)

    def test_get_avg_solution(self):
        test_incident_1 = Incident("solved", "test_inc_1", "2022-04-11 01:00:00", "2022-04-11 03:00:00")
        test_incident_2 = Incident("solved", "test_inc_2", "2022-04-10 05:00:00", "2022-04-10 07:00:00")
        test_incident_3 = Incident("solved", "test_inc_3", "2022-04-12 08:00:00", "2022-04-12 10:00:00")

        self.store.add_incident(test_incident_1)
        self.store.add_incident(test_incident_2)
        self.store.add_incident(test_incident_3)

        expected_result = 2
        self.assertEqual(self.store.incident_status("2022-04-10 04:00:00", "2022-04-11 03:00:00")['average_solution'],
                         expected_result)

    def test_get_avg_solution_with_no_solved_cases(self):
        test_incident_1 = Incident("open", "test_inc_1", "2022-04-11 01:00:00")
        test_incident_2 = Incident("open", "test_inc_2", "2022-04-10 05:00:00")
        test_incident_3 = Incident("open", "test_inc_3", "2022-04-12 08:00:00")

        self.store.add_incident(test_incident_1)
        self.store.add_incident(test_incident_2)
        self.store.add_incident(test_incident_3)

        expected_result = 0
        self.assertEqual(self.store.incident_status("2022-04-10 04:00:00", "2022-04-11 03:00:00")['average_solution'],
                         expected_result)

    def test_get_max_solution(self):
        test_incident_1 = Incident("solved", "test_inc_1", "2022-04-11 01:00:00", "2022-04-12 03:00:00")
        test_incident_2 = Incident("solved", "test_inc_2", "2022-04-10 05:00:00", "2022-04-12 07:00:00")
        test_incident_3 = Incident("solved", "test_inc_3", "2022-04-12 08:00:00", "2022-04-12 10:00:00")

        self.store.add_incident(test_incident_1)
        self.store.add_incident(test_incident_2)
        self.store.add_incident(test_incident_3)

        expected_result = 50
        self.assertEqual(self.store.incident_status("2022-04-10 04:00:00", "2022-04-12 09:00:00")['maximum_solution'],
                         expected_result)

    def test_get_max_solution_with_no_solved_cases(self):
        test_incident_1 = Incident("open", "test_inc_1", "2022-04-11 01:00:00")
        test_incident_2 = Incident("open", "test_inc_2", "2022-04-10 05:00:00")
        test_incident_3 = Incident("open", "test_inc_3", "2022-04-12 08:00:00")

        self.store.add_incident(test_incident_1)
        self.store.add_incident(test_incident_2)
        self.store.add_incident(test_incident_3)

        expected_result = 52
        self.assertEqual(self.store.incident_status("2022-04-10 04:00:00", "2022-04-12 09:00:00")['maximum_solution'],
                         expected_result)


if __name__ == '__main__':
    unittest.main()
