# from csv import reader, DictWriter

# with open("scores1.csv", "w") as file:
#     headers = ["Name", "Score", "Date"]
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Name": "Raylin",
#         "Score": "77",
#         "Date": "06-Nov-2020"
#         })


from csv import reader, DictWriter

with open("scores1.csv", "w") as file:
    headers = ["Name", "Score", "Date"]
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writerow({
        "Name": "Raylin",
        "Score": "77",
        "Date": "06-Nov-2020"
        })
