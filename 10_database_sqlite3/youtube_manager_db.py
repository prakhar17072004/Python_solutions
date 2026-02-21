import sqlite3

conn=sqlite3.connect('youtube_videos.db')

cursor = conn.curser()

cursor.execute(''' 
      CREATE TABLE IF NOT EXIST videos(
               id INTGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL 
               )
''')

def list_videos(videos):
    pass
    

def main():
    while True:
        print("\nYoutube manger app with DB") 
        print("1.List Videos")
        print("2.Add Videos")
        print("3.Update Videos ")
        print("4. Delete Videos")
        print("5. Exit app")
        choice = input("Enter your choice :")

        if choice =='1':
            list_videos()
        elif choice == '2':
            name=input("Enter the videos name :")
            time= input("Enter the video time")
            add_video(name,time)



if __name__ == "__main__":
    main()