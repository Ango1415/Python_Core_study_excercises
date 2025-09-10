"""
Design pattern that uses factory methods to create objects that are used in another method
"""
from abc import ABC, abstractmethod

class Resource(ABC):
    @abstractmethod
    def reference(self, topic):
        pass

class Textbook(Resource):
    def __init__(self):
        self.index= {'Object-oriented Programming': ['Inheritance', 'Classes', 'Overriding', 'Overloading']}

    def reference(self, topic):
        print(f"Referencing {topic} using a textbook")
        return self.index.get(topic)

class Blog(Resource):
    def __init__(self):
        self.index= {'Object-oriented Programming': ['Inheritance', 'Classes', 'Overriding', 'Overloading']}

    def reference(self, topic):
        print(f"Referencing {topic} using a blog")
        return self.index.get(topic)

class Video(Resource):
    def __init__(self):
        self.index= {'Object-oriented Programming': ['Inheritance', 'Classes', 'Overriding', 'Overloading']}

    def reference(self, topic):
        print(f"Referencing {topic} using a video")
        return self.index.get(topic)

class Student:
    def __init__(self, name):
        self.name = name

    # Factory method to return Resource
    def _get_resource(self, resource_type):
        if resource_type == 'Textbook':
            return Textbook()
        elif resource_type == 'Blog':
            return Blog()
        elif resource_type == 'Video':
            return Video()
        else:
            raise ValueError('Invalid resource type, check one that is actually available')

    def explore_topic(self, resource_type, topic):
        resource = self._get_resource(resource_type)
        return resource.reference(topic)

    """ One possible implementation
    def explore_topic(self, resource_type, topic):
        if resource_type == 'Textbook':
            textbook = Textbook()   # Creating an instance of class implementing Resource
            textbook.reference(topic)

        elif resource_type == 'Blog':
            blog = Blog()   # Creating an instance of class implementing Resource
            blog.reference(topic)

        elif resource_type == 'Video':
            video = Video()   # Creating an instance of class implementing Resource
            video.reference(topic)
    """

student = Student('Pedro')
try:
    student.explore_topic('Textbook', 'Object-oriented Programming')
    student.explore_topic('Blog', 'Object-oriented Programming')
    student.explore_topic('Internet', 'Object-oriented Programming')
except ValueError as ve:
    print(ve)