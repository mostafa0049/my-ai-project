import pandas as pd
import requests
import io

def update_2026_data():
    # روابط مباشرة لبيانات موسم 2025/2026 (تحدث يومياً)
    base_url = "https://www.football-data.co.uk/mmz4281/2526/"
    leagues = {
        "E0": "الدوري الإنجليزي الممتاز",
        "SP1": "الدوري الإسباني",
        "I1": "الدوري الإيطالي",
        "D1": "الدوري الألماني",
        "F1": "الدوري الفرنسي",
        "B1": "الدوري البلجيكي",
        "N1": "الدوري الهولندي"
    }

    all_data = []
    print("📡 جاري سحب بيانات موسم 2025-2026...")

    for code, name in leagues.items():
        try:
            url = f"{base_url}{code}.csv"
            df = pd.read_csv(url)
            # توحيد الأعمدة المطلوبة للتحليل الفعلي
            df = df[['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']]
            df.columns = ['Date', 'Home', 'Away', 'HG', 'AG', 'Res']
            df['League'] = name
            all_data.append(df)
            print(f"✅ تم تحديث: {name}")
        except:
            continue

    if all_data:
        final_db = pd.concat(all_data, ignore_index=True)
        # حفظ الملف الذي ستقرأه المنصة
        final_db.to_csv('updated_matches.csv', index=False)
        print(f"🎯 تم تجميع {len(final_db)} مباراة من الموسم الحالي.")

if __name__ == "__main__":
    update_2026_data()
