class User:
    def __init__(self, name, user_id):
        self._name = name
        self._user_id = user_id

    def __repr__(self):
        return f'{self._name}, {self._user_id}'

    @property
    def name(self):         #Getter public: name, private: _name
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @name.deleter
    def name(self):
        self._name = ""


u1 = User('Nils', 123)
print(u1)
u1.name = 'Cornelius'
print(u1)

