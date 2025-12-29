import pandas as pd
import requests

def update_global_data():
    # قائمة بأكواد الدوريات الموثوقة لضمان نجاح العملية
    codes = ["E0", "E1", "SP1", "SP2", "D1", "I1", "F1", "N1", "B1"]
    all_leagues = []
    
    print("🚀 جاري جلب البيانات العالمية...")
    for code in codes:
        try:
            # استخدام رابط ثابت لموسم 2023/2024 لضمان توفر البيانات حالياً
            url = f"https://www.football-data.co.uk/mmz4281/2324/{code}.csv"
            df = pd.read_csv(url)
            cols = ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']
            if all(c in df.columns for c in cols):
                all_leagues.append(df[cols])
                print(f"✅ تم جلب بيانات: {code}")
        except:
            continue

    if all_leagues:
        final_db = pd.concat(all_leagues, ignore_index=True)
        final_db.to_csv('updated_matches.csv', index=False)
        print("📊 تم تحديث قاعدة البيانات بنجاح!")
