class Operation:
    @staticmethod
    def lower_string(content: str):
        return content.lower()

    @classmethod
    def upper_string(cls, content):
        cls.lower_string(content)

temp_str = "Hello World"
print(Operation.lower_string(temp_str))