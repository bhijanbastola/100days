"""    Write a recursive function called flatten_dict that takes a deeply nested Python dictionary and flattens it. The keys of the flattened dictionary should represent the dot-separated path to the values.

nested_data
    "user": "Alice",
    "profile": {
        "info": {
            "age": 30,
            "city": "Denver"
        },
        "tags": ["admin", "developer"]
    },
    "settings": {
        "theme": "dark"
    }
}
Excepted Dict:

{
    "user": "Alice",
    "profile.info.age": 30,
    "profile.info.city": "Denver",
    "profile.tags.0": "admin",
    "profile.tags.1": "developer",
    "settings.theme": "dark"
}"""


    
