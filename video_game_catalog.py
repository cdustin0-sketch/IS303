from pathlib import Path

import pandas as pd


def main():
    # Using __file__ means the file can still be found if the program is
    # started from a different folder in the terminal.
    input_file = Path(__file__).resolve().parent / "video_games_raw.csv"

    # Read the original CSV into a Pandas DataFrame (a table of rows/columns).
    try:
        games = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Could not find {input_file.name} next to this program.")
        return

    # Ask for a row position. iloc uses positions beginning at 0, so position 0
    # is the first game, position 1 is the second, and so on.
    while True:
        row_text = input(
            f"Enter a row number to inspect (0 to {len(games) - 1}): "
        ).strip()

        try:
            row_number = int(row_text)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if 0 <= row_number < len(games):
            break

        print(f"Choose a row number from 0 to {len(games) - 1}.")

    # iloc selects a row by its position in the DataFrame.
    selected_game = games.iloc[row_number]

    print("\nSelected Game:")
    print(f"Title: {selected_game['Title']}")
    print(f"Platform: {selected_game['Platform']}")
    print(f"Genre: {selected_game['Genre']}")
    print(f"Rating: {selected_game['Rating']}")
    print(f"Current Status: {selected_game['Status']}")

    # Keep asking until the user enters one of the statuses listed in the
    # assignment. Case and extra spaces are normalized for easier input.
    valid_statuses = ["Backlog", "Playing", "Completed", "Dropped"]
    while True:
        new_status = input(
            "Enter a new status (Backlog, Playing, Completed, or Dropped): "
        ).strip().title()

        if new_status in valid_statuses:
            break

        print("Please enter Backlog, Playing, Completed, or Dropped.")

    # at changes one cell using its row index and column name.
    # read_csv creates row labels 0, 1, 2, ... so row_number is the label here.
    games.at[row_number, "Status"] = new_status

    # Start with every game marked No. The next two loc statements update
    # multiple rows at once for the games that meet both recommendation rules.
    games["Recommended"] = "No"

    meets_recommendation_rules = (games["Rating"] >= 8) & (games["Price"] <= 40)
    games.loc[meets_recommendation_rules, "Recommended"] = "Yes"

    # query filters the DataFrame using the Recommended column we just made.
    recommended_games = games.query("Recommended == 'Yes'")

    print("\nRecommended Games:")
    print(recommended_games[["Title", "Platform", "Price", "Rating"]])

    # Save to a new filename so the original raw CSV remains unchanged.
    output_file = Path(__file__).resolve().parent / "video_games_cleaned.csv"
    games.to_csv(output_file, index=False)

    print("\nThe catalog has been updated.")
    print(f"Saved as {output_file.name}.")


if __name__ == "__main__":
    main()
