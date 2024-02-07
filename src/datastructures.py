from random import randint

class FamilyStructure:

    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id": 1,
                "fist_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            { 
                "id": 2,
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            { 
                "id": 3,
                "fist_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": 1
            },

              { 
                "id": 4,
                "fist_name": "Alex",
                "last_name": self.last_name,
                "age": 34,
                "lucky_numbers": 17
            },
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)
        return self._members[0]

    def delete_member(self, id):
        members = self._members
        # Find member to delete
        for index, item in enumerate(members):
            if item["id"] == id:
                member_to_delete = index
        
        self._members.pop(member_to_delete)

        # fill this method and update the return
        return self._members


    def get_member(self, id):
        # fill this method and update the return
        members = self._members

        # Find member
        for index, item in enumerate(members):
            print(item)
            if item["id"] == id:
                member = index
                return self._members[member]
            else:
                return None
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members