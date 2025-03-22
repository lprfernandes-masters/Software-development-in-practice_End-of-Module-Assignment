
import unittest
import datetime
from src.models.models import Client, Flight, Airline


class TestModels(unittest.TestCase):
    def test_client_record(self):
        """Testing the client to_dict method"""
        client = Client(1, "Client", "Luis", "Addr1", "Addr2",
                        "Addr3", "City", "State", "Zip", "Country", "123456")
        data = client.to_dict()
        self.assertEqual(data["Name"], "Luis")
        client2 = Client.from_dict(data)
        self.assertEqual(client, client2)

    def test_airline_record(self):
        """Testing the airline to_dict method"""
        airline = Airline(1, "Airline", "Airline1")
        data = airline.to_dict()
        self.assertEqual(data["Company_Name"], "Airline1")
        airline2 = Airline.from_dict(data)
        self.assertEqual(airline, airline2)

    def test_flight_record(self):
        """Testing the flight to_dict method"""
        date_value = datetime.datetime(day=1, month=2, year=2025)
        flight = Flight(1, 1, date_value, "CityA", "CityB")
        data = flight.to_dict()
        self.assertEqual(data["Start_City"], "CityA")
        flight2 = Flight.from_dict(data)
        self.assertEqual(flight, flight2)


if __name__ == '__main__':
    unittest.main()
