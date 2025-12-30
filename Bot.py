import pandas as pd
import requests
import io

def update_current_season_bot():
    # روابط مخصصة لموسم 2025/2026 الحالي
    # هذه الروابط يتم تحديثها فورياً بعد نهاية كل مباراة في الدوريات الكبرى
    base_url = "https://www.football-data.co.uk/mmz4281/2526/" 
    
    leagues = ["E0", "SP1", "I1", "D1", "F1", "N1", "P1"] # إنجلترا، إسبانيا، إيطاليا، ألمانيا، فرنسا، هولندا، البرتغال
    
    all_current_matches = []
    print("📅 جاري سحب بيانات موسم 2025-2026 المباشرة...")

    for league in leagues:
        try:
            url = f"{base_url}{league}.csv"
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                df = pd.read_csv(io.StringIO(response.text))
                
                # توحيد الأعمدة للمحرك
                df = df.rename(columns={
                    'HomeTeam': 'Home', 'AwayTeam': 'Away', 
                    'FTHG': 'HG', 'FTAG': 'AG', 'FTR': 'Res', 'Date': 'Date'
                })
                
                # إضافة عمود الدوري لتمييز البيانات
                df['League'] = league
                all_current_matches.append(df[['Date', 'Home', 'Away', 'HG', 'AG', 'Res', 'League']])
                print(f"✅ تم تحديث بيانات الدوري: {league}")
        except:
            continue

    if all_current_matches:
        final_db = pd.concat(all_current_matches, ignore_index=True)
        # حفظ الملف ليكون المصدر الأساسي للمنصة
        final_db.to_csv('updated_matches.csv', index=False)
        print(f"🚀 اكتمل التحديث! تم تسجيل {len(final_db)} مباراة من الموسم الحالي 2025-2026.")

if __name__ == "__main__":
    update_current_season_bot()
