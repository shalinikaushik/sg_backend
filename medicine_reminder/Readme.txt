#######################################################################################
Medicine List

curl -X GET \
  'http://localhost:3000/cbtbiitr/chikitsa/medicines?name=' \
  -H 'Authorization: Token cb6a5cef4202f79165019847137303d231319aae' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \'

Output:
[
    {
        "pk": 1,
        "name": "Dispirin",
        "compunds": "12xcv345"
    },
    {
        "pk": 2,
        "name": "Crocin",
        "compunds": "1 2 3 4 5 6 7"
    },
    {
        "pk": 3,
        "name": "Medicine 3",
        "compunds": "123"
    },
    {
        "pk": 4,
        "name": "medicine 4",
        "compunds": "1234"
    }
]
########################################################################################
Medicine data

curl -X GET \
  http://localhost:3000/cbtbiitr/chikitsa/medicine/data/1 \
  -H 'Authorization: Token cb6a5cef4202f79165019847137303d231319aae' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \

Output:
{
    "pk": 1,
    "name": "Dispirin",
    "compunds": "12xcv345",
    "medicine_Image": "123456qwerty"
}
###########################################################################################
Reminder data

curl -X GET \
  http://localhost:3000/cbtbiitr/chikitsa/reminder/data/1 \
  -H 'Authorization: Token cb6a5cef4202f79165019847137303d231319aae' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \

Output:

{
    "pk": 1,
    "medicine_detail": [
        {
            "pk": 1,
            "name": "Dispirin",
            "compunds": "12xcv345"
        }
    ],
    "number_of_times_to_take_day": 1,
    "number_of_times_to_take_week": 7,
    "patient_id": 1,
    "timings_of_intake": "2018-07-03T12:10:08+05:30",
    "time_gap": "2.0"
}

############################################################################################
Doctor Details

curl -X GET \
  http://localhost:3000/cbtbiitr/chikitsa/doctor/1 \
  -H 'Authorization: Token cb6a5cef4202f79165019847137303d231319aae' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \

Output:

{
    "pk": 1,
    "doctor_id": 1,
    "patients": [
        {
            "pk": 1,
            "name": "Sahil Sharma",
            "date_of_birth": 0,
            "gender": 1
        },
        {
            "pk": 3,
            "name": "shalini",
            "date_of_birth": 5,
            "gender": 2
        }
    ]
}

############################################################################################
Patient Details

curl -X GET \
  http://localhost:3000/cbtbiitr/chikitsa/patient/1 \
  -H 'Authorization: Token cb6a5cef4202f79165019847137303d231319aae' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \

Output:
{
    "pk": 1,
    "patient_id": 1,
    "next_visit": "2018-07-03T00:16:46+05:30",
    "doctor_comments": "he has high fever bro",
    "problems_faced": "depression and headache",
    "all_medicines": [
        {
            "pk": 1,
            "name": "Dispirin",
            "compunds": "12xcv345"
        }
    ]
}
