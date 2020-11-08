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
from operator import itemgetter

# with open("scores1.csv", "w") as file:
#     headers = ["Name", "Score", "Date"]
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writerow({
#         "Name": "Raylin",
#         "Score": "77",
#         "Date": "06-Nov-2020"
#         })


with open("scores1.csv") as file:
        csv_reader = reader(file)
        # skips the frist row so headers are not printed on the scores
        next(csv_reader)
        # create the scores screen
        print("\n*****************TOP FIVE PLAYERS***************")
        print("*****Player****    ****Score****   \t****Date*****\n")
        # sorts the scores list in descending order
        scores = sorted(csv_reader, reverse=True, key=itemgetter(1))
        print(scores)
        # slices scores list with onlu top five scores
        top = scores[0:5]
        for t in top:
            print(f"{t[0]}\t\t\t{t[1]}\t\t{t[2]}")

        input("\nPress 'enter' to play Dice Game")
