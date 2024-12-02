import pandas as pd
from BundesligaStats import LeagueStats
class BundesligaScrape:
    def __init__(self):
        pass
    def assign_values(self, data):
        # Create a dictionary mapping team names to logo paths
        logo_dict = {
            "Augsburg": r"BLogos\Augsburg.png",
            "Bayern Munich": r"BLogos\Bayern Munich.png",
            "Bochum": r"BLogos\Bochum.png",
            "Dortmund": r"BLogos\Dortmund.png",
            "Eint Frankfurt": r"BLogos\Eint Frankfurt.png",
            "Freiburg": r"BLogos\Freiburg.png",
            "Gladbach": r"BLogos\Gladbach.png",
            "Heidenheim": r"BLogos\Heidenheim.png",
            "Hoffenheim": r"BLogos\Hoffenheim.png",
            "Holstein Kiel": r"BLogos\Holstein Kiel.png",
            "Leverkusen": r"BLogos\Leverkusen.png",
            "Mainz 05": r"BLogos\Mainz 05.png",
            "RB Leipzig": r"BLogos\RB Leipzig.png",
            "St. Pauli": r"BLogos\St. Pauli.png",
            "Stuttgart": r"BLogos\Stuttgart.png",
            "Union Berlin": r"BLogos\Union Berlin.png", 
            "Werder Bremen": r"BLogos\Werder Bremen.png",
            "Wolfsburg": r"BLogos\Wolfsburg.png"
        }
        
        colors={
            "Bayern Munich":"#dc052d",
            "Bochum": "#ADD8E6",
            "Dortmund": "#ffd900",
            "RB Leipzig": "#001f47",
            "Eint Frankfurt": "#E1000F",
            "Freiburg": "#FD1220",
            "Gladbach": "#000000",
            "Heidenheim":"#e2001a",
            "Hoffenheim": "#1961B5",
            "Holstein Kiel": "#0F5787",
            "Leverkusen": "#E32221",
            "Mainz 05": "#C3141E",
            "RB Leipzig": "#DD0741",
            "St. Pauli": "#624839",
            "Stuttgart": "#E32219",
            "Union Berlin": "#EB1923",
            "Werder Bremen": "#009655",
            "Augsburg": "#ba3733",
            "Wolfsburg": "#52a600",
        }

        data["Colors"] = data["Squad"].map(colors)
        data["LogoPaths"] = data["Squad"].map(logo_dict)
        print(data["Colors"])
        print(data[["Rk","Squad"]])
        return data
    def scrape(self):
        try:
            url = "https://fbref.com/en/comps/20/Bundesliga-Stats"
            table_id = "results2024-2025201_overall"
            df_list = pd.read_html(url, attrs={"id": table_id})
            
            if df_list:
                df = df_list[0]
                df=self.assign_values(df)
                df.drop("Notes", axis=1, inplace=True)

                print(df.head())
                return df
                # Example usage of LeagueStats
                league_stats = LeagueStats(df)
                league_stats.highestXG()
            else:
                print(f"No tables found with id '{table_id}'")
        except Exception as e:
            print(f"An error occurred: {e}")