class Nestedtoflatner:
    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.flattened_list = []

    def flatten(self):
        for item in self.nested_list:
            if isinstance(item, list):
                sub_flattener = Nestedtoflatner(item)
                sub_flattener.flatten()
                self.flattened_list.extend(sub_flattener.flattened_list)
            else:
                self.flattened_list.append(item)


# Example
nested_list = [[1, 2, [3, 4]], [5, 6], [7, [8, 9, [10]]]]
flattener = Nestedtoflatner(nested_list)
flattener.flatten()
print(flattener.flattened_list)
