schema = {
    "title": "Floor Access Event",
    "type": "object",
    "properties": {
        "person_id": {
            "type": "string"
        },
        "datetime": {
            "type": "string",
            "format": "date-time"
        },
        "floor_level": {
            "type": "integer"
        },
        "building": {
            "type": "string"
        }
    },
    "required": ["person_id", "datetime", "floor_level", "building"]
}
