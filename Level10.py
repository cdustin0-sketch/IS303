from pathlib import Path

import pandas as pd


def main():
    # Build the CSV path from this script's location. This still works when
    # the program is started from a different folder in the terminal.
    csv_path = Path(__file__).resolve().parent / "cfb.csv"

    try:
        data = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"Could not find cfb.csv in {csv_path.parent}.")
        return

    # Check the required headings before using them, so a differently
    # formatted CSV gets a helpful message instead of a confusing error.
    required_columns = {"Season", "Team", "Win"}
    missing_columns = required_columns - set(data.columns)
    if missing_columns:
        missing_list = ", ".join(sorted(missing_columns))
        print(f"The CSV is missing required column(s): {missing_list}")
        return

    # Remove surrounding spaces so input like " 2020 " is accepted.
    season = input("Enter a season to analyze: ").strip()
    if not season:
        print("Please enter a season.")
        return

    # Comparing text values accepts seasons whether Pandas read them as
    # numbers or text, while avoiding hard-coded season choices.
    season_data = data[data["Season"].astype(str).str.strip() == season]

    if season_data.empty:
        print(f"Season {season} was not found in cfb.csv.")
        return

    # Convert the selected Pandas rows into regular Python dictionaries.
    # Each record will look like {"Season": 2020, "Team": "...", "Win": 10, ...}.
    # Keeping these records in a list makes each team's values easy to access.
    team_records = season_data.to_dict(orient="records")

    # The if/elif order makes the ranges separate, so each team is listed once.
    categories = {
        "10 or more wins:": [],
        "8–9 wins:": [],
        "6–7 wins:": [],
        "Fewer than 6 wins:": [],
    }

    # Read the team name and wins from each record, and add the team to the appropriate category.
    for team in team_records:
        # Convert the win count safely; skip incomplete or invalid rows rather
        # than stopping the whole program because of one bad value.
        wins_value = pd.to_numeric(team["Win"], errors="coerce")
        if pd.isna(wins_value):
            continue
        wins = int(wins_value)
        name = team["Team"]

        # Ignore rows without a team name 
        if pd.isna(name) or not str(name).strip():
            continue
        name = str(name).strip()

        if wins >= 10:
            categories["10 or more wins:"].append(name)
        elif wins >= 8:
            categories["8–9 wins:"].append(name)
        elif wins >= 6:
            categories["6–7 wins:"].append(name)
        else:
            categories["Fewer than 6 wins:"].append(name)

    print(f"\nCollege Football Results for {season}")
    for category, teams in categories.items():
        print(category)
        if teams:
            for name in teams:
                print(name)
        else:
            print("No teams in this category.")
        print()


if __name__ == "__main__":
    main()
