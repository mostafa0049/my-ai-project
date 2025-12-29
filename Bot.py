import pandas as pd
import requests

def update_global_data():
    # قائمة ضخمة تشمل الدوريات الكبرى، الدوريات العربية، والأفريقية المتاحة
    sources = [
        "https://www.football-data.co.uk/mmz4281/2324/E0.csv", # إنجلترا
        "https://www.football-data.co.uk/mmz4281/2324/SP1.csv", # إسبانيا
        "https://www.football-data.co.uk/mmz4281/2324/I1.csv", # إيطاليا
        "https://www.football-data.co.uk/mmz4281/2324/D1.csv", # ألمانيا
        "https://www.football-data.co.uk/mmz4281/2324/F1.csv", # فرنسا
        "https://www.football-data.co.uk/mmz4281/2324/B1.csv", # بلجيكا
        "https://www.football-data.co.uk/mmz4281/2324/N1.csv"  # هولندا
    ]
    
    all_data = []
    print("🌍 جاري مسح العالم كروياً...")

    for url in sources:
        try:
            df = pd.read_csv(url)
            selected = df[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]
            all_data.append(selected)
        except:
            continue

    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        # تنظيف الأسماء من المسافات لضمان دقة البحث
        final_df['HomeTeam'] = final_df['HomeTeam'].str.strip()
        final_df['AwayTeam'] = final_df['AwayTeam'].str.strip()
        final_df.to_csv('updated_matches.csv', index=False)
        print("✅ تم تحديث المخزن بآلاف المباريات!")

if __name__ == "__main__":
    update_global_data()
