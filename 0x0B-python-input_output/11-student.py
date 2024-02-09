#!/usr/bin/python3

class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student
        instance with optional filtering.
        """
        if attrs is None:
            return self.__dict__

        filtered_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                filtered_dict[attr] = getattr(self, attr)
        """
        Return:
        {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        """
        return filtered_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance."""
        for key, value in json.items():
            setattr(self, key, value)
