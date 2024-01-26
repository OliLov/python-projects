"""Test dictionary."""
from test.assertions import is_eq


class TestDictionary:  # pylint: disable=too-few-public-methods
    """Test dictionary."""

    LONG_DICT = {
        "name": "Alice",
        "age": 30,
        "email": "alice@example.com",
        "address": "123, Maple Street, Wonderland",
        "phone": "123-456-7890",
        "occupation": "Engineer",
        "hobbies": ["reading", "cycling", "hiking"],
        "has_pet": True,
        "pet_details": {"pet_name": "Buddy", "pet_type": "Dog", "pet_age": 5},
        "favorite_books": {
            "fiction": "1984",
            "nonfiction": "Sapiens",
            "mystery": "Sherlock Holmes",
            "science fiction": "Dune",
        },
        "languages_spoken": ["English", "Spanish", "French"],
        "education": {
            "undergraduate": "Computer Science",
            "graduate": "Artificial Intelligence",
        },
        "skills": ["Python", "Machine Learning", "Data Analysis"],
        "membership": ["IEEE", "ACM"],
    }

    def test_dictionary(self):
        """Test dictionary."""
        long_dict_copy = self.LONG_DICT.copy()
        long_dict_copy["name"] = "Bob"

        is_eq(
            self.LONG_DICT,
            long_dict_copy,
            "The dictionaries shall be equal.",
            "The dictionaries are not equal!",
        )
