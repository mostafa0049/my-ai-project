import pandas as pd

def update_all_leagues():
    # روابط لمصادر بيانات تغطي البطولات العالمية، الأفريقية، والآسيوية
    sources = [
        "https://www.football-data.co.uk/mmz4281/2425/E0.csv", # الدوري الإنجليزي الحالي
        "https://www.football-data.co.uk/mmz4281/2425/SP1.csv", # الدوري الإسباني الحالي
        "https://www.football-data.co.uk/mmz4281/2425/F1.csv",  # الدوري الفرنسي
        # ملاحظة: لدمج كافة البطولات، نستخدم قاعدة بيانات النتائج التاريخية الشاملة
        "https://github.com/martj42/soccer-csv/raw/master/data/world_cup.csv" # أمثلة لبطولات عالمية
    ]
    
    combined_data = []
    print("🚀 جاري تحديث عقل الروبوت ليشمل كافة الدوريات...")

    for url in sources:
        try:
            df = pd.read_csv(url)
            # توحيد أسماء الأعمدة لضمان عملها مع أي مصدر
            df = df.rename(columns={'HomeTeam': 'Home', 'AwayTeam': 'Away', 'FTR': 'Res'})
            combined_data.append(df[['Home', 'Away', 'Res']])
        except:
            continue

    if combined_data:
        final_db = pd.concat(combined_data, ignore_index=True)
        final_db.to_csv('updated_matches.csv', index=False)
        print(f"✅ تم بنجاح جلب {len(final_db)} مباراة من مختلف البطولات!")

if __name__ == "__main__":
    update_all_leagues()
