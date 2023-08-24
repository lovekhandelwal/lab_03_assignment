## My Python Code
class FlightTable:
    def __init__(self):
        self.matches = []
        
    def add_match(self, location, team1, team2, timing):
        self.matches.append({
            "location": location,
            "team1": team1,
            "team2": team2,
            "timing": timing
        })
        
    def search_by_team(self, team_name):
        team_matches = []
        for match in self.matches:
            if team_name in (match["team1"], match["team2"]):
                team_matches.append(match)
        return team_matches
        
    def search_by_location(self, location_name):
        location_matches = []
        for match in self.matches:
            if match["location"] == location_name:
                location_matches.append(match)
        return location_matches
        
    def search_by_timing(self, timing_type):
        timing_matches = []
        for match in self.matches:
            if match["timing"] == timing_type:
                timing_matches.append(match)
        return timing_matches
        
def main():
    flight_table = FlightTable()
    
    flight_table.add_match("Mumbai", "India", "Sri Lanka", "DAY")
    flight_table.add_match("Delhi", "England", "Australia", "DAY-NIGHT")
    flight_table.add_match("Chennai", "India", "South Africa", "DAY")
    flight_table.add_match("Indore", "England", "Sri Lanka", "DAY-NIGHT")
    flight_table.add_match("Mohali", "Australia", "South Africa", "DAY-NIGHT")
    flight_table.add_match("Delhi", "India", "Australia", "DAY")
    
    while True:
        print("Choose search parameter:")
        print("1. List of all matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")
        
        choice = int(input())
        
        if choice == 1:
            team_name = input("Enter team name: ")
            team_matches = flight_table.search_by_team(team_name)
            for match in team_matches:
                print(match)
        elif choice == 2:
            location_name = input("Enter location name: ")
            location_matches = flight_table.search_by_location(location_name)
            for match in location_matches:
                print(match)
        elif choice == 3:
            timing_type = input("Enter timing type: ")
            timing_matches = flight_table.search_by_timing(timing_type)
            for match in timing_matches:
                print(match)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
