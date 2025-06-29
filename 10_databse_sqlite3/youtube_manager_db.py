import sqlite3

con = sqlite3.connect('youtube_videos.db')

cursor = con.cursor()

cursor.execute('''
               CREATE TABLE IF NOT EXISTS videos (
                   id INTEGER PRIMARY KEY,
                   name TEXT NOT NULL,
                   time TEXT NOT NULL
               )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(name,time,video_id):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name,time,video_id))
    con.commit()
    
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id, ))       # note that we can not pass only one value so coma after video_id is needed because it acpt tuple and when we put coma after atleast one varibale then it send as tuple
    con.commit()

def main():
    while True:
        print("\n Youtube videos manager with DB")
        print("1. List Videos")
        print("2. add videos")
        print("3. update videos")
        print("4. delete videos")
        print("5. exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")

            add_video(name,time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")

            update_video(name,time,video_id)
        elif choice == '4':
            video_id = input("Enter video ID to Delete: ")

            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice!!!")

    con.close()

if __name__ == "__main__":
    main()