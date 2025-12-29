import pandas as pd

def update_mega_database():
    # روابط لمصادر بيانات عالمية ضخمة تغطي معظم دوريات العالم
    urls = [
        "https://www.football-data.co.uk/mmz4281/2425/E0.csv", # إنجلترا
        "https://www.football-data.co.uk/mmz4281/2425/SP1.csv", # إسبانيا
        "https://www.football-data.co.uk/mmz4281/2425/I1.csv",  # إيطاليا
        "https://www.football-data.co.uk/mmz4281/2425/D1.csv",  # ألمانيا
        "https://raw.githubusercontent.com/jokecamp/FootballData/master/nfl/nfl_2023.csv", # مثال لبيانات إضافية
        "https://www.football-data.co.uk/mmz4281/2425/F1.csv"   # فرنسا
    ]
    
    all_frames = []
    print("🌐 جاري اجتياح قواعد البيانات العالمية...")

    for url in urls:
        try:
            df = pd.read_csv(url)
            # توحيد الأعمدة لتناسب الواجهة: الدوري، المضيف، الضيف، أهداف هـ، أهداف ض، النتيجة، التاريخ
            # سنقوم بمحاولة ذكية لاستخراج الدوري من الرابط نفسه
            league_name = url.split('/')[-1].split('.')[0]
            
            temp_df = pd.DataFrame()
            temp_df['Div'] = [league_name] * len(df)
            temp_df['Home'] = df['HomeTeam']
            temp_df['Away'] = df['AwayTeam']
            temp_df['HG'] = df['FTHG']
            temp_df['AG'] = df['FTAG']
            temp_df['Res'] = df['FTR']
            temp_df['Date'] = df['Date']
            
            all_frames.append(temp_df)
        except Exception as e:
            print(f"⚠️ تخطي مصدر بسبب: {e}")

    if all_frames:
        final_db = pd.concat(all_frames, ignore_index=True)
        final_db.to_csv('updated_matches.csv', index=False)
        print(f"✅ تم تحديث النظام بـ {len(final_db)} مباراة من مختلف القارات!")

if __name__ == "__main__":
    update_mega_database()
