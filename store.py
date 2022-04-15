from datetime import datetime


class Store:
    def __init__(self):
        self.incidents = []

    def add_incident(self, incident):
        self.incidents.append(incident)

    def incident_status(self, start_date, end_date):
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')

        open_cases = self.get_num_open_cases(start_date, end_date)
        closed_cases = self.get_num_solved_cases(start_date, end_date)
        average_solution = self.get_avg_solution_time(start_date, end_date)
        maximum_solution = self.get_max_solution_time(start_date, end_date)

        return {'open_cases': open_cases,
                'closed_cases': closed_cases,
                'average_solution': average_solution,
                'maximum_solution': maximum_solution}

    def get_num_open_cases(self, start_date, end_date):
        return len(list(filter(lambda incident: start_date <= incident.get_date_open() <= end_date, self.incidents)))

    def get_num_solved_cases(self, start_date, end_date):
        return len(list(
            filter(lambda incident: incident.get_status() == 'solved' and start_date <= incident.get_date_solved() <= end_date,
                   self.incidents)))

    def get_avg_solution_time(self, start_date, end_date):
        solved_cases = list(filter(
            lambda incident: incident.get_status() == 'solved' and start_date <= incident.get_date_solved() <= end_date,
            self.incidents))
        if len(solved_cases) != 0:
            return int(sum(map(lambda incident: (incident.get_date_solved() - incident.get_date_open()).total_seconds(),
                               solved_cases)) / len(solved_cases) / 3600)
        else:
            return 0

    def get_max_solution_time(self, start_date, end_date):
        closed_cases = list(filter(
            lambda incident: incident.get_status() == 'solved' and start_date <= incident.get_date_open()
                             and incident.get_date_solved() <= end_date, self.incidents))
        open_cases = list(filter(
            lambda incident: incident.get_status() == 'open' and start_date <= incident.get_date_open(),
            self.incidents))
        sol_time = list(map(lambda incident: (incident.get_date_solved() - incident.get_date_open()).total_seconds(),
                            closed_cases)) + \
                   list(map(lambda incident: (end_date - incident.get_date_open()).total_seconds(), open_cases))
        if len(sol_time) != 0:
            return int(max(sol_time) / 3600)
        else:
            return 0
