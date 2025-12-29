import pandas as pd
import requests

def update_global_data():
    # قائمة بجميع الأكواد للدوريات العالمية (أكثر من 20 دوري)
    codes = [
        "E0", "E1", "E2", "E3", "EC", "D1", "D2", "SP1", "SP2", 
        "I1", "I2", "F1", "F2", "N1", "B1", "P1", "T1", "G1", "SC0"
    ]
    
    all_leagues = []
    print("🚀 بدء المسح الشامل للمباريات...")

    for code in codes:
        # سحب بيانات موسم 2025/2026 الحالي
        url = f"https://www.football-data.co.uk/mmz4281/2526/{code}.csv"
        try:
            df = pd.read_csv(url)
            # اختيار البيانات التي يحتاجها الذكاء الاصطناعي فقط
            cols = ['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']
            if all(c in df.columns for c in cols):
                all_leagues.append(df[cols])
                print(f"✅ تم جلب دوري: {code}")
        except:
            continue

    if all_leagues:
        # دمج كل البطولات في ملف واحد
        final_db = pd.concat(all_leagues, ignore_index=True)
        final_db.to_csv('updated_matches.csv', index=False)
        print("📊 اكتمل التحديث لكل العالم!")

if __name__ == "__main__":
    update_global_data()
