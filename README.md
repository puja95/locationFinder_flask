# locationFinder_flask
Get all districts grouped by state from the table of MySQL DB.


API Details : 

/get_locations :  Get all districts grouped by state. METHOD : GET

Sample Response :

```
{
    "data": [
        {
            "districts": [
                {
                    "id": 1,
                    "name": "Bagalkot",
                    "pincode": 587101
                },
                {
                    "id": 2,
                    "name": "Bengaluru Rural",
                    "pincode": 560066
                }
            ],
            "state": "Karnataka"
        },
        {
            "districts": [
                {
                    "id": 3,
                    "name": "South 24 Parganas",
                    "pincode": 700008
                }
            ],
            "state": "West Bengal"
        }
    ]
}
```
