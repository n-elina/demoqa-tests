import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    year: str
    month: str
    day: str
    subject: str
    hobby: str
    photo: str
    address: str
    state: str
    city: str


kos = User(
    'Kos',
    'Ckogann',
    'email@gmail.com',
    'Male',
    '1234567890',
    '1990',
    'June',
    '06',
    'Computer Science',
    'Sports',
    'reference.png',
    'Bosanska Street 60',
    'NCR',
    'Delhi',
)
