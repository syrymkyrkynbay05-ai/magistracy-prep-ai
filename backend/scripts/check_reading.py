import sqlite3

conn = sqlite3.connect("magistracy_prep.db")
cur = conn.cursor()

cur.execute(
    """
    SELECT reading_passage, COUNT(*) as cnt
    FROM questions 
    WHERE topic LIKE '%reading%' AND subject_id='english'
    GROUP BY reading_passage
    ORDER BY reading_passage
"""
)

rows = cur.fetchall()
print("=== БАЗАДАҒЫ READING МӘТІНДЕРІ ===\n")
for i, (passage, cnt) in enumerate(rows, 1):
    if passage:
        # Get first line as title
        title = passage.split("\n")[0][:60].strip()
        print(f'{i}. "{title}" — {cnt} сұрақ')

print(f"\n=== БАРЛЫҒЫ: {len(rows)} мәтін ===")

conn.close()
