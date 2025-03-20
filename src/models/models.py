from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Client:
    ID: int = None
    Type: str = "Client"
    Name: str = ""
    Address_Line_1: str = ""
    Address_Line_2: str = ""
    Address_Line_3: str = ""
    City: str = ""
    State: str = ""
    Zip_Code: str = ""
    Country: str = ""
    Phone_Number: str = ""

    def to_dict(self):
        """Convert the Client instance to a dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Client instance from a dictionary."""
        return cls(**data)


@dataclass
class Airline:
    ID: int = None
    Type: str = "Airline"
    Company_Name: str = ""

    def to_dict(self):
        """Convert the Airline instance to a dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        """Create an Airline instance from a dictionary."""
        return cls(**data)


@dataclass
class Flight:
    Client_ID: int = None
    Airline_ID: int = None
    Date: datetime = None
    Start_City: str = ""
    End_City: str = ""

    def to_dict(self):
        """
        Convert the Flight instance to a dictionary.
        """
        data = asdict(self)
        if self.Date:
            data['Date'] = self.Date.isoformat()
        return data

    @classmethod
    def from_dict(cls, data: dict):
        """
        Create a Flight instance from a dictionary.
        """
        if data.get("Date"):
            data["Date"] = datetime.fromisoformat(data["Date"])
        return cls(**data)
