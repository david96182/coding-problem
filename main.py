from store import Store
from incident import Incident

if __name__ == '__main__':
    some_store = Store()

    incident_1 = Incident('solved', 'Incident 1', '2022-04-10 00:00:00', '2022-04-12 00:00:00')
    some_store.add_incident(incident_1)

    incident_2 = Incident('open', 'Incident 2', '2022-04-12 00:00:00')
    some_store.add_incident(incident_2)

    incident_3 = Incident('solved', 'Incident 3', '2022-04-10 00:00:00', '2022-04-13 00:00:00')
    some_store.add_incident(incident_3)

    incident_4 = Incident('open', 'Incident 4', '2022-04-11 00:00:00')
    some_store.add_incident(incident_4)

    incident_5 = Incident('open', 'Incident 5', '2022-04-12 00:00:00')
    some_store.add_incident(incident_5)

    incident_6 = Incident('solved', 'Incident 6', '2022-04-12 00:00:00', '2022-04-13 00:00:00')
    some_store.add_incident(incident_6)

    incident_7 = Incident('solved', 'Incident 7', '2022-04-11 00:00:00', '2022-04-13 00:00:00')
    some_store.add_incident(incident_7)

    incident_8 = Incident('solved', 'Incident 8', '2022-04-13 00:00:00', '2022-04-13 00:00:00')
    some_store.add_incident(incident_8)

    print(some_store.incident_status('2022-04-10 00:00:00', '2022-04-13 00:00:00'))
